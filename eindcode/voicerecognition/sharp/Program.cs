// See https://aka.ms/new-console-template for more information
using System;
using LattePanda.Firmata;
using sharp.fileHandling;
using sharp.arduinoBrain;

namespace sharp{
    class Program{

        private fileHandling.fileReceiver fileReceiver = new fileReceiver("temporalCommand");
        private ArduinoBrain arduino = new ArduinoBrain();

        static void Main(string[] args)  {
            arduino.pinMode(arduino.leftForward, Arduino.OUTPUT);
            arduino.pinMode(arduino.leftBackward, Arduino.OUTPUT);
            arduino.pinMode(arduino.rightForward, Arduino.OUTPUT);
            arduino.pinMode(arduino.rightBackward, Arduino.OUTPUT);

            Dir(fileReceiver.receiveFile());
        }

        private void Dir(string command) {
            switch(command) {
                case "forward":
                case "go":
                    return arduino.Forward();
                    break;
                case "left":
                    return arduino.Left();
                    break;
                case "right":
                    return arduino.Right();
                    break;
                case "stop":
                    return arduino.Stop();
                    break;
            }
        }
    }
}