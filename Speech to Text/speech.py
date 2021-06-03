import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything: ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        text_file = open("speech_to_txt", "wt")
        text_file.write(text)
        text_file.close()
    except:
        print("Couldn't recognize the voice")
