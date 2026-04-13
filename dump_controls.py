import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib
def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    header = Gtk.HeaderBar()
    win.set_titlebar(header)
    def print_tree(widget, indent):
        print("  " * indent + widget.get_name() + ", classes: " + str(widget.get_css_classes()))
        for child in widget:
            print_tree(child, indent + 1)
    
    # We must show it to generate the internal widgets
    win.present()
    
    GLib.idle_add(lambda: print_tree(header, 0) or app.quit())
app = Gtk.Application()
app.connect('activate', on_activate)
app.run(None)
