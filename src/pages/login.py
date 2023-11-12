from gi.repository import Gtk, Adw, GLib

class LoginPage(Gtk.Box):
	def __init__(self, on_login):
		super().__init__(
			orientation = Gtk.Orientation.VERTICAL,
			width_request = 400,
			height_request = 350,
		)
		self.on_login = on_login
		self.last_toast = None

		self.append(Gtk.Box(vexpand = True))

		self.login_box = LoginBox(self.login_submitted)
		self.append(self.login_box)

		login_button = Gtk.Button(
			label="Log In", 
			margin_top=20, 
			width_request=150, 
			height_request=40, 
			css_classes=["pill"],
			hexpand=False, 
			halign=Gtk.Align.CENTER,
		)
		login_button.connect("clicked", self.login_submitted)
		self.append(login_button)

		self.append(Gtk.Box(vexpand = True))

		self.toast_overlay = Adw.ToastOverlay()
		self.append(self.toast_overlay)


	def login_submitted(self, event):
		self.set_toast(Adw.Toast(title = "Logging in..."))
		GLib.timeout_add(1000, self.login_result) # simulate internet latency


	def login_result(self):
		username = self.login_box.username_row.get_text()
		password = self.login_box.password_row.get_text()

		if self.on_login(username, password) == False:
			self.set_toast(Adw.Toast(title = "Wrong username or password"))
		else:
			self.set_toast(Adw.Toast(title = "Logged in!"))


	def set_toast(self, toast):
		if self.last_toast: self.last_toast.dismiss()
		self.last_toast = toast
		self.toast_overlay.add_toast(toast)


class LoginBox(Gtk.ListBox):
	def __init__(self, login_submitted):
		super().__init__(
			width_request = 350,
			css_classes = ["boxed-list"],
			
			halign = Gtk.Align.CENTER,
			valign = Gtk.Align.CENTER,
		)
		self.set_property("selection-mode", Gtk.SelectionMode.NONE)

		self.username_row = Adw.EntryRow(title = "Username")
		self.password_row = Adw.PasswordEntryRow(title = "Password")

		self.username_row.connect("entry-activated", login_submitted)
		self.password_row.connect("entry-activated", login_submitted)

		self.append(self.username_row)
		self.append(self.password_row)
		