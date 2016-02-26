#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OSX Python Text to Speech and Speech Recognition

"""

import subprocess
import speech_recognition


recognizer = speech_recognition.Recognizer()


def say(text):
    """OS X has built in text to speech"""
    subprocess.call('say ' + text, shell=True)


def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_sphinx(audio)
        # or: return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

say("Say something!")
say("I heard you say " + listen())
