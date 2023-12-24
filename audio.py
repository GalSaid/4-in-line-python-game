import pyttsx3


def audio_start_game():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[1].id)  # setting up a female voice
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    engine.setProperty('rate', 150)  # setting up new voice rate
    engine.say("Welcome to four connect game!")
    engine.runAndWait()


def audio_end_game(win_sentence):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[1].id)  # setting up a female voice
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    engine.setProperty('rate', 150)  # setting up new voice rate
    engine.say(win_sentence)
    engine.runAndWait()

