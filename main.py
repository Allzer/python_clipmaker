import datetime
import os
import speech_recognition

sr = speech_recognition.Recognizer()
time_start = datetime.datetime.now()
file_name = ('timecodes/time_code_{}.txt').format(datetime.datetime.today().strftime("%d.%m.%Y"))

if os.path.exists(file_name) == False:
    os.mkdir('timecodes')

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)

    while True:
        try:
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            print(query)

            if query == 'сделай клип':
                print(datetime.datetime.now()-time_start)
                with open(file_name, 'a', encoding='utf-8') as file:
                    file.write(f'{datetime.datetime.now()-time_start}\n')

        except Exception as e:
            print(e)
