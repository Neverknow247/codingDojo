using System;

namespace basic13
{
    class Program
    {
        static void Main(string[] args)
        {
            OddArray();
        }
        public static int[] OddArray()
        {
            int count = 0;
            for(int i = 1; i<=255; i++){
                if(i%2==1){
                    count++;
                }
            }
            int[] arr = new int[count];
            int temp = 0;
            for(int i = 1; i <=255;i++){
                if(i%2==1){
                    arr[temp]=i;
                    temp++;
                }
            }
            foreach(int num in arr){
                Console.WriteLine(num);
            }
            return arr;
        }

        // Write a function that creates, and then returns, an array that contains all the odd numbers between 1 to 255. 
        // When the program is done, this array should have the values of [1, 3, 5, 7, ... 255].
    }
}
