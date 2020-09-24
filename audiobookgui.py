import kivy
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
import requests
import json
from kivy.core.window import Window
import pyttsx3
import PyPDF2




Window.size = (310,500)
    

class bharathwajan(MDApp):
    
    def read(self):
        print('inside')
        a=self.root.ids.textfield.text
        print(a)
        c=self.root.ids.textfield1.text
        b=int(c)
       
        book=open(a,'rb')
        pdfreader=PyPDF2.PdfFileReader(book)
        total_pages=pdfreader.numPages
        print('total pages ',total_pages)
        
        speaker=pyttsx3.init()
        
        for num in range(b,total_pages):
            page=pdfreader.getPage(num)
            text=page.extractText()
            speaker.say(text)
            speaker.runAndWait()
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette="Yellow"
        
if __name__ == "__main__": 
    bharathwajan().run()
