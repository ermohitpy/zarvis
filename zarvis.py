import pyttsx3
import speech_recognition as sr
import datetime  
import wikipedia 
import webbrowser
#import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning")

	elif hour>=12 and hour<18:
		speak("Good Afternoon")

	else:
		speak("Good Evening")

	speak("hey!!, this is zarvis , How may i help you")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio,Language='en-in')
		print("User said: {query}")

	except Exception as e:
		print("Say that again please...,e")
		return "None"
	return query		
def sendEmail(do,content):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('luciferhostel@gmail.com','udemy@study')
	server.sendemail('prof.ashwinisaini@gmail.com',to,content)
	server.closed()


if __name__=="__main__":
	wishMe()
	while True:
		query = takeCommand().lower()
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia","")
			results = wikipedia.summary(query,sentence=2)
			speak("According to wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			webbrowser.open("youtube.com")


		elif 'open google' in query:
			webbrowser.open("google.com")


		elif 'open facebook' in query:
			webbrowser.open("facebook.com")


		elif 'open gmail' in query:
			webbrowser.open("gmail.com")
			

		# elif 'play music' in query:
		# 	music_dir = 'enter music directory here'
			# songs = os.listdir(music_dir)
			# os.startfile(os.path.join(music_dir,songs[0]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak("Sir,the time is {strTime}")

		elif 'open your code' in query:
			speak("We don't do this here")

		elif 'send email' in query:
			try:
				speak("what should i say?")
				content = takeCommand()
				to = "ermohit2k18@gmail.com"
				sendEmail(to,content)
				speak("Email has been sent")
			except Exception as e:
				print(e)
				speak("sorry bhai, nahi kr paya ") 

		elif 'send email to ashwani Sir' in query:
			try:
				speak("what should i say?")
				content = takeCommand()
				to = "ermohit2k18@gmail.com"
				sendEmail(to,content)
				speak("Email has been sent")
			except Exception as e:
				print(e)
				speak("sorry bhai, nahi kr paya ") 

		elif 'quit' in query:
			speak("Good Bye,See you soon")
			exit()		