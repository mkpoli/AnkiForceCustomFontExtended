# -*- coding: utf-8 -*-
# Force Custom Font Extended v2.4.1
#
# This add-on will allow you to force Anki to use a custom font instead of the default system font by menu options.
# You can also change font size as well as font subtituitions
# by editing the constant "substitutions" following code.
#
# - By mkpoli
# https://github.com/mkpoli
# Based on
# https://ankiweb.net/shared/info/2103013902
#
# \C\o\p\y\r\i\g\h\t: mkpoli
# \C\o\p\y\r\i\g\h\t: Damien Elmes <anki@ichi2.net> (https://github.com/dae)
#
# License: GNU GPL, version 3 or later
#
# This add-on is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This add-on is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# For more details, see <http://www.gnu.org/licenses/>.
from __future__ import with_statement

import os.path
import pickle
import xml.etree.ElementTree as ET
import sip
sip.setapi('QString', 2)

from anki.hooks import addHook
from aqt import mw
from aqt.qt import *

# Font subtitutions.
substitutions = ["Microsoft YaHei UI", "Microsoft YaHei", "HanaMinA", "HanaMinB"]

FONT_CONFIG_XML = None

current_font = None
current_font_ui = None

def save_config(font, font_ui):
    """Recieve QFont objects and save font config as a xml file."""
    font_info = QFontInfo(font)
    font_ui_info = QFontInfo(font_ui)
    fontconfig = ET.Element("fontconfig")
    general = ET.SubElement(
        fontconfig, "font",
        attrib={
            "type": "general",
            "family": font_info.family(),
            "size": str(font_info.pixelSize())
        }
    )
    ui = ET.SubElement(
        fontconfig, "font",
        attrib={
            "type": "menu",
            "family": font_ui_info.family(),
            "size": str(font_ui_info.pixelSize())
        }
    )
    with open(FONT_CONFIG_XML, "w") as xml_file:
        ET.ElementTree(fontconfig).write(xml_file, encoding="utf-8", xml_declaration=True)

from aqt.utils import showInfo

def load_config():
    """Load font config from a xml file and return QFont objects."""
    global current_font, current_font_ui
    font = None
    font_ui = None
    try:
        xml_file = open(FONT_CONFIG_XML, "r")
    except (EnvironmentError, ET.ParseError):
        raise
    else:
        with xml_file:
            tree = ET.parse(xml_file)
            fontconfig = tree.getroot()
            for font_tag in list(fontconfig):
                fontfamily = font_tag.attrib["family"]
                fontsize = int(font_tag.attrib["size"])
                if font_tag.attrib["type"] == "general":
                    font = QFont(fontfamily, fontsize)
                elif font_tag.attrib["type"] == "menu":
                    font_ui = QFont(fontfamily, fontsize)
    current_font = font
    current_font_ui = font_ui
    return font, font_ui

def process_font_fallback(font, substitutions):
    """
    Add substitutions of the font and set style strategy to PreferAntialias.

    Arguments:
    font -- font ready to be added
    substitutions -- a list of str contains the name of font substitution 

    Return Value:
    font -- processed font

    Side Effect:
    All fonts would have a substitution as long as its family name is same as the font.
    """
    font_info = QFontInfo(font)
    QFont.insertSubstitutions(font_info.family(), substitutions)
    font.setStyleStrategy(QFont.PreferAntialias)
    return font

def change_font(font, font_size=None):
    """Change font in main form and all webview fonts."""
    f = QFontInfo(font)
    ws = QWebSettings.globalSettings()
    mw.fontHeight = f.pixelSize() if not font_size else font_size
    mw.fontFamily = f.family()
    mw.fontHeightDelta = max(0, mw.fontHeight - 13)
    ws.setFontFamily(QWebSettings.StandardFont, mw.fontFamily)
    ws.setFontSize(QWebSettings.DefaultFontSize, mw.fontHeight)
    mw.reset()

def change_ui_font(font):
    """Change UI font (mostly menu and dialog text)."""
    QApplication.setFont(font)

#### While Initializaiton ####
def onProfileLoaded():
    global FONT_CONFIG_XML
    global current_font, current_font_ui

    FONT_CONFIG_XML = os.path.join(mw.pm.profileFolder(), "font_config.xml")

    font = None
    font_ui = None
    try:
        font, font_ui = load_config()
    except IOError:
        pass

    if font:
        change_font(font)
    else:
        current_font = QFont(mw.fontFamily, mw.fontHeightDelta)
    if font_ui:
        change_ui_font(font_ui)
    else:
        current_font_ui = QFont(QApplication.font())

addHook("profileLoaded", onProfileLoaded)
###############################

###### User Manipulation ######
def onChangeFont():
    global current_font
    font, success = QFontDialog.getFont(current_font, mw)
    processed_font = process_font_fallback(font, substitutions)
    if success:
        change_font(processed_font)
    current_font = processed_font
    save_config(current_font, current_font_ui)
    

def onChangeUIFont():
    global current_font_ui
    font, success = QFontDialog.getFont(current_font_ui, mw)
    processed_font = process_font_fallback(font, substitutions)
    if success:
        change_ui_font(processed_font)
    current_font_ui = processed_font
    save_config(current_font, current_font_ui)

menu_item = QAction("Change General Font", mw)
menu_item_2 = QAction("Change Menu Font", mw)
mw.connect(menu_item, SIGNAL('triggered()'), onChangeFont)
mw.connect(menu_item_2, SIGNAL('triggered()'), onChangeUIFont)
mw.form.menuTools.addSeparator()
mw.form.menuTools.addAction(menu_item)
mw.form.menuTools.addAction(menu_item_2)
mw.form.menuTools.addSeparator()
###############################
