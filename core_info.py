# Modules
import os
import soundfile
import wave
from typing import List

# Custom Modules
try:
    from modules import language_functions
    from modules.errors import *
    from modules.weather_api import get_weather
    from core_text_types import add_text
except Exception as e:
    raise e

def get_info(ip_address: str, transl_lang: str) -> List[str]:
    
    # Getting weather info
    weather = get_weather(ip_address)
    hour = int(weather['local_time'].split(' ')[1].split(':')[0])
    temp_c = str(weather['temp_c']).split('.')[0]
    
    # Selecting greeting
    if hour < 13:
        greeting = 'Good Morning.'
    elif hour < 19:
        greeting = 'Good Afternoon.'
    elif hour < 23:
        greeting = 'Good Evening.'
    else:
        greeting = 'Good Night.'

    weather = 'The weather in your location is ' + weather['condition'].lower() + '.'
    temp = 'The temperature is ' + temp_c + ' degrees celsius.'
    
    info = [greeting, weather, temp]
    
    # Storing if not present
    for i in info:
        try:
            add_text(i, 'en')
        except TextTypeIsAlreadyStored as e:
            pass

    # Translating bits of info
    trans_info = ''
    audios_names = []
    try:
        os.mkdir('tmp')
    except Exception:
        pass
    result_audio = './tmp/end.wav'

    file_count = 0         

    # Translating and TTS every bit of info    
    for i in info:
        transl_text = language_functions.translate_string(i, transl_lang)
        trans_info += transl_text
        trans_info += ' '
        tts_audio = language_functions.text_to_speech(transl_text, transl_lang)

        # Storing files
        file = open(f'./tmp/{file_count}.wav', mode='wb')
        file.write(bytes(tts_audio))
        file.close()
        audios_names.append(f'./tmp/{file_count}.wav')
        file_count += 1
    
    # Preopening and refactoring of the file
    for audio_name in audios_names:
        data, samplerate = soundfile.read(audio_name)
        soundfile.write(audio_name, data, samplerate)

    # Creating a join-file info
    data= []
    for infile in audios_names:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
    
    # Creating the joined file
    output = wave.open(result_audio, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()

    # Saving bytes
    with open(result_audio, mode='rb') as f:
        audio = f.read()

    return (trans_info, audio)

if __name__ == '__main__':
    print(get_info('95.231.206.38', 'it'))

