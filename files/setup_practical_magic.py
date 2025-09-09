__required_version__ = 23.1

# check if we need to install / update 
__version__ = 0.0
import os.path
if os.path.isdir("setup_practical_magic"):
    from setup_practical_magic import __version__
if __version__<__required_version__:
    import urllib.request
    content = urllib.request.urlopen ("https://setu-discretemathematics.github.io/live/files/setup_practical_magic.zip")
    import zipfile
    from io import BytesIO
    data = zipfile.ZipFile(BytesIO(content.read()))
    data.extractall(".")
    
# now import magic
from setup_practical_magic import *


