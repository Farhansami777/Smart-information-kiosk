import speech_recognition as sr
import pvporcupine
import struct
import pyaudio
from gtts import gTTS
from datetime import datetime
import os
import webbrowser
import PyPDF2 as pdf2
import time
import subprocess
import datetime

import geocoder
#from playsound import playsound

USER = "sir"

g = geocoder.ip('me')
location = g.latlng
address = geocoder.osm(location, method='reverse').address

now = datetime.datetime.now()
current_time = now.strftime("%I:%M %p")

chromium_path = '/usr/bin/chromium-browser'
webbrowser.register('chromium', None, webbrowser.BackgroundBrowser(chromium_path))
# url = 'https://www.google.com/'


#url = "http://localhost/college%20web/index.html"
#url = "file:///var/www/html/te/final/index.html"
chromium_args = ['chromium-browser', '--noerrdialogs', '--disable-infobars', '--kiosk', url]


def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("voice.mp3")
    os.system("mpg321 voice.mp3")


r = sr.Recognizer()


def takeCommand():
    with sr.Microphone() as source:
        print("Listening for request...")
        audio = r.listen(source)
        query = ''
    try:
        print("Recognizing...", end="")
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
    except Exception as e:
        print("Exception:" + str(e))

    return query.lower()


current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")


def ConversationFlow():
    while True:
        userSaid = takeCommand()
        if "hello" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/index.html")
            speak("Hello there, Good to see you.")


        elif "class schedule" in userSaid:
            speak("Here is the class schedule for the current semester:")

        elif "location" in userSaid:

            tts = gTTS(text=f"You are currently at {address}")
            tts.save('location.mp3')
            os.system('mpg321 location.mp3')

        elif "where am i" in userSaid:

            tts = gTTS(text=f"You are currently at {address}")
            tts.save('location.mp3')
            os.system('mpg321 location.mp3')


        elif "where are you" in userSaid:
            tts = gTTS(text=f"You are currently at {address}")
            tts.save('location.mp3')
            os.system('mpg321 location.mp3')


        elif "who are you" in userSaid:
            speak("hello my name is jarvis i am just a rather very smart rebote:")

        elif "name" in userSaid:
            speak("hello my name is jarvis i am just a rather very smart rebote:")

        elif "hi" in userSaid:
            speak("hey there how is your day going")

        elif "hey" in userSaid:
            speak("hey there how is your day going")


        elif "thanks" in userSaid:
            speak("have a lovely day")

        elif "thank you" in userSaid:
            speak("have a lovely day")

        elif "rvce" in userSaid:
            speak("its a reputed college offering undergrad and postgrad degrees")

        #elif "rv" in userSaid:
         #   speak("its a reputed college offering undergrad and postgrad degrees")

        elif "developed" in userSaid:
            speak(
                " I am a smart information kiosk system made by student of e.i.e and the name of my creators are Ankita, Avian, Farhan, Kashish, Lathangi, Manuj, Niharika, Pavan, Saransh, Swati under the guidance of Doctor Kendagenna Swami")

        elif "developer" in userSaid:
            speak(
                " I am a smart information kiosk system made by student of e.i.e and the name of my creators are Ankita, Avian, Farhan, Kashish, Lathangi, Manuj, Niharika, Pavan, Saransh, Swati under the guidance of Doctor Kendagenna Swami")


        elif "terminate" in userSaid:
            speak("thank you for your time ")
            break;


            speak(
                "Educational Qualification	M.Tech, Ph.D Experience	Teaching: 29 yrs; Research: 06 yrs Area of Interest	Bio medical Engineering, VLSI, Embedded Systems, Microcontrollers, Digital Image Processing")
        elif "anand" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/anand_jatti.html")
            speak(
                "Educational Qualification	M.Tech, Ph.D Experience	Teaching: 17 yrs; Industry: 04 yrs; Research: 08 yrs Area of Interest	Image Processing, Signal Processing")

        elif "electronics and instrumentation" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/index.html")
            speak(
                "The Instrumentation Technology Department was established in the year 1981 with a Startup intake of 40 students and the current Intake is 60 students. The Instrumentation Technology was later nomenclated as Electronics and Instrumentation Engineering from the year 2014.")

        elif "EIE" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/index.html")
            speak(
                "The Instrumentation Technology Department was established in the year 1981 with a Startup intake of 40 students and the current Intake is 60 students. The Instrumentation Technology was later nomenclated as Electronics and Instrumentation Engineering from the year 2014.")


        elif "EI" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/index.html")
            speak(
                "The Instrumentation Technology Department was established in the year 1981 with a Startup intake of 40 students and the current Intake is 60 students. The Instrumentation Technology was later nomenclated as Electronics and Instrumentation Engineering from the year 2014.")


        elif "E&i" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/index.html")
            speak(
                "The Instrumentation Technology Department was established in the year 1981 with a Startup intake of 40 students and the current Intake is 60 students. The Instrumentation Technology was later nomenclated as Electronics and Instrumentation Engineering from the year 2014.")


        elif "E and I" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/index.html")
            speak(
                "The Instrumentation Technology Department was established in the year 1981 with a Startup intake of 40 students and the current Intake is 60 students. The Instrumentation Technology was later nomenclated as Electronics and Instrumentation Engineering from the year 2014.")


        elif "E n I" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/index.html")
            speak(
                "The Instrumentation Technology Department was established in the year 1981 with a Startup intake of 40 students and the current Intake is 60 students. The Instrumentation Technology was later nomenclated as Electronics and Instrumentation Engineering from the year 2014.")

        elif "hod" in userSaid:
            webbrowser.get('chromium').open("file:///home/pi/Downloads/png/renu_madhavi.html"
                                            "", new=0)
            speak(
                "Educational Qualification	M.Tech, Ph.D Experience	Teaching: 29 yrs; Research: 06 yrs Area of Interest	Bio medical Engineering, VLSI, Embedded Systems, Microcontrollers, Digital Image Processing")


        elif "head of department" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/renumadhavi.html")
            speak(
                "Educational Qualification	M.Tech, Ph.D Experience	Teaching: 29 yrs; Research: 06 yrs Area of Interest	Bio medical Engineering, VLSI, Embedded Systems, Microcontrollers, Digital Image Processing")


        elif "college of engineering" in userSaid:
            speak("its a reputed college offering undergrad and postgrad degrees")


        elif "time" in userSaid:

            tts = gTTS(text=f"The current time is {current_time}")
            tts.save('time.mp3')
            os.system('mpg321 time.mp3')


        elif "bye" in userSaid:
            speak("Goodbye. Have a great day")
            break

        elif "harsha" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/harsha.html")
            speak(
                "Qualification is M.Tech. Ph.D, Experience Teaching is 13 years; Industry experience of 2 years; Research experience of 6 years and Area of Interest is in Medical Image Processing, Nueral Network")
        elif "padmajha" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/padamaja.html")
            speak(
                "Educational Qualification is M.Tech,  Ph.D, Experience    in Teaching: 29 yrs; Research: 14 yrs,Area of Interest    Biomedical Signal Processing, Computer Communication Network, Measurement and Instrumentation")
        elif "prasanna kumar" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/prasanna.html")
            speak(
                "Qualification    M.Tech, Ph.D, Experience, Teaching: 21yrs, Industry: 01 yrs Research: 08 yrs, Area of Interest Signal Processing (Acoustic Signal Processing), Biomedical Engineering")
        elif "venkatesh" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/venkatesh.html")
            speak(
                "Educational Qualification    M.Tech, B.Sc    Teaching: 31 yrs; Research: 05 yrs, Industry: 03 yrs Area of Interest Instrumentation, Process Control and Automation")
        elif "deepashree" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/deepashree.html")
            speak(
                "Educational Qualification    M.Tech, Ph.D Experience    Teaching: 12 yrs; Industry: 04 yrs; Research: 04 yrs Area of Interest    Medical Image Processing, Biomedical Instrumentation, Signal Processing")
        elif "tabitha" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/tabitha.html")
            speak(
                " Educational Qualification    M.Tech, Ph.D Experience    Teaching: 13 yrs; Research: 05 yrs Area of Interest    Image Processing, Biomedical Signal Processing, Biosensor ")
        elif "swami" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/k_swami.html")
            os.system("mpg321 voice/swami.mp3")
            # speak("Assistant Professo Qualification	M.Tech. Ph.D Experience	Teaching: 11yrs; Industry: 6 yrs; Research:6 yrs Area of Interest	VLSI Design , NOC,His achievments are :Flexible Electronics Mentor Award for Anveshan 2020 Design fellowship program conducted by analog devices, Bengaluru. Felicitated for completion of Ph.D 2019-20, by RSST Trust Felicitated for Presenting a Paper in International Conference during 2018-19, by RSST Trust Felicitated for completion of Ph.D 2019-20 in RVCE")
        elif "rachana" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/rachna.html")
            speak(
                "Educational Qualification is M.Tech,  Ph.D in IIT-Madras, Experience	in Teaching: 15 yrs; Research: 04 yrs,Area of Interest	Biomedical Imaging, Microwave Imaging, Thermal Imaging, Radiometry")
        elif "ramesh" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/kbr.html")
            speak(
                "Qualification	M.Tech, Ph.D, Experience, Teaching: 25yrs, Research: 07 yrs, Area of Interest	Signal Processing, Embedded System, Biomedical engineering")
        elif "renu madhavi" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/renumadhavi.html")
            speak(
                "Educational Qualification	M.Tech, Ph.D Experience	Teaching: 29 yrs; Research: 06 yrs Area of Interest	Bio medical Engineering, VLSI, Embedded Systems, Microcontrollers, Digital Image Processing")
        elif "jatti" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/anand_jatti.html")
            speak(
                "Educational Qualification	M.Tech, Ph.D Experience	Teaching: 17 yrs; Industry: 04 yrs; Research: 08 yrs Area of Interest	Image Processing, Signal Processing")
        elif "rajashree" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/rajasree.html")
            speak(
                " Educational Qualification	M.Tech, Ph.D Experience	Teaching: 12 yrs; Industry: 05 months Area of Interest	Digital Image Processing, Biomedical Instrumentation, Virtual Instrumentation")
        elif "veena" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Teachers/veena.html")
            speak(
                "Qualification	B.E,M.Tech, Ph.D Experience	Teaching: 10 yrs; Industry: 02 yrs; Research: 06 yrs Area of Interest	 Biomedical Image Processing, Digital Image Processing, ARM Processors, Embedded Systems, Biomedical Instrumentation.")
        elif "principle" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Principal.html")
            speak(
                "Dr. K N Subramanya is presently the Principal and Professor, Department of Industrial Engineering and Management at R V College of Engineering. His Academic Qualification includes: Ph.D. in Supply Chain Management (Avinashilingam University, Coimbatore), MBA with HR specialization (5th Rank), M.Tech. in Industrial Management (IITM, Chennai) and B.E in Industrial and Production Engineering (Bangalore University).")
        elif "principal" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Principal.html")
            speak(
                "Dr. K N Subramanya is presently the Principal and Professor, Department of Industrial Engineering and Management at R V College of Engineering. His Academic Qualification includes: Ph.D. in Supply Chain Management (Avinashilingam University, Coimbatore), MBA with HR specialization (5th Rank), M.Tech. in Industrial Management (IITM, Chennai) and B.E in Industrial and Production Engineering (Bangalore University).")

        elif "Subramanya" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/Principal.html")
            speak(
                "Dr. K N Subramanya is presently working as Principal and Professor, Department of Industrial Engineering and Management at R V College of Engineering. His Academic Qualification includes: Ph.D. in Supply Chain Management (Avinashilingam University, Coimbatore), MBA with HR specialization (5th Rank), M.Tech. in Industrial Management (IITM, Chennai) and B.E in Industrial and Production Engineering (Bangalore University).")
        # different course

        elif "1st semester" in userSaid:
            speak(
                "according to 2018 scheme 1st sem courses are Engineering Mathematics-I, Engineering Physics,Elements of Electrical Engineering, Elements of Civil Engineering, Elements of Engineering, Computer Aided Engineering Drawing English Language Laboratory-1")
        elif "2nd semester" in userSaid:
            speak(
                "according to 2018 scheme 2nd sem courses are Engineering Mathematics-I,Engineering Chemistry, Programing in C, Elements of Electronics Engineering, Elements of Mechanical Engineering,English Language Laboratory-1")
        elif "3rd semester" in userSaid:
            speak(
                "according to 2018 scheme,,3rd sem courses are Discrete and Integral Transforms, Environmental Technology, Analog Electronic Circuits, Analysis & Design of Digital Circuits, Data Structures using c, Measurement & Process Instrumentation, Bridge Course: Mathematics, Kannada Course:")
        elif "4th semester" in userSaid:
            speak(
                "4th sem courses are Linear Algebra, Statistics and Probability, Engineering Materials, Sensors and Actuators, Microprocessor & Microcontroller, Signals and Systems, Control Systems, Design Thinking lab, Bridge Course: C Programming, ProfessionalPractice-I")
        elif "5th semester" in userSaid:
            speak(
                "Courses offered are Foundations of Management and Economics,Data Networks,DSP,virtual instrumentation,global")
        elif "6th semester" in userSaid:
            speak(
                "Course offered are IPR & Entrepreneurship,Automatic Process Control Technology,Advanced Micro-controller & Application")
        elif "7th semester" in userSaid:
            speak(
                "Course offerd are Industrial Automation Technology,Constitution of India and Professional Ethic,Advamced Image processing")
        elif "8th semester" in userSaid:
            speak("Major project")
        elif "courses" in userSaid:
            speak(
                "he syllabi of the courses are contemporary and constantly updated as per industry needs and the laboratories are modernized to reflect the latest changes in technology ")
        elif "bank" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/bank.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "admin" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/Admin.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "aerospace" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/Aerospace.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "badminton" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/badminton.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "biotech" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/Biotech.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "bus shelter" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/BusShelter.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "cauvery" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/Cauvery.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "civil" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/civil.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "computer science" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/ComputerScience.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "dtl" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/dtl.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "electrical" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/Electrical.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "industrial" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/IndustrialDept.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "information science" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/InformationScience.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "library" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/Library.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "mechanical" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/mech.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "reasearch" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/R_D.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "shrishivanand" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/ShriShivanand.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "telecommunication" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/Telecommunication.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "workshop" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/Workshop.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "food" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/FoodCourt.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "temple" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/GaneshTemple.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "lounge" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/LOCATION/VIPLounge.html")
            speak("Here is the map to reach the desired location and for further info you can scan the QR and respective link provided on screen ")
        elif "ranking" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/blog.html")
            speak("Here is the ranking of the college  ")
        elif "placement" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/blog.html")
            speak("Here is the placements details of the college and list of all companies that are visiting our campus thank you")
        elif "coe" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/COE.html")
            speak("there are different coe in the college here is the list of all coe thank you")
        elif "center of excellance" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/COE.html")
            speak("there are different COE in the college here is the list of all COE thank you ")
        elif "lab" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/labs.html")
            speak("here is Department of Electronics & Instrumentation Engineering Labs Infrastructure thank you")
        elif "course" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/course.html")
            speak("here are different courses provided by our college thank you")
        elif "teachers" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/teachers.html")
            speak("here is detail of eie teachers thank you ")
        elif "contacts" in userSaid:
            webbrowser.open_new("/home/pi/Desktop/college web/contacts.html")
            speak("here you can contact us for any query kindly share you details and query thank you")
        else:
            speak("Invalid option. Please try again.")

        time.sleep(10)


def main():
    # webbrowser.open_new("http://localhost/vlsi/k_swami.html")
    subprocess.Popen(chromium_args)
    # webbrowser.get('chromium').open("http://localhost/college%20web/index.html", new=0)
    porcupine = None
    pa = None
    audio_stream = None

    print("Jarvis is online and ready!")
    print("**")
    print("Jarvis : Awaiting your call")
    try:
        porcupine = pvporcupine.create(keywords=["jarvis", "computer"])
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length)

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Hotword detected...", end="")
                speak("Hello there,I am an intelligent system made my the student of EIE Department")
                ConversationFlow()
                time.sleep(1)
                print("Jarvis :Awaiting your call")

    finally:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()


main()