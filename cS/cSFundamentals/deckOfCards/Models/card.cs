

namespace DeckofCards.Models
{
    public class Card
    {
        public string stringVal;

        public string suit;

        public int val;

        public Card(string sValue, string su, int value)
        {
            stringVal = sValue;
            suit = su;
            val = value;
        }

    }

}