De Grandmizer Shtick
This repository contains scripts for generating and playing audio conversations between two people based on scraped article content. The conversation generation is done using OpenAI's ChatGPT model, and the audio synthesis is performed using Google Cloud Text-to-Speech API.

Scripts
main_and_gui.py
This script contains the graphical user interface (GUI) for controlling the conversation generation and audio playback. It uses the Tkinter library for creating the GUI window and the ThemedStyle from ttkthemes for styling. The GUI window provides buttons to start the conversation generation process and play the generated audio. It also has a button to stop the conversation generation.

main_process_voices.py
This script is responsible for the main process of generating conversations based on scraped articles. It imports functions from other scripts for article scraping, text generation, and audio synthesis. The main_process_voices function is the entry point, which takes parameters such as the number of articles to process, the number of characters to consider from the article content, and the maximum number of tokens for text generation. It uses the get_today_articles_links function from Scraping.py to get the links to the articles, then extracts the article content using the extract_article_content function. The article content is used as a prompt for the conversation generation using the generate_answer function from text2text.py. The dialogues are extracted from the generated answer using the extract_dialogues function from helping_func.py, and then converted into audio files using the convert_text_audio function from text2speech.py. The generated audio files are played in sequence using the play_sounds_in_sequence function from text2speech.py.

text2speech.py
This script contains functions for synthesizing text into speech using the Google Cloud Text-to-Speech API and playing the generated audio files. The synthesize_text function takes text, save name, and gender parameters and synthesizes the text into speech using the API. The convert_text_audio function takes dialogues spoken by person A and person B, and converts them into audio files using the synthesize_text function. The play_sound function plays a sound from a specified file path, and the play_sounds_in_sequence function plays a list of sound files in sequence.

text2text.py
This script contains the generate_answer function, which uses OpenAI's ChatGPT model to generate an answer based on a given prompt. It makes use of the OpenAI API to interact with the model and retrieve the generated answer.

Scraping.py
This script contains functions for web scraping articles from a specific website. The create_soup function creates a BeautifulSoup object from a provided URL. The get_today_articles_links function retrieves a list of articles published today on a specific website. The extract_article_content function extracts the content of an article from a provided URL.

Dependencies
The following dependencies are required to run the scripts:

Python 3.x
Tkinter
ttkthemes
BeautifulSoup
requests
google-cloud-texttospeech
pygame
openai
dotenv
Please make sure to install these dependencies before running the scripts.

Usage
To use the application, follow these steps:

Install the required dependencies mentioned above.
Make sure to set the Google Cloud API key in the environment variable GOOGLE_APPLICATION_CREDENTIALS.
Modify the script parameters as needed in the main_process_voices function in main_process_voices.py.
Run the main_and_gui.py script to open the graphical user interface.
Click the "I'm leaving home button to start the main_process_voices script, which will generate audio files based on the articles' content. The generated audio files will be played in sequence.

Click the "Break Run" button to stop the execution of the main_process_voices script and turn off the sound.

Note: The script is currently set to run in demo mode, which plays pre-recorded audio files. If you want to process real articles and generate audio files based on the content, you can modify the parameters in the main_process_voices function and set the demo parameter to False.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
The script uses the following libraries:

tkinter: For creating the graphical user interface.
ttkthemes: For applying themed styles to the GUI.
subprocess: For executing shell commands to start/stop the main_process_voices script.
time: For adding delays in the script.
Scraping: A custom module for web scraping articles and extracting their content.
text2text: A custom module for generating answers using ChatGPT.
helping_func: A custom module for extracting dialogues from generated answers.
text2speech: A custom module for converting text to speech using the Google Cloud Text-to-Speech API.
Disclaimer
This script is provided as-is without any warranty. Use it at your own risk. Be aware of the terms and conditions of the websites you scrape articles from and comply with them.

Please note that the usage of the Google Cloud Text-to-Speech API may incur charges. Make sure to check the pricing details on the Google Cloud website before using the API.
