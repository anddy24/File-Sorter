import os
import shutil

# source directory
source_directory = "~/Downloads"  # path

# file categories
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Scripts": [".py", ".sh", ".js", ".php"],
    "Executables": [".exe", ".bin", ".app", ".run"]
}

# creating the direcotries from the dictionary keys
for category in file_categories.keys():
    category_path = os.path.join(source_directory, category)
    os.makedirs(category_path, exist_ok=True)


for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()

        for category, extensions in file_categories.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(source_directory, category, filename))
                print(f"Mutat: {filename} → {category}")
                break

print("Sortare completă!")

