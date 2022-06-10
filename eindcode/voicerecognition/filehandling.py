class File:
    def __init__(self, fileName, textString):
        self.fileName = fileName
        self.textString = textString


class FileHandler(File):
    def setFileContents(fileObj):  # Store file contents in a file
        file = open(fileObj.fileName + ".txt", "wt")
        file.write(fileObj.textString)
        file.close()

    def getFileContents(fileObj):  # Return contents from a file
        file = open(fileObj.fileName + ".txt", "rt")
        contents = file.read()
        return contents


fileObj = File("name", "Contents in file")
fileWriter = FileHandler.setFileContents(fileObj)
print(FileHandler.getFileContents(fileObj))