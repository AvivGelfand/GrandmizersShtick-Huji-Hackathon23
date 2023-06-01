import re
from typing import Tuple, List


def line_contains_colon(line: str) -> bool:
    """
    Check if a line contains a colon.

    :param line: The line to check.
    :return: True if the line contains a colon, False otherwise.
    """
    pattern = r':'
    return bool(re.search(pattern, line))


def clean_until_pers(text: str) -> str:
    """
    Clean the text until the occurrence of "Person".

    :param text: The text to clean.
    :return: The cleaned text starting from the occurrence of "Person" or the original text if "Person" is not found.
    """
    person_index = text.find('Person')
    if person_index != -1:
        return text[person_index:]
    else:
        return text


def extract_dialogues(conversation_text) -> tuple[list[str], list[str]]:
    """
    Extract dialogues from the conversation text(the ChatGPT response).

    :param conversation_text: The text containing the conversation.
    :return: A tuple containing the dialogues spoken by person A and person B.
    """
    person_a_dialogue = []
    person_b_dialogue = []

    conversation_text = clean_until_pers(conversation_text)
    lines = [line for line in conversation_text.split('\n') if line != ""]

    for ind, line in enumerate(lines):
        line = line.strip()
        if not line_contains_colon(line):
            continue
        if ind % 2 == 0:
            person_a_dialogue.append(line.split(":")[1])
        else:
            person_b_dialogue.append(line.split(":")[1])

    min_len = min(len(person_a_dialogue), len(person_b_dialogue))
    return person_a_dialogue[:min_len], person_b_dialogue[:min_len]

# Example usage
txt ="""
Person 1: Did you hear about that building in Iowa that collapsed?
Person 2: Yeah, it's crazy! They said three people are still unaccounted for?
Person 1: Yeah, Branden Colvin, Ryan Hitchcock and Sarah Elwood. I can't imagine how scared their families must be.
Person 2: I know, it's tragic. It's a reminder that sometimes even the strongest buildings can succumb to forces of nature.
year-old Sarah Elwood.
Person 1: Did you hear about that building in Iowa that collapsed?
Person 2: Yeah, it's crazy! They said three people are still unaccounted for?
Person 1: Yeah, Branden Colvin, Ryan Hitchcock and Sarah Elwood. I can't imagine how scared their families must be.
Person 2: I know, it's tragic. It's a reminder that sometimes even the strongest buildings can succumb to forces of nature.
"""
test_dig = txt
extract_dialogues(test_dig)
