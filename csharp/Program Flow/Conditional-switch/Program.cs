using System;

namespace ConditionalOps
{
    class Program
    {
        static void Main(string[] args)
        {
            int theVal = 50;

            // TODO: The switch statement
            switch (theVal)
            {
                case 52:
                case 53:
                case 54:
                    Console.WriteLine("52-54");
                    break;
                default:
                    Console.WriteLine("oh my");
                    break;
            }
        }
    }
}
