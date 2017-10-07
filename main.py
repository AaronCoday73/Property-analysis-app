from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
import os

class HelpAboutPopup(Popup):
    pass

class FileLoadFilePopup(Popup):

    def selected(self, filename):
        print("select: %s" % filename[0])

    def open_file(self, path, filename):
       #print("path:" + path + "filename:" +filename)
        with open(os.path.join(path, filename[0])) as f:
            print(f.read())

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