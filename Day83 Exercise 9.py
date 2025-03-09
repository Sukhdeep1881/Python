# Python program to convert text to speech

# win32com module library is used to convert text to speech
import win32com.client

# interact with microsoft speech SDK to speak
speaker = win32com.client.Dispatch("SAPI.SpVoice")

listOfPeople = ["Sukhdeep Singh", "Rajvir Singh", "Dev", "Kunal", "Himani"]

# while True:
#     print("Enter the word to speak it out by computer")
#     s = input()
#     speaker.Speak(s)
#     break

def speak(text = 0):
    if text == len(listOfPeople):
       return 0
    else:
        print(f"Shoutout to {listOfPeople[text]}")
        speaker.Speak(f"Shoutout to{listOfPeople[text]}")
    return speak(text + 1)

speak()





