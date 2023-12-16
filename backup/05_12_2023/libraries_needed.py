from kivy.lang import Builder
from kivymd.app import MDApp

from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast
from kivymd.uix.fitimage import FitImage
from kivymd.uix.toolbar import MDActionBottomAppBarButton, MDFabBottomAppBarButton
from kivymd.utils import asynckivy
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarCloseButton
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.segmentedbutton import MDSegmentedButton, MDSegmentedButtonItem

from kivy.properties import DictProperty
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import FadeTransition
from kivy.core.audio import SoundLoader
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.text import LabelBase
from kivy.clock import mainthread
from kivy.factory import Factory
# from kivy.core.window import Window
# Window.size = (400, 720)

import os
import re
import requests
from functools import partial
import json
from plyer import filechooser
from pylatexenc.latex2text import LatexNodes2Text
from threading import Thread
from time import sleep
from urllib.request import urlopen
from datetime import datetime