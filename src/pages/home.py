from gi.repository import Gtk, Adw, GLib

class HomePage(Gtk.Box):
	def __init__(self, username, on_logout):
		super().__init__(
			orientation = Gtk.Orientation.HORIZONTAL,
			width_request = 750,
			height_request = 420,
			css_classes=["view"]
		)

		self.append(SidePane(username, on_logout))
		self.append(Gtk.Separator())
		
		box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		box.append(Gtk.Box(hexpand=True))
		box.append(Gtk.Image(icon_name="emoji-nature-symbolic", pixel_size=75))
		box.append(Gtk.Box(hexpand=True))

		self.append(box)




class SidePane(Gtk.Box):
	def __init__(self, username, on_logout):
		super().__init__(
			vexpand = True,
			width_request = 220,
			orientation = Gtk.Orientation.VERTICAL,
			css_classes=["background"]
		)

		box = Gtk.Box(height_request=80)
		
		box.append(Adw.Avatar(size=50, margin_start=15))
		box.append(Gtk.Label(label = username, margin_start=20))

		self.append(box)
		
		self.append(Gtk.Separator(margin_start=7, margin_end=7))
		
		mock_button = Gtk.Button(
			css_classes = ["flat"], 
			margin_bottom = 7, 
			margin_end = 7, 
			margin_start = 7, 
			margin_top = 7,
			child = Adw.ButtonContent(icon_name = "mail-unread-symbolic", label = "Messages"),
			can_focus=False
		)

		self.append(mock_button)

		self.append(Gtk.Box(vexpand=True))
		self.append(Gtk.Separator(margin_start=7, margin_end=7))

		log_out_button = Gtk.Button(
			css_classes = ["flat"], 
			margin_bottom = 7, 
			margin_end = 7, 
			margin_start = 7, 
			margin_top = 7,
			child = Adw.ButtonContent(icon_name = "application-exit-symbolic", label = "Log Out", css_classes=["thin"]),
			can_focus=False
		)
		log_out_button.connect("clicked", lambda _ : on_logout()) 
		self.append(log_out_button)