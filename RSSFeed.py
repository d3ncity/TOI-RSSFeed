# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:37:56 2020

@author: 01uni
"""

import feedparser
from tkinter import *
import tkinter as t

window = t.Tk()
window.title("TOI NewsFeed")

canvas = t.Canvas(window, height=400, width=700, bg="#C96567")
canvas.pack()     

frame = t.Frame(window, bg="#ADD8E6") 
frame.place(relwidth=0.8,relheight=0.8, relx=0.1, rely=0.1)     
      
content = t.Text(frame, bg="#ADD8E6", height=400, width=700)

NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")

print ('Number of RSS posts :', len(NewsFeed.entries))
print("--Displayed on Window--")

i=0
while(i<len(NewsFeed.entries)):
    content.insert(t.INSERT, "Story "+str(i+1)+": \n")
    content.insert(t.INSERT, NewsFeed.entries[i].title+"\n")
    content.insert(t.INSERT, NewsFeed.entries[i].summary+"\n")
    content.insert(t.INSERT, NewsFeed.entries[i].published+"\n")
    content.insert(t.INSERT, NewsFeed.entries[i].link+"\n\n\n\n")
    i+=1 

content.config(state="disabled")
content.pack()
window.mainloop()