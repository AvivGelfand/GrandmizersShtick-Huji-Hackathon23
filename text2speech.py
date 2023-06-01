import os
from google.cloud import texttospeech_v1
import pygame

# set the code for the env
os.environ[
    'GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\orine\PycharmProjects\Hackathon23\stt-hackton23-ff184d52e37a.json"


def synthesize_text(text, save_name, gender, directory="audio_files"):
    """
    Synthesize text into speech and save it as a WAV file.

    :param text: The text to synthesize.
    :param save_name: The name of the WAV file to save.
    :param gender: The gender of the voice. Use "woman" for female and any other value for male.
    :param directory: The directory to save the WAV file (default is "audio_files").
    :return: The file path of the saved WAV file.
    """
    client = texttospeech_v1.TextToSpeechClient()

    input_text = texttospeech_v1.SynthesisInput(text=text)
    voice = texttospeech_v1.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Studio-O" if gender == "woman" else "en-US-Studio-M"
    )
    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.LINEAR16,
        pitch=-3.6,
        speaking_rate=1.3 if gender == "man" else 1.4
    )

    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config
    )

    os.makedirs(directory, exist_ok=True)  # Create the 'audio_files' directory if it doesn't exist
    file_path = os.path.join(directory, "{}.wav".format(save_name))

    with open(file_path, "wb") as out_file:
        out_file.write(response.audio_content)
        print("Audio content written to file '{}.wav'".format(save_name))

    return file_path


def convert_text_audio(art_ind, person_a, person_b):
    """
    Convert text dialogues into audio files.

    :param art_ind: The index of the article.
    :param person_a: A list of dialogues spoken by person A.
    :param person_b: A list of dialogues spoken by person B.
    :return: A list containing the file paths of the generated audio files.
    """
    TEMP_ORDER_AUDIO = []
    order_audio=0
    for ind_sentence in range(len(person_a)):
        temp_file_path_man = synthesize_text(person_a[ind_sentence],
                                             "article_{}{}_{}".format(art_ind, order_audio,"pers_a"), "man")
        order_audio+=1
        temp_file_path_woman = synthesize_text(person_b[ind_sentence],
                                               "article_{}{}_{}".format(art_ind, order_audio, "pers_b"), "woman")
        order_audio+=1
        TEMP_ORDER_AUDIO.extend([temp_file_path_man, temp_file_path_woman])

    return TEMP_ORDER_AUDIO


def play_sound(file_path):
    """
    Play a sound from the specified file path.

    :param file_path: The file path of the sound file to play.
    :return: None
    """
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def play_sounds_in_sequence(file_list):
    """
    Play a list of sound files in sequence.

    :param file_list: A list of file paths of the sound files to play.
    :return: None
    """
    for file_path in file_list:
        play_sound(file_path)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Adjust the tick value to control the delay

# Example usage
# synthesize_text("Hey, have you heard about Raven Tolbert?", "output_woman",woman= True)
# synthesize_text("No, I haven't. That sounds interesting! So", "output_man",woman=False)
# directory = "audio_files"
# audio_files = [os.path.join(directory, audio) for audio in os.listdir(directory) if audio.endswith(".wav")]
# play_sounds_in_sequence(audio_files)
