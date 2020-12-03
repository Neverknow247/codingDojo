using System;
using DeckofCards.Models;

namespace DeckofCards
{
    class Program
    {
        static void Main(string[] args)
        {
            Deck newDeck = new Deck();
            newDeck.PrintDeckInfo();

            Card tempCard = newDeck.Deal();
            int i = 52;
            while (i > 0)
            {
                newDeck.PrintCardInfo(tempCard);
                    if(i==0){
                    return;
                }
                tempCard = newDeck.Deal();
                i--;
            }


        }


    }
}
