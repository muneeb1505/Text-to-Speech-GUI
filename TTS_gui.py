from tkinter import*
import pyttsx3
root  = Tk()
root.title("First code")
root.geometry("250x400")
root.configure(bg="black")

def speak():
   engine = pyttsx3.init()
   engine.say(entry.get())
   engine.runAndWait()
   entry.delete(0,END)

entry = Entry(root,font=("Arial",12))
entry.pack(pady=50)
button = Button(text="Speak up",
                width=14,
                height=2,
                bg="Green",
                fg="White",
                activebackground="Red",
                activeforeground="White",
                command=speak
                )
button.pack(pady=25,padx=10)
root.mainloop()
