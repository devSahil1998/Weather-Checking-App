from tkinter import *
from tkinter import ttk, messagebox
import requests
from PIL import Image,ImageTk

def button(x):
    if x==1:
        global weather_stats
        parameters={
        'q':weather_stats.entry1.get(),
        'APPID':'d1953869045846fa51e77dcda55a6df2'}
        try:
            weburl=requests.get('http://api.openweathermap.org/data/2.5/forecast',  params=parameters).json()
            print(weburl)
            messagebox.showinfo(title='Statistics', message="{} : {}".format(weburl['list'][0]['weather'][0]['main'],weburl['list'][0]['weather'][0]['description']))
        except:
            messagebox.showerror(title='ERROR', message='An Error Occurred Please Try Again Later')

    elif x==2:
        parameters = {
        'q': weather_stats.entry1.get(),
        'APPID': 'd1953869045846fa51e77dcda55a6df2'}
        try:
            weburl = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=parameters).json()
            messagebox.showinfo(title='Statistics',message="wind speed -> {}".format(weburl['list'][0]['wind']['speed']))
        except:
            messagebox.showerror(title='ERROR',message='An Error Occurred Please Try Again Later')

    elif x==3:
        parameters = {
        'q': weather_stats.entry1.get(),
        'APPID': 'd1953869045846fa51e77dcda55a6df2'}
        try:
             weburl = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=parameters).json()
             messagebox.showinfo(title='Statistics', message="temperature -> {} , Humidity-> {} ".format(((weburl['list'][0]['main']['temp']) - 273.15), weburl['list'][0]['main']['humidity']))
        except:
            messagebox.showerror(title='ERROR', message='An Error Occurred Please Try Again Later')

class weather_statistics:
    def __init__(self, master):
        self.master=master
        self.style=ttk.Style()
        self.style.configure('TFrame', background='#ff8c18')
        self.style.configure('TLabel', background='#ff8c18')
        self.style.configure('TEntry', background='#ff8c18')
        self.style.configure('TButton', background='#ff8c18')
        self.frame1=ttk.Frame(self.master)
        self.frame2=ttk.Frame(self.master)
        self.frame1.pack(); self.frame2.pack()
        img=Image.open("logo1.jpg")
        img = img.resize((290, 100), Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(img)
        self.label1=ttk.Label(self.frame1,  image=self.img, background='black')
        self.label2=ttk.Label(self.frame2,  text='Enter City Name :',  font=('arial', 10, 'bold italic'))
        self.entry1=ttk.Entry(self.frame2,  width='15')
        self.button1 = ttk.Button(self.frame2, text='Check Rain', command= lambda : button(1))
        self.button2 = ttk.Button(self.frame2, text='Check Wind', command= lambda : button(2))
        self.button3 = ttk.Button(self.frame2, text='Check Temperature', command= lambda : button(3))
        self.label1.grid(rowspan=2, columnspan=2)
        self.label2.grid(row=0, column=0,  padx=20,  pady=20)
        self.entry1.grid(row=0,  column=1,  padx=20,  pady=20)
        self.button1.grid(row=1, column=0  , pady=20, sticky='w')
        self.button2.grid(row=1, column=0 , pady=20, sticky='e')
        self.button3.grid(row=1, column=1 , pady=20, sticky='w' )
 
root=Tk()
root.title('Weather Statistics')
root.configure(background='#ff8c18')
root.resizable(False, False)
root.geometry('300x220')
weather_stats=weather_statistics(root)
root.mainloop()