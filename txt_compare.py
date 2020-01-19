from tkinter import *
import time

class App():
    def __init__(self, master=None):
        self.widt1 = Frame(master)
        self.widt1.pack()

        self.string1 = Entry(self.widt1)
        self.string1.pack()

        self.widt2  = Frame(master)
        self.widt2.pack()

        self.string2 = Entry(self.widt2)
        self.string2.pack()

        #Div
        self.div = Frame(master)
        self.div.pack()

        self.tDiv = Label(self.div,text='')
        self.tDiv.pack()
        #Div

        self.widt4  = Frame(master)
        self.widt4.pack()

        self.compare = Button(self.widt4)
        self.compare['text']    = "Compare"
        self.compare['width']   = 10
        self.compare['height']  = 2
        self.compare['command'] = self.comp
        self.compare.pack()

        self.widt3 = Frame(master)
        self.widt3.pack(side=BOTTOM)

        self.log = Label(self.widt3, text='Insert some texts for comparison')
        self.log['width'] = 90
        self.log['bg']      = 'bisque'
        self.log.pack()
    
    def comp(self):
        str1 = self.string1.get()
        str2 = self.string2.get()
        if str1 == '' and str2 == '':
            self.log['text'] = 'Empty'
        else:
            if str1 == str2:
                self.log['text'] = 'OK'
                self.log['bg']      = 'green'
            else:
                self.log['text'] = 'Not equal'
                self.log['bg']      = 'red'

window = Tk()
App(window)
window.title('Text Compare')
window.geometry('300x300')
window.resizable(width =FALSE , height=FALSE)
window.mainloop()