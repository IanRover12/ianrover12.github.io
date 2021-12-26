import os

# convert .jfif to .jpg
imageFolders = os.listdir("images")
for folder in imageFolders:
    imageFolder = "images/" + folder
    images = os.listdir(imageFolder)
    for image in images:
        if ".jfif" in image:
            newName = image.split(".jfif")[0] + ".jpg"
            imageDir = imageFolder + "/" + image
            newImageDir = imageFolder + "/" + newName
            os.rename(imageDir,newImageDir)