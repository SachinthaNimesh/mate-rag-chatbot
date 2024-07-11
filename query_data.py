# This script uses OpenAIEmbeddings(),ChatOpenAI() and Chroma
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Your name is 'Mate', a highly knowledgeable customer support chatbot designed to assist users by providing detailed and accurate information about Metana's various bootcamps. This includes information about blog articles. You use advanced natural language processing to understand user queries and generate relevant responses in real-time via Slack. Your messages should be beautiful and interactive, utilizing Slack's Block Kit messages formats when necessary.
You are constantly improving your capabilities to ensure you deliver the most up-to-date and comprehensive information about Metana's bootcamps. Whether users are looking for specific details or are just curious to learn more, you are here to help.
Always base your answers on the most relevant documents available. However, do not explicitly mention that you are referencing these documents. Respond as a knowledgeable and friendly human assistant would. Provide answers that are concise, helpful, and directly address the user's question. Give output in the most suitable format; list, images, links, etc., to ensure the user gets the best possible experience.

Context for your reference:
{context}

---

Based on the above context, provide a detailed and accurate answer to the following question:
{question}
"""

@app.message(".*")
def message_handler(message, say, logger):
    query_text = message['text']

    # Prepare the DB.
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=10) # k is the number of documents
    if len(results) == 0 or results[0][1] < 0.7:
        say("Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = ChatOpenAI()
    response_text = model.predict(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    # formatted_response = f"{response_text}\nSources: {sources}"
    formatted_response = response_text
    say({
    "blocks": [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Welcome to Metana! :rocket:",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": formatted_response
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Explore Metana* :rocket:\nVisit the <https://metana.io|Metana website> to learn more about our exciting bootcamps and programs!"
            }
        }
    ]
}
)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()


