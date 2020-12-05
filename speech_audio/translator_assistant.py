# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 03:01:00 2020

@author: senol
"""

def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

def fix_link(sentence):
    sentence_list = list(sentence)
    space_list = get_index_positions(sentence_list, " ")
    for i in space_list:
        sentence_list[i] = "%20"
        
    new_sentence = "".join(sentence_list)
    new_sentence = str(new_sentence)
        
    return new_sentence

#%%
import speech_recognition as sr
import webbrowser
import time
from sys import exit
from gtts import gTTS
from playsound import playsound
import random
import os


r = sr.Recognizer()

def record(ask = False):        
    with sr.Microphone() as source:
        if ask:
            speak(ask)
            
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio)
            
        except sr.UnknownValueError:
            speak("Sorry! I did't understand.")       
            
        except sr.RequestError:
            speak("System is not working.")
            
        return voice
    
def response(voice):
    if 'Translate' in voice:
        sentence = record('what do you want to translate')
        url_sentence = fix_link(sentence)
        url = "https://translate.google.com/?sl=en&tl=tr&text="+url_sentence+"&op=translate"
        webbrowser.get().open(url)
        
    if 'thank you' in voice:
        speak("Good Bye")
        exit()
        
def speak(string):
    tts = gTTS(string)
    rand = random.randint(1, 100)
    file = 'translate-audio-'+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("How can I help you.")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)


        