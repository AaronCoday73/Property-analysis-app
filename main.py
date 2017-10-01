from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty



class ProtoPAP(BoxLayout):
    txtOutput = ObjectProperty(None)

    def clear(self):
        self.txtOutput.text = ""
        self.txtOutput.text = "The end is near, there is no help for the wicked"



class ProtopapApp(App):
    def build(self):
        return ProtoPAP()


if __name__ == '__main__':
    ProtopapApp().run()