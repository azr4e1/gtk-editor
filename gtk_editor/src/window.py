import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw  # noqa

# css_provider = Gtk.CssProvider()
# css_provider.load_from_path("style.css")
# Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(
# ), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(640, 480)
        self.set_title('gtk-editor')

        self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.set_child(self.box)
        self.set_editor()
        self.set_buttons()

        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        self.set_headerbar()

    def set_headerbar(self):
        menu = Gio.Menu.new()
        popover = Gtk.PopoverMenu()
        popover.set_menu_model(menu)
        hamburger = Gtk.MenuButton()
        hamburger.set_popover(popover)
        hamburger.set_icon_name("open-menu-symbolic")

        self.header.pack_end(hamburger)

        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.show_about)
        self.add_action(action)

        menu.append("About", "win.about")

    def set_editor(self):
        scrolledWindow = Gtk.ScrolledWindow()
        scrolledWindow.set_vexpand(True)
        scrolledWindow.set_hexpand(True)
        scrolledWindow.set_margin_start(5)
        scrolledWindow.set_margin_end(5)
        self.box.append(scrolledWindow)

        self.text_view = Gtk.TextView()

        self.text_buffer = self.text_view.get_buffer()
        self.text_buffer.set_text("Hello World!")

        scrolledWindow.set_child(self.text_view)

    def set_buttons(self):
        pass

    def show_about(self, action, param):
        dialog = Adw.AboutWindow(transient_for=self)
        dialog.set_application_name("gtk-editor")
        dialog.set_version("0.1")
        dialog.set_developer_name("azr4e1")
        dialog.set_license_type(Gtk.License(Gtk.License.GPL_3_0))
        dialog.set_comments("Simple demo app in GTK4 and LibAdwaita")
        dialog.set_website("https://github.com/azr4e1/gtk-editor")
        dialog.set_issue_url(
            "https://github.com/azr4e1/gtk-editor/issues")
        dialog.set_copyright("© 2022 azr4e1")
        dialog.set_developers(["azr4e1"])

        dialog.set_visible(True)
