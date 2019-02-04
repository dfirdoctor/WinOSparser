from distutils.core import setup
import py2exe
setup(console=['WinOSparser.py'],
	options = {'py2exe': {'bundle_files': 1,'compressed': 1, 'optimize': 2}},
	zipfile = None
)