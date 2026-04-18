import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def dump_node(widget, depth=0):
    css_name = widget.get_css_name()
    classes = widget.get_css_classes()
    print("  " * depth + f"{css_name} classes={classes}")
    
    child = widget.get_first_child()
    while child:
        dump_node(child, depth+1)
        child = child.get_next_sibling()

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    hb = Gtk.HeaderBar()
    win.set_titlebar(hb)
    dump_node(hb)
    app.quit()

app = Gtk.Application(application_id='org.test.Dump')
app.connect('activate', on_activate)
app.run(None)
