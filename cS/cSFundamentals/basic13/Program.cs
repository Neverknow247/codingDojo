using System;

namespace basic13
{
    class Program
    {


        static void Main(string[] args)
        {
            int[] arr = { 1, -2, 4, 5, -9, 7 };
            NumToString(arr);
        }
        public static void PrintNumbers()
        {
            for (int i = 1; i < 256; i++)
            {
                Console.WriteLine(i);
            }
        }
        public static void PrintOdds()
        {
            for (int i = 1; i < 256; i++)
            {
                if (i % 2 == 1)
                {
                    Console.WriteLine(i);
                }
            }
        }
        public static void PrintSum()
        {
            int sum = 0;
            for (int i = 0; i < 256; i++)
            {
                sum += i;
                Console.WriteLine($"New number: {i} Sum: {sum}");
            }
        }
        public static void LoopArray(int[] numbers)
        {
            for (int i = 0; i < numbers.Length; i++)
            {
                Console.WriteLine(numbers[i]);
            }
        }
        public static int FindMax(int[] numbers)
        {
            int max = numbers[0];
            for (int i = 1; i < numbers.Length; i++)
            {
                if (numbers[i] > max)
                {
                    max = numbers[i];
                }
            }
            Console.WriteLine(max);
            return max;
        }
        public static void GetAverage(int[] numbers)
        {
            int average = 0;
            for (int i = 0; i < numbers.Length; i++)
            {
                average += numbers[i];
            }
            average = average / numbers.Length;
            Console.WriteLine(average);
        }
        public static int[] OddArray()
        {
            int count = 0;
            for (int i = 1; i <= 255; i++)
            {
                if (i % 2 == 1)
                {
                    count++;
                }
            }
            int[] arr = new int[count];
            int temp = 0;
            for (int i = 1; i <= 255; i++)
            {
                if (i % 2 == 1)
                {
                    arr[temp] = i;
                    temp++;
                }
            }
            foreach (int num in arr)
            {
                Console.WriteLine(num);
            }
            return arr;
        }
        public static int GreaterThanY(int[] numbers, int y)
        {
            int greater = 0;
            for (int i = 0; i < numbers.Length; i++)
            {
                if (numbers[i] > y)
                {
                    greater++;
                }
            }
            Console.WriteLine(greater);
            return greater;
        }
        public static void SquareArrayValues(int[] numbers)
        {
            for (int i = 0; i < numbers.Length; i++)
            {
                numbers[i] = numbers[i] * numbers[i];
                Console.WriteLine(numbers[i]);
            }
        }
        public static void EliminateNegatives(int[] numbers)
        {
            for (int i = 0; i < numbers.Length; i++)
            {
                if (numbers[i] < 0)
                {
                    numbers[i] = 0;
                }
            }
        }
        public static void MinMaxAverage(int[] numbers)
        {
            int max = numbers[0];
            int min = numbers[0];
            int avg = 0;
            for (int i = 0; i < numbers.Length; i++)
            {
                if (numbers[i] > max)
                {
                    max = numbers[i];
                }
                if (numbers[i] < min)
                {
                    min = numbers[i];
                }
                avg += numbers[i];
            }
            avg = avg / numbers.Length;
            Console.WriteLine($"Max: {max} Min: {min} Avg: {avg}");
        }
        public static void ShiftValues(int[] numbers)
        {
            for (int i = 0; i < numbers.Length; i++)
            {
                if (i == numbers.Length - 1)
                {
                    numbers[i] = 0;
                }
                else
                {
                    numbers[i] = numbers[i + 1];
                }
            }
        }
        public static object[] NumToString(int[] numbers)
        {
            string[] arr = new string[numbers.Length];
            for(int i =0; i<numbers.Length;i++)
            {
                if(numbers[i] < 0)
                {
                    arr[i] = "Dojo";
                }
                else
                {
                    arr[i] = numbers[i].ToString();
                }
                Console.WriteLine(arr[i]);
            }
            return arr;
        }
    }
}
