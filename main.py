import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

files = os.listdir()
files.remove("main.py")
#print(files)
createIfNotExist('Images')  #make folders
createIfNotExist('Docs')
createIfNotExist('Media')
createIfNotExist('Other')

imgExts = [".png",".jpg",".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = [".txt",".docx",".doc",".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
#print(docs)

mediaExts = [".mp4",".mp3",]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if(ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)

#print(others)

move("Images",images)
move("Docs",docs)
move("Media",medias)
move("Other",others)

