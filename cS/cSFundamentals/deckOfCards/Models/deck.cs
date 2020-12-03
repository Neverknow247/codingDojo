namespace DeckOfCards.Models
{
    public class Card
    {
        private string[] stringVal ={"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};

        private string[] suits = {"Clubs", "Spades", "Hearts", "Diamonds"};

        private int[] val = {1,2,3,4,5,6,7,8,9,10,11,12,13};
        private object stringVal1;
        private string suit;
        private int numVal;

        public Card(object stringVal1, string suit, int numVal)
        {
            this.stringVal1 = stringVal1;
            this.suit = suit;
            this.Val = numVal;
        }
    }
    
}