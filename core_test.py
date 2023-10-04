import modules.ipstack_api as ipstack
import modules.translate_api as translate
import modules.tts_api as tts
import modules.ipify_api as ipify
import modules.errors

userIP = ipify.get_ip()

userLanguage = ipstack.resolve_ip(userIP)
userMessage = translate.translate_string("Hello, this is a test, will this be in the correct language?", userLanguage)
print(userMessage)
with open('myfile.wav', mode='bw') as f:
            f.write(tts.text_to_speech(userMessage, userLanguage))
f.close()
