from tkinter import *
window=Tk()
window.geometry("500x600")
window.config(bg="white")
label=Label(window,text='Mood Tracker',font=("ink free",30))
label.config(fg="#996633",bg="white")
image=PhotoImage(file="yellow stars.png")
label.config(image=image,compound="left")
label.pack()
moods=["Happy","Sad","Angry","Nothing"]
happy=PhotoImage(file="happy.png")
sad=PhotoImage(file="sad.png")
angry=PhotoImage(file="angry.png")
nothing=PhotoImage(file="idk.png")
moodimages=[happy,sad,angry,nothing]
x=IntVar()
for index in range(len(moods)):
    radiobutton=Radiobutton(window,text=moods[index] #adds text to radio button
                            ,variable=x, #groups radiobutton together if they share the same variable
                            value=index, #assigns each radiobutton a different value
                            bg="white",
                            image=moodimages[index], #adds image
                            compound="left") 
    radiobutton.config(font=("ink free",20))
    radiobutton.config(padx=50)
    radiobutton.pack(anchor="w")
window.mainloop()
