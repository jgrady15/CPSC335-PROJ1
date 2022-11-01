import os
import tokenize
import tkinter
from unicodedata import decimal


class Card():
    def __init__(self, name) -> None:
        self.name = name
    
    def fee(self) -> decimal:
        self.name = self.name.lower()
        if(self.name == "amex"):
            return 1
        elif (self.name == "visa"):
            return 1.2
        else:
            return 0.7