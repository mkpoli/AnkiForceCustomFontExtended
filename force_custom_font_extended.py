# -*- coding: utf-8 -*-
# Force Custom Font Extended
# This add-on will allow you to force Anki to use a custom font instead of the default system font. You can also change font size as well as font subtituitions.
# You will need to edit the following CONSTANTS to make it work
# - By mkpoli
# https://github.com/mkpoli
# Based on
# https://ankiweb.net/shared/info/2103013902
# - Legacy Comment -
# \C\o\p\y\r\i\g\h\t: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# - Legacy Comment Over -
"""
default font
"""
FONT = "PT Serif"
"""
font subtitutions
"""
FONT_SUBTITUTIONS = ["Microsoft YaHei UI", "Microsoft YaHei"]
"""
font size
"""
FONT_HEIGHT = 16
"""
Change Basic UI Font as well?
"""
CHANGE_UI_FONT = True

from aqt import mw
from aqt.qt import *

## DEBUG
# from anki_debug import print_err
## DEBUG END

def changeFont():
    QFont.insertSubstitutions(FONT, FONT_SUBTITUTIONS)
    font = QFont(FONT)
    if (CHANGE_UI_FONT):
        QApplication.setFont(font)
    f = QFontInfo(font)
    ws = QWebSettings.globalSettings()
    # mw.fontHeight = f.pixelSize()
    mw.fontHeight = FONT_HEIGHT
    mw.fontFamily = f.family()
    mw.fontHeightDelta = max(0, mw.fontHeight - 13)
    ws.setFontFamily(QWebSettings.StandardFont, mw.fontFamily)
    ws.setFontSize(QWebSettings.DefaultFontSize, mw.fontHeight)
    mw.reset()
    ## DEBUG
    # print_err('Font-fmaily : ' + f.family())
    # print_err('Font-Subtitutions: ' + ','.join(font.substitutions()))
    # print_err('f.pixelSize() = %d' % f.pixelSize())
    # debug()
    ## DEBUG END

changeFont()
