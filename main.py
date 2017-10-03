from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty


class HelpAboutPopup(Popup):
    pass

class FileLoadFilePopup(Popup):
    pass

class ProtoPAP(BoxLayout):
    txtOutput = ObjectProperty(None)
    txtFileName = StringProperty("No File")

    def clear(self):
        self.txtOutput.text = ""
        self.txtOutput.text = "The end is near, there is no help for the wicked"

    def helpaboutpop(self, *args):
        HelpAboutPopup().open()

    def fileloadpop(self, *args):
        print("txtFileName before=" + self.txtFileName + "\n" )
        FileLoadFilePopup().open()
        print("txtFileName after=" + self.txtFileName + "\n")

class ProtopapApp(App):
    def build(self):
        return ProtoPAP()


if __name__ == '__main__':
    ProtopapApp().run()