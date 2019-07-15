'''
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as mic:
    print("Say something...")
    audio = r.listen(mic)
    text = r.recognize_google(audio)
    print("You said :",text)
'''
import speech_recognition as sr

mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()
device_id = None

print("Welcome User".center(50))

while True:

    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id = i

    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
                            chunk_size = chunk_size) as source:

        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        print("Waiting for connection")
        
        text = r.recognize_google(audio)
        text = text.lower()
        print("you said: " + text)
