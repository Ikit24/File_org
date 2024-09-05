import os
from pathlib import Path

list_of_dirs = {
    "Pic_folder": [".pmg", ".jpeg", ".jpg", ".gif"],
    "Video_folder": [".mp4", ".wmv", ".mov", ".mpg", ".mpeg", ".mkv"],
    "Zip_folder": [".rar", ".zip", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg"],
    "Music_folder": [".mp3", ".msv", ".wav", ".wma"],
    "PDF_folder": [".pdf"],
}

File_Format_Dictionary = {
    final_file_format: directory
    for directory, file_format_stored in list_of_dirs.items()
    for final_file_format in file_format_stored
}


def organizer():
    for entry in os.scandir():
        if entry.is_dir():
            continue
            file_path = Path(entry)
            final_file_format = file_path.suffix.lower()
            if final_file_format in File_Format_Dictionary:
                directory_path = Path(File_Format_Dictionary[final_file_format])
        os.makedirs(directory_path, exist_ok=True)
        os.rename(file_path, directory_path.joinpath(file_path))


try:
    os.mkdir("Other_Folder")
except ValueError:
    print("Failed to create new directory")
for dir in os.scandir():
    try:
        if dir.is_dir():
            os.rmdir(dir)
        else:
            os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/Other_Folder/' + str(Path(dir)))
    except ValueError:
        print("Failed to create new directory called Other Folder. File directory already exist")

if __name__ == "__main__":

    organizer()
