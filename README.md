# De Grandmizer Shtick

![De Grandmizer Shtick](images/De_Grandmizer_Shtick_photo.jpg)

De Grandmizer Shtick is a Python application that generates conversations using ChatGPT and converts them into audio files using the Google Cloud Text-to-Speech API. It provides a graphical user interface (GUI) for easy interaction. The project is designed to help create the illusion of an occupied home do intimidate burlaries and creaeted during HUJI hacaton 2023.

## Features

- Scrapes articles from websites and extracts their content.
- Uses ChatGPT to generate answers based on user input.
- Converts text to speech using the Google Cloud Text-to-Speech API.
- Plays the generated audio files in sequence.

## Installation

1. Clone the repository: `git clone https://github.com/AvivGelfand/Hackathon23/edit/master/`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set the Google Cloud API key in the environment variable `GOOGLE_APPLICATION_CREDENTIALS`.
4. Modify the script parameters in `main_process_voices.py` as needed.
5. Run the application: `python main_and_gui.py`

## Usage

1. Open the graphical user interface by running `main_and_gui.py`.
2. Click the "I'm leaving home, turn on sound" button to start processing the articles and generating audio files.
3. Click the "I'm back, turn off sound" button to stop the execution and turn off the sound.

**Note:** The application is currently set to run in demo mode, playing pre-recorded audio files. Modify the parameters in the `main_process_voices` function and set `demo` to `False` for real article processing.


Please note that the usage of the Google Cloud Text-to-Speech and OpenAi API   may incur charges. Check the pricing details before using the API.
