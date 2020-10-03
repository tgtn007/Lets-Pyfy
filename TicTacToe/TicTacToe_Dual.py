import pyttsx3 
import datetime
engine = pyttsx3.init('sapi5') 
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

rate=engine.getProperty("rate")
engine.setProperty("rate",125)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    time=int(datetime.datetime.now().hour)
    if time>=6 and time<12:
        speak("Good morning, sir")
    elif time>=12 and time<14:
        speak("Good noon, sir")
    elif time>=14 and time<17:
        speak("Good afternoon, sir")
    elif time>=17 and time<21:
        speak("Good evening, sir")
    else:
        speak("Good night, sir, It's not the perfect time for playing, but you are an engineer So Let's play. ")

wish()
speak("I am your assistant\n 'Enter your name 1st player : '")
Player_1=input()
speak('Enter your name 2nd player : ')
Player_2=input()
speak('So lets start the  game......')
speak(f'{Player_1} please choose your sign between "o" & "x" : ')
p1_sign=input().lower()
if p1_sign=='x' :
    p2_sign='o'
elif  p1_sign=='o':
    p2_sign='x'
else :
    speak('Please choose a sign between "o" and "x" only .')
speak(f"So {Player_1}'s sign = '{p1_sign}' and {Player_2}'s sign = '{p2_sign}' .\n")
p1_count=p2_count=p1_score=p2_score=f=s=0
tte=[[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']]
tte[0][1]=tte[1][1]=tte[2][1]=tte[3][1]=tte[4][1]=tte[0][3]=tte[1][3]=tte[2][3]=tte[3][3]=tte[4][3]='|'
tte[1][0]=tte[1][2]=tte[1][4]=tte[3][0]=tte[3][2]=tte[3][4]='_'


def check(p1_score,p2_score) :
    if tte[0][0]==tte[0][2]==tte[0][4]==p1_sign or tte[2][0]==tte[2][2]==tte[2][4]==p1_sign or tte[4][0]==tte[4][2]==tte[4][4]==p1_sign or tte[0][0]==tte[2][0]==tte[4][0]==p1_sign or tte[0][2]==tte[2][2]==tte[4][2]==p1_sign or tte[0][4]==tte[2][4]==tte[4][4]==p1_sign or  tte[0][0]==tte[2][2]==tte[4][4]==p1_sign or tte[0][4]==tte[2][2]==tte[4][0]==p1_sign :
        p1_score=p1_score+1
        s=1
    elif tte[0][0]==tte[0][2]==tte[0][4]==p2_sign or tte[2][0]==tte[2][2]==tte[2][4]==p2_sign or tte[4][0]==tte[4][2]==tte[4][4]==p2_sign or tte[0][0]==tte[2][0]==tte[4][0]==p2_sign or tte[0][2]==tte[2][2]==tte[4][2]==p2_sign or tte[0][4]==tte[2][4]==tte[4][4]==p2_sign or  tte[0][0]==tte[2][2]==tte[4][4]==p2_sign or tte[0][4]==tte[2][2]==tte[4][0]==p2_sign :
        p2_score=p2_score+1
        s=1
    else :
        s=0
    return s,p1_score,p2_score


def play(p1_count,p2_count,p1_score,p2_score) :
    if p1_count>p2_count :
        speak(f'{Player_2} please choose a loaction between 1 to 9 which is empty : ')
        p2_loc=input()
        print('\n')
        if p2_loc not in ['1','2','3','3','4','5','6','7','8','9'] :
            speak('\n Please enter a loaction between 1 to 9 that is empty !!!\n')
        else :
            disp('p2',p2_loc)
            p2_count=p2_count+1
        if p2_count>=3 :
            s,p1_score,p2_score=check(p1_score,p2_score)
        else :
            s=0
    else :
        speak(f'{Player_1} please choose a loaction between 1 to 9 which is empty : ')
        p1_loc=input()
        print('\n')
        if p1_loc not in ['1','2','3','3','4','5','6','7','8','9'] :
            speak('\n Please enter a loaction between 1 to 9 that is empty !!!\n')
        else :
            disp('p1',p1_loc)
            p1_count=p1_count+1
        if p1_count>=3 :
            s,p1_score,p2_score=check(p1_score,p2_score)
        else :
            s=0
    if ' ' not in tte[0] and ' ' not in tte[1] and ' ' not in tte[2] and ' ' not in tte[3] and ' ' not in tte[4]  :
        f=1
    else :
        f=0
    return p1_count,p2_count,p1_score,p2_score,f,s


def disp(a,b) :
    if a=='p1' :
        if b=='1' and  tte[0][0]==' ' :
            tte[0][0]=p1_sign
        elif b=='2' and  tte[0][2]==' ' :
            tte[0][2]=p1_sign
        elif b=='3' and  tte[0][4]==' ' :
            tte[0][4]=p1_sign
        elif b=='4' and  tte[2][0]==' ' :
            tte[2][0]=p1_sign
        elif b=='5' and  tte[2][2]==' ' :
            tte[2][2]=p1_sign
        elif b=='6' and  tte[2][4]==' ' :
            tte[2][4]=p1_sign
        elif b=='7' and  tte[4][0]==' ' :
            tte[4][0]=p1_sign
        elif b=='8' and  tte[4][2]==' ':
            tte[4][2]=p1_sign
        elif b=='9' and  tte[4][4]==' ' :
            tte[4][4]=p1_sign
        else :
           speak('\n Please enter a loaction between 1 to 9 that is empty !!!!!\n')
    elif a=='p2' :
        if b=='1' and  tte[0][0]==' ' :
            tte[0][0]=p2_sign
        elif b=='2' and  tte[0][2]==' ' :
            tte[0][2]=p2_sign
        elif b=='3' and  tte[0][4]==' ' :
            tte[0][4]=p2_sign
        elif b=='4' and  tte[2][0]==' ' :
            tte[2][0]=p2_sign
        elif b=='5' and  tte[2][2]==' ' :
            tte[2][2]=p2_sign
        elif b=='6' and  tte[2][4]==' ' :
            tte[2][4]=p2_sign
        elif b=='7' and  tte[4][0]==' ' :
            tte[4][0]=p2_sign
        elif b=='8' and  tte[4][2]==' ' :
            tte[4][2]=p2_sign
        elif b=='9' and  tte[4][4]==' ' :
            tte[4][4]=p2_sign
        else :
           speak('\n Please enter a loaction between 1 to 9 that is empty !!!!!\n')
    for i in tte :
        for j in i :
            print(j,end='   ')
        print('\n')


speak('Let Us Play ......\n')
for i in tte :
    for j in i :
        print(j,end='   ')
    print('\n')


while True :
    p1_count,p2_count,p1_score,p2_score,f,s=play(p1_count,p2_count,p1_score,p2_score)
    if f==1 or s==1:
       break
if p1_score>p2_score :
    speak(f'{Player_1} wins......')
elif p2_score>p1_score :
     speak(f'{Player_2} wins......')
else :
    speak('Draw....')
