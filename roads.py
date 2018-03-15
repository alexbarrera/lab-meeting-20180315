#!/usr/bin/env python

# Define the class of vehicle Car
class Road(object):
    def __init__(self, name, direction, length):
        self.name = name
        self.direction = direction
        self.length = length
        
    def description(self):
        return "%s goes %s for %d miles." % (self.name, self.direction, self.length)