import os
from pathlib import Path
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt','.doc','.docx'],
	"EXECUTABLES":['.exe','.msi'],
	"PRESENTATIONS":['.ppt','.pptx'],
	"SPREADSHEET":['.xls','.xlsx','.csv'],
	"SCRIPTS":['.py','.ipynb','.vbs','.cpp'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}
def  pickDirectory(value):
    for category,suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'


def organizeDirectory():
    #Scandir used to scan files in directories
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item) #Store item path to filePath variables
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()
