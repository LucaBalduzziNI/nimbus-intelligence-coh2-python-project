from gui.Home import home

#tmp1 = text_to_speech('ciao', 'en-us')
#encoded = base64.b64encode(tmp1)
#print(execute_query('insert into translations (language_code, target_audio_bin) values (%s, %s)', ('test2', tmp1)))
#audio = execute_query('select target_audio_bin from translations where language_code = %s limit 1', ('test45'))#[0]['TARGET_AUDIO_BIN']
#print(audio)


#with open('working.wav', mode='bw') as f:
    #tmp2 = base64.b64decode(audio)
    #if tmp1 == tmp2:
        #print('true')
    #f.write(tmp2)

    #f.write(base64.b64decode(audio))

#with open('not_working.wav', mode='bw') as f:
    #f.write(bytes(audio))

if __name__ == '__main__':
    home()