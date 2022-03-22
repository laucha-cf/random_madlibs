from sample_madlibs import code, hp, hungergames, zombie
import random

if __name__ == '__main__':
    ran_choice = random.choice( [hp, code, hungergames, zombie] )
    ran_choice.madlib()
