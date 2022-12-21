using System;
using System.Text;

namespace ProgChallenge {
    class Program
    {
        static (bool, int) IsPalindrome(string txt) {
            // StringBuilder sb = new StringBuilder();
            // foreach (char c in txt.ToLower())
            // {
            //     if (!char.IsPunctuation(c) && !char.IsWhiteSpace(c))
            //         sb.Append(c);
            // }
            // string trimmed = sb.ToString();

            // sb.Clear();
            // for (int i=trimmed.Length-1;i>=0;i--) {
            //     sb.Append(trimmed[i]);
            // }
            // string rev = sb.ToString();
            // return (trimmed.Equals(rev), txt.Length);

            txt = txt.ToLower();
            for (int i=0,j=txt.Length-1;i<j;i++,j--)
            {
                while (char.IsPunctuation(txt[i]) || char.IsWhiteSpace(txt[i])) {
                    i++;
                }
                while (char.IsPunctuation(txt[j]) || char.IsWhiteSpace(txt[j])) {
                    j--;
                }
                // Console.WriteLine($"{txt[i]} {txt[j]}");
                if (txt[i] != txt[j] || i>j)
                    return (false, 0);
            }
            return (true, txt.Length);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Let's begin:");
            while (true)
            {
                string txt = Console.ReadLine();
                if (txt.Equals("exit")) break;
                (bool, int) result = IsPalindrome(txt);
                Console.WriteLine($"Palindrome: {result.Item1}, Length: {result.Item2}");
            }
        }
    }
}

