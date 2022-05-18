using System.Threading;
using LattePanda.Firmata; // includes arduino.cs needed to send UART messages to Arduino from Latte

namespace BlinkingLed
{
    class Program
    {
        static void Main(string[] args)
        {
            int IN1 = 8;
            int IN2 = 9;
            int IN3 = 10;
            int IN4 = 11;

            Arduino arduino = new Arduino(); // object arduino needed to write to arduino Leonardo (co-processor Latte)
            arduino.pinMode(IN1, Arduino.OUTPUT); // D8 as output
            arduino.pinMode(IN2, Arduino.OUTPUT); // D9 as output
            arduino.pinMode(IN3, Arduino.OUTPUT); // D10 as output
            arduino.pinMode(IN4, Arduino.OUTPUT); // D11 as output

            while (true)
            {
                // Rotate the Motor A clockwise
                //arduino.digitalWrite(IN1, Arduino.HIGH);
                //arduino.digitalWrite(IN2, Arduino.LOW);
                //Thread.Sleep(2000);
                // Motor A
                arduino.digitalWrite(IN1, Arduino.HIGH);
                arduino.digitalWrite(IN2, Arduino.HIGH);
                arduino.digitalWrite(IN3, Arduino.HIGH);
                arduino.digitalWrite(IN4, Arduino.HIGH);

                //arduino.digitalWrite(IN2, Arduino.HIGH);
                //Thread.Sleep(500);

                // Rotate the Motor B clockwise
                //arduino.digitalWrite(IN3, Arduino.HIGH);
                //arduino.digitalWrite(IN4, Arduino.LOW);
                //Thread.Sleep(2000);
                //// Motor B
                //arduino.digitalWrite(IN3, Arduino.HIGH);
                //arduino.digitalWrite(IN4, Arduino.HIGH);
                //Thread.Sleep(500);

                //// Rotates the Motor A counter-clockwise
                //arduino.digitalWrite(IN1, Arduino.LOW);
                //arduino.digitalWrite(IN2, Arduino.HIGH);
                //Thread.Sleep(2000);
                //// Motor A
                //arduino.digitalWrite(IN1, Arduino.HIGH);
                //arduino.digitalWrite(IN2, Arduino.HIGH);
                //Thread.Sleep(500);

                //// Rotates the Motor B counter-clockwise
                //arduino.digitalWrite(IN3, Arduino.LOW);
                //arduino.digitalWrite(IN4, Arduino.HIGH);
                //Thread.Sleep(2000);
                //// Motor B
                //arduino.digitalWrite(IN3, Arduino.HIGH);
                //arduino.digitalWrite(IN4, Arduino.HIGH);
                //Thread.Sleep(500);
            }
        }
    }
}