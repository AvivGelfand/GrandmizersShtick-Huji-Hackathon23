# Import the necessary modules
from Scraping import get_today_articles
from text2text import generate_answer

# Read some data about the headline from CBS
article_content = get_today_articles()

# Organize the question and add the 'fine tuning' in terms of the question itself
prompt = "..."

# Ask the OpenAI ChatGPT
# generative_ans = generate_answer(prompt)

# Convert the question into an audio file

# Play the audio file
