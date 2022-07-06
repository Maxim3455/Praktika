import webbrowser as wb
import speech_recognition as sr

def func3():
    print('Скажите')
    mic = sr.Microphone(device_index=2)


    f = sr.Recognizer()
    with sr.Microphone() as source:
        Audio = f.listen(source)


    b = f.recognize_google(Audio, language="ru-RU")
    wb.open("https://yandex.ru/search/?lr=213&text={}".format(b))
