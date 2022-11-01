from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
import socket


class MyBoxLayout(BoxLayout):
                        


    def turn_left(self):
        currentAngle = int(self.ids.angles.text)
        if currentAngle > 0:
            currentAngle = currentAngle - 1
        elif currentAngle == 0:
            currentAngle = 359
        self.ids.angles.text=str(currentAngle)
        self.degrees = self.degrees + 1
        s = socket.socket()
        s.connect(('127.0.0.1', 3333))
        data = "went left"
        s.send(data.encode())
        dataFromServer = s.recv(1024)
        print(dataFromServer.decode())
        s.close()

    def turn_right(self):
        currentAngle = int(self.ids.angles.text)
        if currentAngle < 359:
            currentAngle = currentAngle + 1
        elif currentAngle == 359:
            currentAngle = 0
        self.ids.angles.text=str(currentAngle)
        self.degrees = self.degrees - 1
        s = socket.socket()
        s.connect(('127.0.0.1', 3333))
        data = "went right"
        s.send(data.encode())
        dataFromServer = s.recv(1024)
        print(dataFromServer.decode())
        s.close()

Builder.load_string('''

<MyBoxLayout>:
    degrees: 90
    BoxLayout:
        orientation: "vertical"

        Label:
            id: arrow
            text: "---->"
            font_size: 40
            canvas.before:
                PushMatrix
                Rotate:
                    angle: root.degrees
                    origin: self.center
            canvas.after:
                PopMatrix

        Label:
            id: angles
            text: "0"
            font_size: 30

        
        
        BoxLayout:
            orientation: "horizontal"

            Button:
                text: "<----"
                font_size: 35
                on_press: root.turn_left()
            Button:
                text: "---->"
                font_size: 35
                on_press: root.turn_right()

''')


class RotorApp(App):
    def build(self):
        return MyBoxLayout()


if __name__=="__main__":
    RotorApp().run()