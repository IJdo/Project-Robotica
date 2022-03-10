using System.Threading;
using LattePanda.Firmata; // includes arduino.cs needed to send UART messages to Arduino from Latte

namespace BlinkingLed
{
    class Program
    {
        static void Main(string[] args)
        {
            Arduino arduino = new Arduino(); // object arduino needed to write to arduino (co processor Latte)
            arduino.pinMode(13, Arduino.OUTPUT); // D13 as output
            while (true)
            {
                // Turns pin D13 and led D13 ON and OFF, 500ms each
                arduino.digitalWrite(13, Arduino.HIGH);
                Thread.Sleep(500);
                arduino.digitalWrite(13, Arduino.LOW);
                Thread.Sleep(500);
            }
        }
    }
}
