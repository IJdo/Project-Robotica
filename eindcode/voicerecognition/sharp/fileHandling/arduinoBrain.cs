using System;
using System.IO; // for file handling
using LattePanda.Firmata;

namespace sharp.arduinoBrain {
    class ArduinoBrain {
        private Arduino arduino = new Arduino();

        private uint leftForward = 8; // left
        private uint leftBackward = 9; // left
        private uint rightForward = 10; // right
        private uint rightBackward = 11; // right

        public void Forward() {
            // Motor right ON
            arduino.digitalWrite(leftForward, Arduino.HIGH);
            arduino.digitalWrite(leftBackward, Arduino.LOW);
            Thread.Sleep(1000);
            // Motor left ON
            arduino.digitalWrite(rightForward, Arduino.HIGH);
            arduino.digitalWrite(rightBackward, Arduino.LOW);
        }

        public void Left() {
            arduino.digitalWrite(leftForward, Arduino.HIGH);
            arduino.digitalWrite(rightBackward, Arduino.HIGH);
            Thread.Sleep(1000);
            //Motor Control Left
            arduino.digitalWrite(leftForward, Arduino.LOW);
            arduino.digitalWrite(rightBackward, Arduino.LOW);
        }

        public void Right() {
            arduino.digitalWrite(rightForward, Arduino.HIGH);
            arduino.digitalWrite(leftBackward, Arduino.HIGH);
            Thread.Sleep(1000);
            //Motor Control Left
            arduino.digitalWrite(rightForward, Arduino.LOW);
            arduino.digitalWrite(leftBackward, Arduino.LOW);
        }

        public void Stop() {
            arduino.digitalWrite(rightForward, Arduino.LOW);
            arduino.digitalWrite(rightBackward, Arduino.LOW);
            arduino.digitalWrite(leftForward, Arduino.LOW);
            arduino.digitalWrite(leftBackward, Arduino.LOW);
        }

        // public string receiveFile() {
        //     fileText = File.ReadAllText(@"..\" + name + ".txt");
        //     // Console.WriteLine(fileText);
        //     return fileText;
        // }
    }
}