using System;

namespace Exceptions
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 100;
            int y = 10;
            int result;

            // TODO: try-catch expressions make error checking easier
            try
            {
                result = x / y;
                if (x>1000) throw new ArgumentOutOfRangeException("x", "x must be less than 1000");
                Console.WriteLine("The result is: {0}", result);
            }
            catch (ArgumentOutOfRangeException e)
            {
                Console.WriteLine(e.Message);
            }
            finally {
                Console.WriteLine("done");
            }
        }
    }
}
