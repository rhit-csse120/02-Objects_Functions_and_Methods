"""
Demonstrates using (calling) STRING methods,
and using the DOT trick to discover them.

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


def main():
    """
    Tests the other functions in this module, by running them.
    """
    strings_1("help me Edgar")
    print("The above should have printed:")
    print("hZlp mZ Zdgar")
    print()

    strings_1("Ello, here be eeees and ZEEZEE.")
    print("The above should have printed:")
    print("Zllo, hZrZ bZ ZZZZs and zZZzZZ.")
    print()

    strings_1("abcdef ABCDEF")
    print("The above should have printed:")
    print("abcdZf abcdZf")
    print()

    strings_2("do THIS in title mode!")
    print("The above should have printed:")
    print("Do This In Title Mode!")
    print()

    strings_2("Hey xxx: who isxxx?")
    print("The above should have printed:")
    print("Hey Siri: Who Issiri?")
    print()

    strings_2("OK xx xxxx Sirixxxsiri.")
    print("The above should have printed:")
    print("Ok Xx Sirix Sirisirisiri.")
    print()


def strings_1(string):
    """
    Prints the given string, but with:
      -- All characters converted to lower case, and then
      -- Each occurrence of   e   replaced by   Z.
    For example:
      strings_1("help me Edgar")   prints   hZlp mZ
      strings_1("Hello, here be eeees.")   prints   HZllo, hZrZ bZ ZZZZs.
    Type hints:
      :type string: str
    """
    ###########################################################################
    # TODO: 2. Implement and test this function, per its doc-string above.
    #   Use the appropriate   string   methods to implement the function.
    #   Tests are already written for you in  main  above.
    #  _
    #   To discover the appropriate   string   methods, temporarily type
    #      "".
    #   (note the dot!) and use the so-called DOT TRICK, seeing what you find.
    ###########################################################################


def strings_2(string):
    """
    Prints the given string, but with:
      -- Each occurrence of   xxx   replaced by   Siri, and then
      -- The string printed in "title" mode.
    For example:
      strings_2("do THIS in title mode!")  prints  Do This In Title Mode!
      strings_2("Hey xxx: who isxxx?")   prints   Hey Siri: Who Issiri?
      strings_2("OK xx xxxx Sirixxxsiri.")   prints
          Ok Xx Sirix Sirisirisiri.
    Type hints:
      :type string: str
    """
    ###########################################################################
    # TODO: 3. Implement and test this function, per its doc-string above.
    #   Use the appropriate   string   methods to implement the function.
    #   Tests are already written for you in  main  above.
    #  _
    #   To discover the appropriate   string   methods, temporarily type
    #      "".
    #   (note the dot!) and use the so-called DOT TRICK, seeing what you find.
    ###########################################################################


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
