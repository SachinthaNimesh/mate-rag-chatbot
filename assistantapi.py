# this script uses open ai assistant api for chatbot responses
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
import re
import time
from openai import OpenAI
import glob # to import .md files from mate-bot2/data

# Load environment variables from .env file
load_dotenv('.env')


api_key = os.environ.get("OPENAI_API_KEY")
assistant_id = os.environ.get("ASSISTANT_ID")

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN_1"))


###
def load_openai_client_and_assistant():
    client = OpenAI(api_key=api_key)
    my_assistant = client.beta.assistants.retrieve(assistant_id)
    thread = client.beta.threads.create()

    # Create a vector store called "Financial Statements"
    vector_store = client.beta.vector_stores.create(name="Metana database")
    data_directory = "/Users/nimesh/Documents/GitHub/mate-bot2/data/metana-posts"
    # Get the first three markdown files in the data directory
    file_paths = glob.glob(os.path.join(data_directory, "*.md"))[:3]
    if not file_paths:
        raise ValueError("No markdown files found in the data directory")

    file_streams = [open(path, "rb") for path in file_paths]

    # Print the file paths to verify
    print("Markdown files selected for upload:")
    for path in file_paths:
        print(path)

    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id, files=file_streams
    )

    # Print the status and the file counts of the batch to see the result of this operation.
    print(file_batch.status)
    print(file_batch.file_counts)

    # Update the assistant to use the new Vector Store
    my_assistant = client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
    )

    return client, my_assistant, thread


client, my_assistant, assistant_thread = load_openai_client_and_assistant()
###

###
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run
###

###


# initiate assistant ai response
def get_assistant_response(user_input=""):
    message = client.beta.threads.messages.create(
        thread_id=assistant_thread.id,
        role="user",
        content=user_input,
    )

    run = client.beta.threads.runs.create(
        thread_id=assistant_thread.id,
        assistant_id=assistant_id,
    )

    run = wait_on_run(run, assistant_thread)

    # Retrieve all the messages added after our last user message
    messages = client.beta.threads.messages.list(
        thread_id=assistant_thread.id, order="asc", after=message.id
    )

    # Extract and clean the text content from messages
    response_text = messages.data[0].content[0].text.value
    cleaned_response = clean_response_text(response_text)
    return cleaned_response
###

###
def clean_response_text(response_text):
    # Remove  ,  , etc. patterns
    cleaned_text = re.sub(r'【\d+:\d+†source】', '', response_text)
    return cleaned_text.strip()
###
    

# Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    print(message)

    assistant_response = get_assistant_response(message["text"])
    formatted_response = f"{assistant_response}"
    blocks = [
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
    say({
        "blocks": blocks
    })




# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN_1"]).start()
