import speech_recognition
import keyboard

sr = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)

    while True:
        try:
            audio = sr.listen(source=mic)

            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            print(query)

            if query == 'начать клип' or query == 'закончить клип':
                keyboard.send('alt+f9')
        except Exception as e:
            print(e)
