# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
### TODO
- Preference Menu.
- Add option to change font subsitituions.
- Add option to change font render style.

## [2.4.2] - 2017-08-20
### Fixed
- Wrong convert on pixelsize vs pointsize

## [2.4.1] - 2017-08-20
### Fixed
- Open-source license and declaration.

## [2.4.0] - 2017-08-19
### Added
- Detailed Information in Comments.
- Now font config can be saved into user profile folder.
### Changed
- Better docstring adheres to PEP 257.
- Cleared Code and Comments.
### Fixed
- Now can read font config successfully.

## [2.3.0] - 2017-08-16
### Added
- Better Font Rendering (Amti-Aliasing).
### Changed
- Cleared Code and Comments.
- Default value of FONT_SUBTITUTIONS -> ["Microsoft YaHei UI", "Microsoft YaHei", "HanaMinA", "HanaMinB"].
- Text of UI Font Changing -> Menu Font.
- Text of Font Changing -> General Font.

## [2.2.1] - 2017-08-16
### Fixed
- onChangeUIFont() called change\_font -> change\_ui\_font.
- onChangeFont(): first argument of getFont() QFont(QApplication.font()) -> QFont(mw.fontFamily, mw.fontHeightDelta).

## [2.2.0] - 2017-08-16
### Added
- Added two menu items to change font seperately.
- Menu seperator for better appearance.
### Chamged
- Menu item "Change font" can only change webview font now.
- Better CHANGELOG following [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2017-08-16
### Added
- TODO list.
- CHANGELOG.
- Menu item "Change font".

## [2.0.1] - 2017-08-16
### Fixed
- Defunction by hacking of onPref due to unknown failure.

## [2.0.0] - 2017-08-15 [YANKED]
### Added
- Hacking of entrance function (onPref) of Preference Dialog.
### Changed
- Constant controll to FontDialog.
### Removed
- All Constants.

## [1.0.0] - 2016-09-09
### Added
- UI Font change switches by bool constant CHANGE\_UI\_FONT (Default True).
- Basic support (hard-coded) for font fallback (especially for CJK characters).
- Constant list FONT_SUBTITUTIONS for easier modification of font fallback list (Default ["Microsoft YaHei UI", "Microsoft YaHei"]).

## [0.2.0] - 2016-09-08
### Added
- Constant FONT\_HEIGHT for easier controll of font "size" (= font height = pixel size) (Default 16), inspired by Review post "How to" posted on 2013-11-30 (https://ankiweb.net/shared/info/2103013902).
- Comments to every constant.

## [0.1.0] - 2016-09-07
### Added
- Original Code From customfont by dae (Damien Elmes <anki@ichi2.net>).
- Constant FONT for easier controll of font type (Default "PT Serif").
### Changed
- Style of naming variables (f -> font).