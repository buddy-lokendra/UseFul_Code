import os
import shutil
from datetime import datetime


SOURCE = os.path.dirname(os.path.abspath(__file__))

DEST = os.path.join(SOURCE, "Organized")

SCRIPT_NAME = os.path.basename(__file__)

SKIP_FILES = {
    SCRIPT_NAME,
    "run.bat"
}



def collect_files():

    paths = []


    for name in os.listdir(SOURCE):

        path = os.path.join(SOURCE, name)


        if os.path.isdir(path):
            continue


        if name in SKIP_FILES:
            continue


        paths.append(path)



    # Organized folder ke andar ki files bhi collect karo

    if os.path.isdir(DEST):

        for root, dirs, files in os.walk(DEST):

            for file in files:

                path = os.path.join(root, file)

                paths.append(path)


    return paths





file_types = {


    "pdf": [
        ".pdf"
    ],


    "excel": [
        ".xls",
        ".xlsx",
        ".xlsm",
        ".xlsb",
        ".csv"
    ],


    "word": [
        ".doc",
        ".docx"
    ],


    "powerpoint": [
        ".ppt",
        ".pptx"
    ],


    "images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp",
        ".bmp"
    ],


    "videos": [
        ".mp4",
        ".mkv",
        ".avi",
        ".mov"
    ],


    "songs": [
        ".mp3",
        ".flac",
        ".aac",
        ".ogg"
    ],


    "audio": [
        ".wav",
        ".m4a",
        ".wma"
    ],


    "archives": [
        ".zip",
        ".rar",
        ".7z"
    ],


    "text": [
        ".txt",
        ".md",
        ".log"
    ],


    "code": [
        ".py",
        ".java",
        ".js",
        ".html",
        ".css",
        ".json",
        ".xml",
        ".yml",
        ".yaml"
    ]

}





def get_category(ext):

    ext = ext.lower()


    for category, extensions in file_types.items():


        if ext in extensions:

            return category



    return None





def duplicate_name(folder, filename):


    name, ext = os.path.splitext(filename)


    new_name = filename

    count = 1



    while os.path.exists(
        os.path.join(folder, new_name)
    ):


        new_name = f"{name}_repeat{count}{ext}"

        count += 1



    return new_name







def organize_files():


    os.makedirs(
        DEST,
        exist_ok=True
    )



    for file_path in collect_files():


        file = os.path.basename(file_path)


        ext = os.path.splitext(file)[1]


        category = get_category(ext)



        if category is None:

            continue




        # Month folder create

        month = datetime.fromtimestamp(
            os.path.getmtime(file_path)
        ).strftime("%Y-%m")



        target_folder = os.path.join(
            DEST,
            category,
            month
        )



        os.makedirs(
            target_folder,
            exist_ok=True
        )




        new_file = duplicate_name(
            target_folder,
            file
        )




        try:


            shutil.move(

                file_path,

                os.path.join(
                    target_folder,
                    new_file
                )

            )


            print(
                f"Moved: {file} --> {category}/{month}"
            )



        except Exception as e:


            print(
                "Error:",
                file,
                e
            )






if __name__ == "__main__":


    organize_files()



    print("\n==========================")

    print(" DONE - FILES ORGANIZED ")

    print(" MONTH WISE SORT COMPLETE ")

    print(" NO DELETE / NO OVERWRITE ")

    print("==========================")