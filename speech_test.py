import speech_recognition as sr
import time

print(sr.__version__)
r = sr.Recognizer()
r.dynamic_energy_threshold = False
r.energy_threshold = 400

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    try:
        print("speak")
        audio = r.listen(source,phrase_time_limit=5)
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN', show_all=False)
        print(f"User said: {query.lower()}\n")
        
    except sr.UnknownValueError:
        print("UnknownValueError")
    except sr.RequestError:
        print("Resquest Error")
    except Exception:
        print("Some Exception")