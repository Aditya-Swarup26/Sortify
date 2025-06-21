# Sortify

Sortify is a Python script that automatically organizes your messy folders by sorting files into categorized subfolders based on their file extensions. It also keeps a log of every action taken!

## 🚀 Features
- Automatically creates folders like Images, Videos, Documents, etc.
- Sorts files into appropriate folders.
- Moves unknown file types into an "Others" folder.
- Logs every move in a `organizer_log.txt` file.
- Easily customizable to support more file types.

## 📁 Supported File Types

| Category      | Extensions                                     |
|---------------|------------------------------------------------|
| Images        | .jpg, .jpeg, .png, .gif                        |
| Videos        | .mp4, .mkv, .flv                               |
| Documents     | .txt, .pdf, .docx                              |
| Audios        | .mp3, .wav                                     |
| Spreadsheets  | .xlsx, .xls, .csv                              |
| Archives      | .zip, .tar, .rar                               |
| Codes         | .py, .html, .css, .cpp, .c, .js, .jsx          |
| Others        | Any unsupported file types                     |

## ⚙️ How to Use
1. Clone this repo:
   ```bash
   git clone https://github.com/Aditya-Swarup26/Sortify.git
   cd Sortify
2. Run the script:
   
        ->python sortify.py
   
   
4. Enter the full path of the folder you want to organize.
5. Sit back and let Sortify tidy up your files!

📝 Logs

   ->All actions are saved in a organizer_log.txt file inside the source folder.

🛠️ Requirements

   ->Python 3.x
   ->No external libraries needed (uses built-in os, shutil, datetime)

✨ License

   ->MIT License



