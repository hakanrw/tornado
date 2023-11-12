# Tornado
Example Gtk+Adwaita application written in Python

## Screenshots
![image](https://github.com/hakanrw/tornado/assets/57678928/3e5b85ca-b159-4078-aec6-65efbcb330fd)
![image](https://github.com/hakanrw/tornado/assets/57678928/fd10795c-7d9a-4c55-b430-fa79ba4f6e3f)

## Running
Note: This app only runs on Linux systems.

### As prebuilt AppImage
There are existing AppImage executables on workflow artifacts.
- Go to <a href="https://github.com/hakanrw/tornado/actions/workflows/create-appimage.yml">workflow runs</a>
- Select the latest workflow run at the top
- Install `Tornado-x86_64.AppImage` from Artifacts section
- After download, make it executable by `chmod +x Tornado-x86_64.AppImage`
- Run the app by `./Tornado-x86_64.AppImage`   

### From source
This is a simple python application.
- Clone the repository by `git clone https://github.com/hakanrw/tornado.git`
- Cd into the newly installed repo by `cd tornado`
- Run the project by `python3 src/tornado.py`

## Building AppImage executable
- Install `appimagetool` and `make` if you do not have it
- Run `make`
- The executable should have been generated at `Tornado-x86_64.AppImage`

## Trivia
You can find users and their passwords written in cleartext at `src/users.py`.

Or just login as `admin` with the password `admin`
