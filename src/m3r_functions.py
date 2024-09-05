"""
Exploration of CALLING FUNCTIONS.

Authors: David Mutchler, Rachel Krohn, Dave Fisher, Shawn Bohner, Sriram Mohan,
         Amanda Stouder, Vibha Alangar, Mark Hays, Dave Henthorn, Matt Boutell,
         Scott McClellan, Yiji Zhang, Mohammed Noureddine, Steve Chenoweth,
         Claude Anderson, Michael Wollowski, Chandan Rupakheti,
         Derek Whitley, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # TODO: If you got help from anyone on this module, list their names here.

###############################################################################
# TODO: 2. READ the code below. TRACE (by hand) the execution of the code,
#   predicting what will get printed.  Then run the code
#   and compare your prediction to what actually was printed.
#   Then mark this _TODO_ as DONE and commit-and-push your work.
###############################################################################


def main():
    hello("Snow White")
    goodbye("Bashful")
    hello("Grumpy")
    hello("Sleepy")
    hello_and_goodbye("Magic Mirror", "Cruel Queen")


def hello(friend):
    print("Hello,", friend, "- how are things?")


def goodbye(friend):
    print("Goodbye,", friend, "- see you later!")
    print("   Ciao!")
    print("   Bai bai!")


def hello_and_goodbye(person1, person2):
    hello(person1)
    goodbye(person2)


main()
