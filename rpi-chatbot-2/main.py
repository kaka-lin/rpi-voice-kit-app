import aiy.audio
from gtts import gTTS
import speech_recognition as sr
import pygame
from fake_chatbot import chatbot

def play_test(fd):
    pygame.init()
    #pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load(fd)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        question = r.recognize_google(audio, language="zh-TW")
        print("question: {}".format(question))
        answer = chatbot(question)
        print("answer: ", answer)
        if answer == '':
            answer = '蛤，請再說一次！'
        tts = gTTS(answer, lang='zh-tw')
        tts.save('answer.mp3')
        play_test('answer.mp3')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
