#!/usr/bin/env python

""" Simple version of classic lemonade stand game. Written in Python 2.7 
"""

__author__ = 'jeremy osborn'

import random


question_dict = {"Hey! {player name} where have you been? Betty needs your help painting her house. She has to paint 1000 square feet of walls in her house and she knows that a gallon of paint can cover 250 square feet of wall. Help her figure out how many gallons of paint she needs. \n" : 4,"Betty needs your help once again. This time, she wants to put a fence around her farm and needs to figure out how much material she needs. She knows her farm is a perfect square with area 3600 feet^2, how many feet of fencing does she need to enclose her whole farm? (integer only) \n": 240}





class LemonadeStand:

    """ LemonadeStand class with three methods - make_lemonade, sell_lemonade, display_data.
    """

    def __init__(self):
        """ setup initial parameters. weather is randomized."""
        self.day = 0
        self.cash = 0
        self.lemonade = 0
        self.weather = random.randrange(50, 100)
        self.questions = 1
        self.first = 1

    def make_lemonade(self):
        """ Make lemonade to sell later. Cost to make lemonade changes each day."""

        try:
            key = random.choice(question_dict.keys())
            answer = int(raw_input(key))
            if answer == question_dict[key]:
                self.lemonade += 5
                print('\nCongratulations! You earned 5 cups of lemonade for helping your Neighbor!\n')
            else:
                print('Oh No, you were unable to help your neighbor and got no lemonade \n')
            del question_dict[key]
            self.first = 0
        except IndexError:
            print("All your neighbors have been helped, you cant get anymore lemonade \n")
            self.questions = 0

        
        

    def sell_lemonade(self):
        """ Sell lemonade that you have made previously. Bad weather and/or high price will discount net demand. """
        while True:
            try:
                price = int(raw_input('How many cents will you charge for a cup of lemonade? (0-100) '))
                if price in range(0, 101):
                    break
                else:
                    print('Please choose a number between 1 and 100')
                    continue
            except ValueError, e:
                print ('Please choose a number between 1 and 100.')
                continue
        cups = random.randrange(1, 101)  # without heat or price factors, will sell 1-100 cups per day
        price_factor = float(100 - price) / 100  # 10% less demand for each ten cent price increase
        heat_factor = 1 - (((100 - self.weather) * 2) / float(100))  # 20% less demand for each 10 degrees below 100
        if price == 0:
            self.lemonade = 0  # If you set price to zero, all your lemonade sells, for nothing.
            print('All of your lemonade sold for nothing because you set the price to zero.')
            self.day += 1
            self.weather = random.randrange(50, 100)
        demand = int(round(cups * price_factor * heat_factor))
        if demand > self.lemonade:
            print(
                'You only have ' + str(self.lemonade) + ' cups of lemonade, but there was demand for ' + str(
                    demand) + '.')
            demand = self.lemonade
        revenue = demand * round((float(price) / 100), 2)
        self.lemonade -= demand
        self.cash += revenue
        self.day += 1
        self.weather = random.randrange(50, 100)
        print('You sold ' + str(demand) + ' cup(s) of lemonade and earned $' + str(revenue) + ' dollars!\n')

    def display_data(self, name):
        """ Display all data for the lemonade stand."""
        if self.first:
            print('\nWelcome ' + name + '!\n')
        print('Day: ' + str(self.day))
        print('Weather: ' + str(self.weather))
        print('Cash: $' + str(self.cash))
        print('Lemonade: ' + str(self.lemonade))
        print('============================' + '\n')


def main():

    """ Create new LemonadeStand object and play game, or exit.
    """

    choice = ''
    while choice not in ['y', 'n']:
        choice = raw_input('Create a new lemonade stand? (y/n) ')
        if choice == 'y':
            name = raw_input('Hi friend. What is your name? ')
            stand = LemonadeStand()
            stand.display_data(name)
            while True:
                if stand.questions:
                    stand.make_lemonade()
                    stand.display_data(name)
                stand.sell_lemonade()
                stand.display_data(name)                  

        elif choice == 'n':
            print('Goodbye!')
            return


main()