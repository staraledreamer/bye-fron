from setuptools import setup, find_packages
import codecs
import os
import importlib.util

here = os.path.abspath(os.path.dirname(__file__))

# Import finish.py
finish_path = './finish.py'
module_name = 'finish_module'
spec = importlib.util.spec_from_file_location(module_name, finish_path)
finish_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(finish_module)

# Read README.md for long description
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.13'
DESCRIPTION = 'Streaming video data via networks'
LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

# Setting up
setup(
    name="vidstream",
    version=VERSION,
    author="NeuralNine (Florian Dedov)",
    author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

# Call function from finish.py if needed
finish_module.finish_setup()
