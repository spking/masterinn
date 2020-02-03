# Skítakall - Classes Skrá #
# Sölvi Scheving Pálsson #
# 2. Febrúar 2020 #
import random
from termcolor import cprint


class Deck:
    def __init__(self, t, n):
        self.tegund = t
        self.numer = n

    def Skapastokk(self, t, listi):
        for x in range(1, 14):
            t1 = Deck(t, x)
            listi.append(t1)
        return listi

    def __str__(self):
        return self.tegund +" "+ str(self.numer)
