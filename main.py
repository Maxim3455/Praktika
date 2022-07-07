import cod1
import cod2
import cod3
import cod4
import cod5
import cod6

import speech_recognition as sr

print('Если вы хотите сложить числа, скажите "сложение чисел"')
print('Если вы хотите открыть диспетчер задач, скажите "открыть диспетчер задач"')
print('Если вы хотите что-то найти в интернете, скажите "поиск в интернете"')
print('Если вы хотите открыть папку пользователя, скажите "открыть папку пользователя"')
print('Если вы хотите открыть панель управления, скажите "открыть панель управления"')
print('Если вы хотите включить или выключить звук, скажите "настройки звука"')
print('Если вы хотите выключить программу, скажите "выключить программу"')

while True:
    mic = sr.Microphone(device_index=2)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    a = r.recognize_google(audio, language="ru-RU")

    if a == 'сложение чисел':
        print(cod1.func1())
    elif a == 'открыть диспетчер задач':
        cod2.func2()
    elif a == 'поиск в интернете':
        cod3.func3()
    elif a == 'открыть папку пользователя':
        cod4.func4()
    elif a == 'открыть панель управления':
        cod5.func5()
    elif a == 'настройки звука':
        cod6.func6()
    elif a == 'Выключить программу':
        break