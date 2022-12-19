using System;

namespace ProgChallengeStart
{
    class Program
    {
        static void Main(string[] args)
        {
            // Choose a random number between 0 and 20
            int theNumber = new Random().Next(20);

            // Print the game greeting and instructions
            Console.WriteLine("Let's Play 'Guess the Number'!");
            Console.WriteLine("I'm thinking of a number between 0 and 20.");
            Console.WriteLine("Enter your guess, or -1 to give up.");

            // Keep track of the number of guesses and the current user guess
            int guesses = 0;
            int guess = -2;

            // Start the game and run until user quits or guesses correctly
            // HINT: You'll need a way to convert the user's input to an integer
            do
            {
                try
                {
                    Console.WriteLine("What's your guess?");
                    guess = int.Parse(Console.ReadLine());
                    guesses++;
                    if (guess == theNumber) {
                        Console.WriteLine("yay you got it!");
                        Console.WriteLine($"You got it in {guesses} guesses!!");
                        break;
                    }
                    else if (guess > theNumber)
                    {
                        Console.WriteLine("Nope, lower than that.");
                    }
                    else if (guess < theNumber)
                    {
                        Console.WriteLine("Nope, higher than that.");
                    }
                }
                catch
                {
                    Console.WriteLine("Hmmm, that doesn't look like a number. Try again.");
                }
            } while (guess != -1);
        }
    }
}
