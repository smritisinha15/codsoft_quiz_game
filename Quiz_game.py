#-----------------------CODSOFT (INTERNSHIP ..... PYTHON PROGRAMMING)-------------------------------------

# NAME - SMRITI SAROJ SINHA
# COLLEGE - CENTRAL UNIVERSITY OF HARYANA

#---------------------------QUIZ GAME---------------------------------------------------------


#IMPORTING MODULES
from tkinter import *
import random

# FUNCTION FOR THE NEXT QUESTION TO BE DISPLAYED IN THE QUIZ TEMPELATE
def next(event):
    b = event.widget
    value =  b['text']
    # print(value)

    for i in range (10):
        if value == correct_answer[i]:
            if value == correct_answer[9]:
                def close(): # FUNCTION FOR CLOSING THE WINDOW 
                    rootb.destroy()
                    root.destroy()

                def playagain(): # FUNCTION FOR ATTEMPTING THE QUIZ AGIAN
                    rootb.destroy()
                    quesnumberarea.delete(1.0 , END)
                    quesarea.delete(1.0,END)
                    quesnumberarea.insert(END , s[0])
                    quesarea.insert(END, questions[0])
                    optionbuttonA.config(text=optionA[0]) 
                    optionbuttonB.config(text=optionB[0])
                    optionbuttonC.config(text=optionC[0])
                    optionbuttonD.config(text=optionD[0])
                    score.config(image=scoreimage0)

                rootb = Toplevel() # NEW GUI WINDOW TO DISPLAY THE THE WIN STATEMENT TO THE USER AND TO CHOSE THE 
                                   # OPTIONS TO PLAY AGAIN OR TO CLOSE THE WINDOW
                rootb.overrideredirect(True) # TO REMOVE THE TITLE BAR FROM THE NEW WINDOW
                rootb.config(bg='black')
                rootb.geometry('500x500+140+30')
                rootb.title('result')
                imglabel = Label(rootb, image= image1 , bd = 0)
                imglabel.pack()

                winlabel = Label(rootb , text='You Won' , font = ('Times New Roman' , 40 , 'bold') , bg='black' , fg='white')
                winlabel.pack()

                playagainbutton = Button(rootb , text='Play Again' , font=('Times New Roman' , 20 , 'bold'), bg = 'black' , fg = 'white' , 
                                        activebackground='black' , activeforeground='white' , bd = 0 , cursor='hand2',
                                        command=playagain)
                playagainbutton.pack()

                closebutton = Button(rootb , text='Close' , font=('Times New Roman' , 20 , 'bold'), bg = 'black' , fg = 'white' , 
                                        activebackground='black' , activeforeground='white' , bd = 0 , cursor='hand2' ,
                                        command=close)
                closebutton.pack()

            quesnumberarea.delete(1.0 , END)
            quesarea.delete(1.0,END)
            quesnumberarea.insert(END , s[i+1])
            quesarea.insert(END, questions[i+1])
            optionbuttonA.config(text=optionA[i+1])
            optionbuttonB.config(text=optionB[i+1])
            optionbuttonC.config(text=optionC[i+1])
            optionbuttonD.config(text=optionD[i+1])
            score.config(image=scoreimages[i])
            break
        
    else:
        def close(): # FUNCTION TO CLOSE THE ENTIRE WINDOW 
            roota.destroy()
            root.destroy()

        def tryagain(): # FUNCTION TO DISPLAY THE TRY AGAIN OPTION SO THAT USER CAN ATTEMPT THE QUIZ AGAIN
            roota.destroy()
            quesnumberarea.delete(1.0 , END)
            quesarea.delete(1.0,END)
            quesnumberarea.insert(END , s[0])
            quesarea.insert(END, questions[0])
            optionbuttonA.config(text=optionA[0])
            optionbuttonB.config(text=optionB[0])
            optionbuttonC.config(text=optionC[0])
            optionbuttonD.config(text=optionD[0])
            score.config(image=scoreimage0)

        roota = Toplevel() #NEW GUI WINDOW TO DISPLAY LOSE STATEMENT
        roota.overrideredirect(True)
        roota.config(bg='black')
        roota.geometry('500x500+140+30')
        roota.title('result')
        imglabel = Label(roota, image= image1 , bd = 0)
        imglabel.pack()

        loselabel = Label(roota , text='You Lose' , font = ('Times New Roman' , 40 , 'bold') , bg='black' , fg='white')
        loselabel.pack()

        tryagainbutton = Button(roota , text='Try Again' , font=('Times New Roman' , 20 , 'bold'), bg = 'black' , fg = 'white' , 
                                activebackground='black' , activeforeground='white' , bd = 0 , cursor='hand2',
                                command=tryagain)
        tryagainbutton.pack()

        closebutton = Button(roota , text='Close' , font=('Times New Roman' , 20 , 'bold'), bg = 'black' , fg = 'white' , 
                                activebackground='black' , activeforeground='white' , bd = 0 , cursor='hand2' ,
                                command=close)
        closebutton.pack()

        roota.mainloop()
        
# LIST FOR CORRECT ANSWERS OF THE QUESTIONS IN THE QUIZ
correct_answer = ["Application software","modifier","Central statistical organisation","Milk and its products",
                  "Odisha","Ocean depth","Operating system","Lime","wrought iron","centrifugation",]

# LIST OF THE QUESTIONS TO BE DISPLAYED IN THE QUIZ
questions = ["MS-Word is an example of _____","Ctrl, Shift and Alt are called .......... keys.",
             "National Income estimates in India are prepared by","The staple food of the Vedic Aryan was",
             "The tropic of cancer does not pass through which of these Indian states ?",
             "Fathometer is used to measure","A computer cannot \"boot\" if it does not have the _____",
             "What color does yellow and green make?","The purest form of iron is",
             "The working principle of a washing machine is" , "  "]

# LIST OF OPTIONS 'A' OF THE QUESTIONS
optionA = ["An operating system","modifier","Planning Commission","Barley and rice","Madhya Pradesh",
           "Earthquakes","Compiler","Lime","wrought iron","reverse osmosis", "  "]

# LIST OF OPTIONS 'B' OF THE QUESTIONS
optionB = ["A processing device","function","Reserve Bank of India","Milk and its products","West Bengal",
           "Rainfall","Loader","Ocean mist","steel","diffusion" , "  "]

# LIST OF OPTIONS 'C' OF THE QUESTIONS
optionC = ["Application software","alphanumeric","Central statistical organisation","Rice and pulses",
           "Rajasthan","Ocean depth","Operating system","Maroon","pig iron","centrifugation" , "  "]

# LIST OF OPTIONS 'D' OF THE QUESTIONS
optionD = ["An input device","adjustment","Indian statistical Institute","Vegetables and fruits","Odisha",
           "Sound intensity","Assembler","Tangerine","nickel steel","dialysis" , "  "]

# LIST OF SERIAL OF THE QUESTIONS
s = [ 'Q - i' , 'Q - ii' , 'Q - iii' , 'Q - iv' , 'Q - v' , 'Q - vi' , 'Q - vii' , 'Q - viii' , 'Q - ix' , 
     'Q - x' , '  ']

root = Tk() # THE MAIN GUI WINDOW
root.geometry('1370x7400+0+0')
root.title('Sqeezzzyyy....Quizzzyyy....')

# IMAGES USED THE PROGRAM
image1 = PhotoImage(file='C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\image(quiz).png')
image2 = PhotoImage(file = 'C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\quiztemp.png')
scoreimage0 = PhotoImage(file='C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\score 0.png')
scoreimage1 = PhotoImage(file ='C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\score 1.png')
scoreimage2 = PhotoImage(file= 'C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\score 2.png')
scoreimage3 = PhotoImage(file= 'C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\score 3.png')
scoreimage4 = PhotoImage(file= 'C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\score 4.png')
scoreimage5 = PhotoImage(file= 'C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\score 5.png')
scoreimage6 = PhotoImage(file= 'C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\score 6.png')
scoreimage7 = PhotoImage(file= 'C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\score 7.png')
scoreimage8 = PhotoImage(file= 'C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\score 8.png')
scoreimage9 = PhotoImage(file= 'C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\score 9.png')
scoreimage10 = PhotoImage(file= 'C:\\Users\\DELL\\OneDrive\\Desktop\\projects(codsoft)\\score 10.png')

# LIST OF SCORES FOR EACH QUESTIONS
scoreimages = [ scoreimage1 ,scoreimage2 ,scoreimage3 ,scoreimage4 ,scoreimage5 ,
               scoreimage6 ,scoreimage7, scoreimage8 ,scoreimage9 ,scoreimage10   ]

root.config(bg='black')

leftframe = Frame(root , bg='black' , padx=120 , pady= 50 )
leftframe.grid(row = 0 , column = 0)

upperframe = Frame(leftframe)
upperframe.grid(row=0 , column=0)

bottomframe = Frame(leftframe , bg='black')
bottomframe.grid(row=1 , column=0)

rightframe =  Frame(root , bg='black')
rightframe.grid(row=0 , column=1)

quizlabel = Label(upperframe, image = image1 , bd=0 ,bg='black' , activeforeground='black' )
quizlabel.grid()

score = Label(bottomframe , image= scoreimage0 , bg='black', fg='white' ,
             activeforeground='black' , bd=0)
score.grid()

quiztemp = Label (rightframe , image = image2 , bd=0 ,bg='black' , activebackground='black' )
quiztemp.grid()

quesarea = Text(rightframe , font=('Comic Sans MS' , 10 , 'bold'), width= 50 , height=1.5 , bg= '#bcbefa',bd=0 ,
                wrap='word' )
quesarea.place(x=70 , y=130)

quesnumberarea = Text(rightframe , font=('Comic Sans MS' , 12 , 'bold'), width= 6 , height=2 , bg= '#bcbefa',bd=0 ,
                wrap='word' )
quesnumberarea.place(x=220 , y=70)
quesnumberarea.insert(END , s[0])

quesarea.insert(END , questions[0])
optionbuttonA = Button(rightframe , text=optionA[0] , bg='#c1ff72', bd=0, activebackground='#c1ff72' ,
                       font=('Comic Sans MS' , 10, 'bold') , cursor='hand2' )
optionbuttonB = Button(rightframe , text=optionB[0] , bg='#c1ff72', bd=0, activebackground='#c1ff72' ,
                       font=('Comic Sans MS' , 10, 'bold') , cursor='hand2' )
optionbuttonC = Button(rightframe , text=optionC[0] , bg='#c1ff72', bd=0, activebackground='#c1ff72' ,
                       font=('Comic Sans MS' , 10, 'bold') , cursor='hand2' )
optionbuttonD = Button(rightframe , text=optionD[0] , bg='#c1ff72', bd=0, activebackground='#c1ff72' ,
                       font=('Comic Sans MS' , 10, 'bold') , cursor='hand2' )
    
optionbuttonA.place(x=38 , y=244)
optionbuttonB.place(x=290 , y=244)
optionbuttonC.place(x=38 , y=350)
optionbuttonD.place(x=290 , y=350)

optionbuttonA.bind('<Button-1>' , next)
optionbuttonB.bind('<Button-1>' , next)
optionbuttonC.bind('<Button-1>' , next)
optionbuttonD.bind('<Button-1>' , next)

root.mainloop()