#!/usr/bin/python3

import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk, GLib

from pages.login import LoginPage
from pages.home import HomePage
from users import users


class TornadoMainWindow(Adw.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Things will go here
        self.username = None

        self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)

        self.box.append(Adw.HeaderBar())
        self.content_bin = Adw.Bin()
        self.box.append(self.content_bin)

        self.set_content(self.box)
        self.set_default_size(500, 500)

        self.set_page("login")

    def on_login(self, username, password):
        if username in users and users[username] == password:
            self.username = username
            GLib.timeout_add(500, lambda : self.set_page("home"))
            return True
        else:
            return False

    def on_logout(self):
        self.username = None
        self.set_page("login")

    def set_page(self, page):
        if page == "login":
            self.content_bin.set_child(LoginPage(on_login = self.on_login))

        if page == "home":
            self.content_bin.set_child(HomePage(username = self.username, on_logout = self.on_logout))


class TornadoApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        style_provider = Gtk.CssProvider()
        css = "row > box > image { opacity: 0; } .card-color { background-color: @card_bg_color; } .thin { font-weight: normal; }"
        style_provider.load_from_data(css, len(css))

        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.win = TornadoMainWindow(application=app)
        self.win.present()
        self.win.set_title("Tornado")


app = TornadoApp(application_id="dev.candar.hakan.Tornado")
app.run(sys.argv)
