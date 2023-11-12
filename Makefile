install_dir = /opt/tornado

AppImage: AppDir
	ARCH=x86_64 appimagetool AppDir


AppDir: clean
	mkdir -p AppDir/$(install_dir)

	cp -r src/. AppDir/$(install_dir)

	cp -r res/. AppDir/

	ln -s opt/tornado/tornado.py AppDir/AppRun

clean:
	rm -rf AppDir
	rm -f Tornado-x86_64.AppImage


run: AppImage
	./Tornado-x86_64.AppImage
