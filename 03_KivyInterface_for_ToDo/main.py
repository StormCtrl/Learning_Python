#modules needed for this program
import os
from kivy.app import App
from kivy.uix.button import Button

#Kivy Code to create the Primary interface
class ToDoApp(App):
    def build(self):
        return Button(text="Hello!",
                      background_color=(0,0,0,1),
                      font_size = 150)

#This launches the App
if __name__ == "__main__":
    ToDoApp().run()
