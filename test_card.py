import random
from card import Carte


def random_card_Nbr():
    types = ["spade","heart", "diamond","club"]
    nums = [i for i in range(1,14)]
    t = random.choice(types)
    n = random.choice(nums)
    c = Carte(n,t)
   
    return [n,t]

