using System;

namespace human
{
    class Program
    {
        public static void Main(string[] args)
        {
            Human nathan = new Human("Nathan");
            Human rob = new Human("Rob");
            nathan.Attack(rob);
            nathan.Attack(rob);
            nathan.Attack(rob);
        }
    }

    class Human
    {
        // Fields for Human
        public string Name;
        public int Strength;
        public int Intelligence;
        public int Dexterity;
        private int health;

        public int Health
        {
            get { return health; }
        }
        public Human(string name)
        {
            Name = name;
            Strength = 3;
            Intelligence = 3;
            Dexterity = 3;
            health = 100;
        }

        public Human(string name, int str, int intel, int dex, int hp)
        {
            Name = name;
            Strength = str;
            Intelligence = intel;
            Dexterity = dex;
            health = hp;
        }

        // Build Attack method
        public int Attack(Human target)
        {
            Console.WriteLine($"{this.Name} has attacked {target.Name}.");
            target.health -= this.Strength * 5;
            Console.WriteLine($"{target.Name} has {target.health} health remaining!");
            return target.health;
        }
    }


}
