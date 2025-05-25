import speech_recognition as sr  
import os
import sys
import serial  
import time    

try:
    arduino = serial.Serial(port='/dev/cu.usbserial-10', baudrate=9600, timeout=1)
    time.sleep(2)
    print("Arduino connected successfully!")
except Exception as e:
    print(f"Failed to connect to Arduino: {e}")
    arduino = None

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-IN")
            print(f"You said: {query}")
            return query.lower()
        except Exception as e:
            print("Sorry, I couldn't understand.")
            return "error"

q = 0

if __name__ == "__main__":
    say("Voice assistant ready")

    while True:
        command = takeCommand()

        if "turn on presentation mode" in command:
            say("Turning on presentation mode")
            if arduino:
                arduino.write(f"{q}\n".encode())
                arduino.flush() 
                print(f"Sent to Arduino: {q}")
            else:
                print("Arduino not connected")

            while True:
                command = takeCommand()

                if "turn off" in command:
                    say("Shutting down")
                    if arduino:
                        q = 2
                        arduino.write(f"{q}\n".encode())
                        print(f"Sent to Arduino: {q}")
                    break

                elif "quit" in command:
                    say("Thanks")
                    if arduino:
                        arduino.close()  # Close serial connection
                    sys.exit()

        elif "quit" in command:
            say("Goodbye!")
            if arduino:
                arduino.close()
            sys.exit()