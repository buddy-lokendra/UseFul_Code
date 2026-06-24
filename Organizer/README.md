# 📂 File Organizer Automation

A Python automation tool that automatically organizes files from a folder into structured categories and month-wise directories.

This project helps to clean and manage your files automatically without manually sorting images, videos, documents, and other files.

---

# 🚀 Features

- Automatic file organization
- Category-based sorting
- Month-wise folder management
- Supports multiple file formats
- Duplicate file handling
- No file overwrite
- Safe file movement
- Existing organized files can be processed again

---

# 📌 How It Works

The script scans files from the current directory and automatically moves them into the `Organized` folder.

Files are separated based on their extension and creation/modification month.

Example:


Downloads
│
├── photo.jpg
├── movie.mp4
├── song.mp3
├── report.docx
│
└── code.py


After running:


Organized

├── images
│ └── 2026-06
│ └── photo.jpg
│
├── videos
│ └── 2026-06
│ └── movie.mp4
│
├── songs
│ └── 2026-06
│ └── song.mp3
│
└── word
└── 2026-06
└── report.docx


---

# 🛠️ Technologies Used

- Python 3
- OS Module
- Shutil Module
- Datetime Module

No external packages required.

---

# 📂 Supported File Categories

## Images


.jpg
.jpeg
.png
.gif
.webp
.bmp


## Videos


.mp4
.mkv
.avi
.mov


## Audio / Songs


.mp3
.flac
.aac
.ogg
.wav


## Documents


.pdf
.doc
.docx
.xls
.xlsx
.csv
.ppt
.pptx


## Code Files


.py
.java
.js
.html
.css
.json
.xml
.yml
.yaml


---

# ▶️ Installation & Usage

## Clone Repository

```bash
git clone https://github.com/your-username/File-Organizer-Automation.git
Navigate into project
cd File-Organizer-Automation
Run Application
python code.py
🔐 Safety Features
Original files are moved safely
No permanent deletion
Existing files are not replaced
Duplicate names are automatically renamed

Example:

file.jpg

file_repeat1.jpg
file_repeat2.jpg
🎯 Use Cases

This project can be useful for:

Cleaning Downloads folder
Managing personal files
Organizing office documents
Automating daily file management tasks
📁 Project Structure
File-Organizer-Automation

│
├── code.py
│
├── README.md
│
└── Organized/
👨‍💻 Author

Lokendra Pandit

📄 License

This project is open-source and available for learning and personal use.