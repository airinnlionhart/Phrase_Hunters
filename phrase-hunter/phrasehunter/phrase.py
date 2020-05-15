# Create your Phrase class logic here.
import random
from character import *

class Phrase():
    """"""

    def __init__(self, aphrase):
        self.list_of_phrases = [aphrase]

    def add_to(self, aphrase):
        self.list_of_phrases.append(aphrase)


        g1 = Phrase("this is a test")
        g1.add_to("another test is in order")
