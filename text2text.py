import os
import openai
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAIKEY")


def generate_answer(question):
    """
    Generates an answer to the given question using the OpenAI API.

    :param question: The question to generate an answer for.
    :return: The generated answer as a string.
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        # stop=[" Human:", " AI:"],
    )
    answer = response["choices"][0]["text"]
    return answer


# Example usage
# question = "What is the capital of France?"
# answer = generate_answer(question)
# print(answer)
