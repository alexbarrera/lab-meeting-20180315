#!/usr/bin/env python

# Define the class of vehicle Car
class Car:
    def __init__(self, doors=3, mpg=30):
        self.wheels = 4
        self.doors = doors
        self.mpg = mpg
        
    def cost(self, distance, galon_price=2.5):
        return "$%.2f" % (galon_price*distance/self.mpg)