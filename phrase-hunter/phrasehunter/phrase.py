# Create your Phrase class logic here.
class Phrase():
    """"""

    def __init__(self, aphrase):
        self.list_of_phrases = [aphrase.lower()]

    def add_to(self, aphrase):
        self.list_of_phrases.append(aphrase)



