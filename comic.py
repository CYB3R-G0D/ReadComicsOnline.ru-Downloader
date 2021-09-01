#Import tkinter library
from tkinter import *
from comickaze import Comickaze, Converter

c = Comickaze(log_level="VERBOSE")

#Create an instance of tkinter window or frame
win=Tk()
win.geometry("500x250")
win.title("ReadComicsOnline.ru-Downloader")

def get_input():
   value=my_text_box.get("1.0","end-1c")
   output=my_text_out.get("1.0","end-1c")
   format=my_text_for.get("1.0","end-1c")
   comic = c.get_comic(value)
   download_dir = output
   output_format = Converter.CBZ
   multithreaded_downloader = c.create_downloader(comic.chapters, number_of_threads=8, output_format=output_format)
   multithreaded_downloader.start(download_dir)

my_labe3 = Label(win, text = "")
my_labe3.pack()

my_label = Label(win, text = "Enter the comic url below")
my_label.pack()

#Creating a text box widget
my_text_box=Text(win, height=1, width=40)
my_text_box.pack()

my_labe3 = Label(win, text = "")
my_labe3.pack()

my_labe2 = Label(win, text = "Enter format <supported: CBZ,PDF,IMG> Please in all caps")
my_labe2.pack()

my_text_for=Text(win, height=1, width=40)
my_text_for.pack()

my_labe3 = Label(win, text = "")
my_labe3.pack()

my_labe4 = Label(win, text = "Output folder name")
my_labe4.pack()

my_text_out=Text(win, height=1, width=40)
my_text_out.pack()

my_labe3 = Label(win, text = "")
my_labe3.pack()

#Create a button for Comment
comment= Button(win, height=1, width=10, text="Download", command=lambda: get_input())

#command=get_input() will wait for the key to press and displays the entered text
comment.pack()

my_labe3 = Label(win, text = "")
my_labe3.pack()

win.mainloop()