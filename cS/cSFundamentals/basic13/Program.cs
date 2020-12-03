using System;

namespace basic13
{
    class Program
    {
        static void Main(string[] args)
        {
            // OddArray();
            ShiftValues(new int[] {1,5,10,7,-2});
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

        // Write a function that creates, and then returns, an array that contains all the odd numbers between 1 to 255. 
        // When the program is done, this array should have the values of [1, 3, 5, 7, ... 255].

        public static void ShiftValues(int[] numbers)
        {
            for(int i = 0; i<numbers.Length; i++){
                if(i==numbers.Length-1){
                    numbers[i] = 0;
                }
                else{
                    numbers[i] = numbers[i+1];
                }
            }
            // Write a function that shifts each number by one to the front and adds '0' to the end. 
            // For example, when the program is done, if the array [1, 5, 10, 7, -2] is passed to the function, 
            // it should become [5, 10, 7, -2, 0].
        }


    }
}
