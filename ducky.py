import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ducky(Gtk.Window):
    def __init__(self):
        super().__init__(title="Ducky")
        eventbox = Gtk.EventBox()        
        self.add(eventbox)
        image = Gtk.Image()
        image.set_from_file("ducky.png")        
        eventbox.add(image)

window = ducky()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()