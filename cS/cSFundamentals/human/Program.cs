using System;

namespace human
{
    class Program
    {
        public static void Main(string[] args)
        {
            Vehicle myVehicle = new Vehicle(7);
            Console.WriteLine($"My vehicle is holding {myVehicle.numPassengers} people");
        }
    }
    class Vehicle
    {
        public int numPassengers;
        public Vehicle(int val)
        {
            numPassengers = val;
        }
    }
}
