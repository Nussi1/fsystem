from tkinter import Tk
from tkinter.filedialog import askdirectory
import os

import hashlib

Tk().withdraw()
path = askdirectory(title="Select a folder")