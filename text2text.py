import os
import openai
from dotenv import load_dotenv

# pip freeze > requirements.txt

# load the .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_answer(question, context):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"],
    )
    answer = response["choices"][0]["text"]
    return answer


response = openai.Completion.create(
    model="text-davinci-003",
    prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"],
)
print("response: \n", response)

# extract the answer from the response
answer = response["choices"][0]["text"]
print("answer: \n", answer)


generate_answer(
    "Write a conversation between to people about the weather. It needs to be good for audio generation.",
)
