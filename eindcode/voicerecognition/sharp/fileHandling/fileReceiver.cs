using System;
using System.IO; // for file handling

namespace sharp.fileHandling {
    sealed class fileReceiver {
        private string name;
        private string fileText { get; set; } = string.Empty;

        public fileReceiver(string fileName) {
            name = fileName;
        }

        public string receiveFile() {
            fileText = File.ReadAllText(@"..\" + name + ".txt");
            // Console.WriteLine(fileText);
            return fileText;
        }
    }
}