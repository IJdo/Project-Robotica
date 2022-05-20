

namespace RobotHond
{
    class Program
    {
        
        static void Main(string[] args)
        {
            Robot Hond = new Robot();

            while (true)
            {
                Hond.Ultra_FRNT.Calculate_distance();
                Console.WriteLine("afstand = " + Hond.Ultra_FRNT.Distance);

                
            }
        }
    }
}
