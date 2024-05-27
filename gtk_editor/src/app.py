from .window import MainWindow
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Adw, Gio  # noqa


class MyApp(Adw.Application):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
        self.connect('open', self.on_open)
        # need to tell GApplication we can handle this
        self.set_flags(Gio.ApplicationFlags.HANDLES_OPEN)
        self.win = None

    def on_activate(self, app):
        # check if application has been launched already
        if not self.win:
            self.win = MainWindow(application=app)
        self.win.present()

    def on_open(self, app, files, n_files, hint):
        # adding this because window may have not been created with this entry point
        self.on_activate(app)
        for file in files:
            print("File to open: " + file.get_path())
