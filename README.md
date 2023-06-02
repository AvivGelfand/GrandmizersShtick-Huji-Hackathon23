# Text-to-Speech Article Reader

This project is a Python application that converts text articles into audio files using the Google Cloud Text-to-Speech API. It provides a graphical user interface (GUI) for easy interaction.

## Features

- Scrapes articles from websites and extracts their content.
- Uses ChatGPT to generate answers based on user input.
- Converts text to speech using the Google Cloud Text-to-Speech API.
- Plays the generated audio files in sequence.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/text-to-speech-article-reader.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set the Google Cloud API key in the environment variable `GOOGLE_APPLICATION_CREDENTIALS`.
4. Modify the script parameters in `main_process_voices.py` as needed.
5. Run the application: `python main_and_gui.py`

## Usage

1. Open the graphical user interface by running `main_and_gui.py`.
2. Click the "I'm leaving home" button to start processing the articles and generating audio files.
3. Click the "Break Run" button to stop the execution and turn off the sound.

**Note:** The application is currently set to run in demo mode, playing pre-recorded audio files. Modify the parameters in the `main_process_voices` function and set `demo` to `False` for real article processing.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

The application uses the following libraries:

- `tkinter` for creating the GUI.
- `ttkthemes` for applying themed styles to the GUI.
- `subprocess` for executing shell commands.
- `time` for adding delays in the script.
- Custom modules for web scraping, generating answers, extracting dialogues, and text-to-speech conversion.

## Disclaimer

This application is provided as-is without any warranty. Use it at your own risk. Be aware of the terms and conditions of the websites you scrape articles from and comply with them.

Please note that the usage of the Google Cloud Text-to-Speech API may incur charges. Check the pricing details on the Google Cloud website before using the API.
