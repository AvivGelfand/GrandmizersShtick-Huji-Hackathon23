# Import the necessary modules
from Scraping import get_today_articles_links,extract_article_content
from text2text import generate_answer
from helping_func import extract_dialogues
from text2speech import convert_text_audio,play_sounds_in_sequence
import datetime
import os

# the main prompt for the rest of the script
PROMPT = """create conversation between 2 people about the following article : {}
            with at least 8 responses for each person, use every time 
            person 1 : text..
            person 2 : response text..
            person 1 : response text..
             """

def print_time_stamp(art_ind:int)->None:
    """
    Prints the current timestamp and the value of art_ind.
    :param art_ind: an integer representing the art_ind of the article.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Row {art_ind+1} processed.")

def demo_process():
    """
    Play the audio files in the demo directory in sequence.

    :return: None
    """
    directory = "audio_files_demo"
    audio_files = [os.path.join(directory, audio) for audio in os.listdir(directory) if audio.endswith(".wav")]
    play_sounds_in_sequence(audio_files)


def real_process(NUMB_OF_ARTICLE, CHAR_OF_ARTICLE,max_tokens):
    """
    Process articles and generate audio files based on the content.

    :param NUMB_OF_ARTICLE: The number of articles to process.
    :param CHAR_OF_ARTICLE: The number of characters to consider from the article content.
    :return: A list containing the order of audio files generated.
    """
    ORDER_AUDIO = []

    # Read some data about the headlines from CBS
    article_links = get_today_articles_links(NUMB_OF_ARTICLE)
    for art_ind, article_l in enumerate(article_links):
        TEMP_ORDER_AUDIO = []

        # Extract a portion of the article content
        conv_topic = extract_article_content(article_l)[0:CHAR_OF_ARTICLE]

        # Ask the OpenAI ChatGPT
        generative_ans = generate_answer(PROMPT.format(conv_topic),max_tokens=max_tokens)
        print(generative_ans)

        # Extract dialogues from the generated answer
        person_a, person_b = extract_dialogues(generative_ans) #txt)

        # Convert the dialogues into audio files
        art_ind=0
        TEMP_ORDER_AUDIO = convert_text_audio(art_ind, person_a, person_b)

        # Add the TEMP_ORDER_AUDIO to the ORDER_AUDIO list
        ORDER_AUDIO.append(TEMP_ORDER_AUDIO)

        # Play the audio files in sequence
        play_sounds_in_sequence(TEMP_ORDER_AUDIO)

    return ORDER_AUDIO


def main(CHAR_OF_ARTICLE=200, NUMB_OF_ARTICLE=1,max_tokens=400, demo=True):
    """
      The main function for processing articles.

      :param CHAR_OF_ARTICLE: The desired number of characters per article.
      :param NUMB_OF_ARTICLE: The desired number of articles.
      :param max_tokens: The maximum number of tokens.
      :param demo: A boolean indicating whether to run in demo mode.
      :return: None
      """
    if demo:
        print("start demo")
        demo_process()
        "finish demo"
        return

    print("start real process")
    ORDER_AUDIO = real_process(NUMB_OF_ARTICLE, CHAR_OF_ARTICLE,max_tokens)
    print(ORDER_AUDIO)
    print("finish")


# main(CHAR_OF_ARTICLE=200,max_tokens=3500,demo=False)
main(demo=True)
