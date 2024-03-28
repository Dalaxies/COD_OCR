# Call of Dragons OCR
This is a python implementation to get alliance members' power and merits.
## Requirements
### On Windows
- Python 3.11.7
- ADB (https://developer.android.com/tools/releases/platform-tools)
- Poetry (https://python-poetry.org/docs/#installation)
- Tesseract (https://github.com/UB-Mannheim/tesseract/wiki))
- Android Emulator - Personally I used the emulator **LDPlayer9** (https://www.ldplayer.net/versions)
### On Android Emulator
- Android 9 or lower
- Resolution set at **1280 x 720**
- Latest CoD APK + Logged into account
- AdbClipboard-2.0_3-release.apk (https://github.com/PRosenb/AdbClipboard/releases)
## Set Up
### dotenv file
Copy `.env.example` to `.env` and fill it with install locations.  
```
ADB_BINARY=[path to adb.exe]
ADB_DEVICE_NAME=To get your `ADB_DEVICE_NAME`, run `adb devices`.  
TESSERACT_BINARY=[path to tesseract.exe]
GOOGLE_SPREADSHEET_ID=(direct write work in progress, import CSV for now)
```
### Poetry Setup
1. run `poetry shell` in a terminal of this folder.  
2. then run `poetry install` to install all requirements.  
## Execute
With an active shell, run `python main.py`.  The tool will print out the alliance tag, name, members and position of the current account after a while.  Then it will go through the rankings without further logging.  All errors will be printed, safe to ignore errors do not crash/exit the program.
