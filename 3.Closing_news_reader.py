#Step.3
#What i'm gonna make
#Take(-> Request) and treat(-> Response & Use) infos from outside(outter space? environment?)
#What should I use? Libraries(Bunch of Modules)?
#EX. Music Recommendation Program etc...
#English word book? Dictionary program?
#Okay, then. Let's Do this. From Scratch.
#First. Googling!

#Cambridge Uni Dictionary URL (Below)
#https://dictionary.cambridge.org/ko/%EC%82%AC%EC%A0%84/ ** This url doesn't allow to approach.(Remote end closed connection without response Error)
#I need urllib.

#import urllib.request

#url = 'https://naver.com'
#def req(url):
#    res = urllib.request.urlopen(url)
#    byte_data = res.read()
#    text_data = byte_data.decode('utf-8')
#    return text_data

#webpage=req(url)
#print(webpage)
import os
import time

print(os.getcwd())

from selenium import webdriver

cpath = r'C:\Users\gram\anaconda3\envs\py_seung_env\chromedriver_win32\chromedriver_win32.exe'
driver = webdriver.Chrome(cpath)