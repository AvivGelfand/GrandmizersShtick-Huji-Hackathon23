# Import the necessary modules
from Scraping import get_today_articles
from text2text import generate_answer

# Read some data about the headline from CBS
article_content = get_today_articles()

# Organize the question and add the 'fine tuning' in terms of the question itself
prompt = f"""Task: Write a general conversation between two citizens, to be converted to an audio file, about the text of the article that follows the string TEXT_START and ends in TEXT_STOP. 
Style: Casual
Tone: Sarcastic
Audience: 40-year old
Length: 5 sentences each citizen
Format: json

TEXT_START
{article_content[0]}
TEXT_STOP"""


# Ask the OpenAI ChatGPT
generative_ans = generate_answer(prompt)
print(generative_ans)


# Convert the question into an audio file

# Play the audio file
