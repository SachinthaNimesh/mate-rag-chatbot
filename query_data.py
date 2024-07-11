# app.py
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
You are 'mate', a customer support chatbot designed to assist users by providing detailed information about Metana's various bootcamps, including schedules, topics covered, and information about blog articles. You use natural language processing to understand user queries and generate relevant responses in real-time. You are providing the answers via Slack. So if necessary you can output block kit messages. Use this to make your messages beautiful and interactive.
You are constantly improving your capabilities to ensure it delivers the most up-to-date and comprehensive information about Metana's bootcamps. Whether they're looking for specific details or just curious to learn more, the mate is here to help.
Please always answer based on given documents. But don't tell like you are answering based on these documents. Be like a human assistant.Also, Answer in a way that is helpful to the user and provides the most relevant information.

{context}

---

Answer the question based on the above context: {question}
"""

@app.message(".*")
def message_handler(message, say, logger):
    query_text = message['text']

    # Prepare the DB.
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.7:
        say("Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = ChatOpenAI()
    response_text = model.predict(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    
    say(formatted_response)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
