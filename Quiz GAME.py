import tkinter
from tkinter import *
import random

questions = [
    "Which is the capital of india.",
    "How many vowel in alphabet.",
    "Who is the Prime Minister of India.",
    "Who is the Cheif Minister of Uttar Pradesh. ",
    "The Taj Mahal is located in ?",
    "Who is called the ship of the desert?",
    "How many articles are there in the Indian Constitution ?",
    "Who is the first Prime Minister of India ?",
    "Who wrote the constitution of India ?",
    "Who is known as Iron Man of India ?",
]

answer_choice=[
    ["Uttar Pradesh","Delhi","Karnataka","Bangluru",],
    ["5","4","3","8",],
    ["Dr. Manmohan Singh","Indira Gandhi","Rahul Gandhi","Narendra Modi",],
    ["Chandra Shekhar Ajad","Mayavati","Yogi Aditya Nath","Akhiesh Yadav",],
    ["America","China","India","Pakistan",],
    ["Goat","Camel","Deer","Beer",],
    ["470","449","370","455",],
    ["Sardar Balabh Bhai Patel","Dr. Bheem Rao Ambedkar","Pt. Jawahar Lal Nehru","Dr. Rajendra Prasad",],
    ["Sardar Balabh Bhai Patel","Dr. Bheem Rao Ambedkar","Pt. Jawahar Lal Nehru","Dr. Rajendra Prasad",],
    ["Sardar Balabh Bhai Patel","Dr. Bheem Rao Ambedkar","Pt. Jawahar Lal Nehru","Dr. Rajendra Prasad",],
    
]

answer=[1,0,3,2,2,1,0,2,1,0]

user_answer=[]

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x= random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage=Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50,30))

    labelresulttext= Label(
        root,
        font = ("Consolas",20),
        background="#ffffff"
    )
    labelresulttext.pack()
    if score >= 25:
        img = PhotoImage(file="d:\great.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You Are Excelent!!")
    elif score >= 10 and score < 25:
        img = PhotoImage(file="d:\satisfy.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You can  be better !!")
    else:
        img = PhotoImage(file="d:\png-clipart-sad-emoji-illustration-emoji-smiley-sadness-emoticon-happy-sad-face-sticker-thumbnail.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You should work hard !!")



def calc():
    global indexes,user_answer,answer
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answer[i]:
            score=score + 5
        x += 1
    print(score)
    showresult(score)

que=1

def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global que
    x =radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if que < 5:
        lblQuestion.config(text=questions[indexes[que]])
        r1['text']= answer_choice[indexes[que]][0]
        r2['text']= answer_choice[indexes[que]][1]
        r3['text']= answer_choice[indexes[que]][2]
        r4['text']= answer_choice[indexes[que]][3]
        que += 1
    else:
        print(indexes)
        print(user_answer)
        calc()

# def selected():
#     global radiovar
#     x = radiovar.get()
#     print(x)


def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text=questions[0],
        font=("Consolas",16),
        width =500,
        justify= "center",
        wraplength=400,
        background="#ffffff"
        )
    lblQuestion.pack(pady=(100,30))
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answer_choice[indexes[0]][0],
        font=("Times",12),
        value=0,
        variable=radiovar,
        command=selected,background="#ffffff"

    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answer_choice[indexes[0]][1],
        font=("Times",12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r2.pack(pady=5)
    r3 = Radiobutton(
        root,
        text=answer_choice[indexes[0]][2],
        font=("Times",12),
        value=2,
        variable=radiovar,
        command=selected,background="#ffffff"
    )
    r3.pack(pady=5)


    r4 = Radiobutton(
        root,
        text=answer_choice[indexes[0]][3],
        font=("Times",12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r4.pack(pady=5)


def startIspressed():

    labeltext.destroy()
    labelimage.destroy()
    lblinstrucion.destroy()
    lblrules.destroy()
    btnstart.destroy()
    gen()
    startquiz()

root = tkinter.Tk()
root.title("QuizGame")
root.geometry("700x690")
root.config(background="#ffffff")
# root.resizable(0,0)

img1 = PhotoImage(file = "D:/download (1).png")
labelimage = Label(
    root,
    image = img1,
    background="#ffffff"
)
labelimage.pack()

labeltext=Label(
    root,
    text="Quiz GAME",
    font=("Cosmic sans MS",24,"bold"),
    background="#ffffff"
)
labeltext.pack(pady=(0,40))

img2=PhotoImage(file="d:\download (4).png")
btnstart=Button(
    root,
    image = img2,
    relief=FLAT,
    background="#ffffff",


    # background="#ffffff",
    border=0,
    command=startIspressed,
)
btnstart.pack()

lblinstrucion=Label(
    text="Read the Rules and \nClick start Once ypou Are Ready",
    background="#ffffff",
    font=("Consoas",14),
    justify="center",


)
lblinstrucion.pack(pady=(1,90))

lblrules=Label(
    root,
    text="This quiz Contains 10 quetions \nYou will get 20 seconds to solve a question \n Once you will be a final choice \n hence think before you select\nCick Start Once you are ready",
    width=150,
    font=("Times",14),
    background="#000000",
    foreground="#FACA2F",

)
lblrules.pack()
root.mainloop()
