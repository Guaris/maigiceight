import random
import tkinter as tk

class Magic8:
    def __init__(self):
        self.answers = [
            "It is certain.",
            "It is decidedly so",
            "without a doubt",
            "Yes - definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most Likely.",
            "Outlook good",
            "Yes",
            "Signs Point to Yes",
            "Reply hazy, Try Again",
            "Ask Again Later.",
            "Better not tell you now",
            "Cannot predict Now",
            "Concentrate and ask again",
            "Dount Count on it",
            "My Reply is no",
            "My Sources say no",
            "Outlook not so good",
            "Very Doubtful"
        ]


    def readfuture(self):
        choice = random.randint(1,20)
        return (self.answers[choice])

    def askquestion(self,S):
        print('The Eightball Says:{}'.format(self.readfuture()))


class Window(tk.Frame):

    def __init__(self, m, master=None):
        super().__init__(master)
        self.eightball = m
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self)
        self.button["text"] = self.eightball.readfuture()
        self.button.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")





root = tk.Tk()
app = Window(Magic8(),master=root)
app.mainloop()

