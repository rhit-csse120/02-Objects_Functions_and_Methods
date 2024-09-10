"""
Practice DEFINING and CALLING
     FUNCTIONS

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

import rosegraphics as rg


def main():
    """
    TESTS the functions that you will write below.
    You write the tests per the _TODO_s below.
    """
    window = rg.TurtleWindow()
    # Put your TESTS immediately below this line, as directed by _TODO_s below.

    window.close_on_mouse_click()


###############################################################################
# TODO: 2a.  Define a function immediately below this _TODO_.
#   It takes two arguments that denote, for a right triangle,
#   the lengths of the two sides adjacent to its right angle,
#   and it returns the length of the hypotenuse of that triangle.
#     HINT: Apply the Pythagorean theorem.
#  _
#   You may name the function and its parameters whatever you wish,
#   but choose DESCRIPTIVE (self-documenting) names.
#
# TODO: 2b.  In main, CALL your function TWICE (with different values
#   for the arguments) and print the returned values,
#   to test whether you defined the function correctly.
###############################################################################


###############################################################################
# TODO: 3a.  Define a function immediately below this _TODO_.
#   It takes two arguments:
#     -- a string that represents a color (e.g. "red")
#     -- a positive integer that represents the thickness of a Pen.
#  _
#   The function should do the following (in the order listed):
#     a. Constructs two SimpleTurtle objects, where:
#          - one has a Pen whose color is "green" and has the GIVEN thickness
#          - the other has a Pen whose color is the GIVEN color
#              and whose thickness is 5
#  _
#        Note: the "GIVEN" color means the PARAMETER that represents a color.
#        Likewise, the "GIVEN" thickness means the PARAMETER for thickness.
#  _
#     b. Makes the first (green) SimpleTurtle move FORWARD 100 pixels.
#  _
#     c. Makes the other (thickness 5) SimpleTurtle move BACKWARD 100 pixels.
#  _
#   You may name the function and its parameters whatever you wish,
#   but choose DESCRIPTIVE (self-documenting) names.
#
# TODO: 3b.  In main, CALL your function at least TWICE (with different values
#   for the arguments) to test whether you defined the function correctly.
###############################################################################

###############################################################################
# TODO: 4.
#   As always, ensure that no blue bars on the scrollbar-thing to the right
#   remain.  If needed, run one more time to be sure that all is still OK.
#  _
#   Then COMMIT-and-PUSH your work as before:
#     1. Select    Git     from the menu bar (above).
#          Or, right-click on the project in the Project window
#          and select   Git  from the pull-down menu that appears.
#     2. Choose   Commit...   from the pull-down menu that appears.
#     3. In the   "Commit and Push"   sub-window that pops up
#        (the one in which you can type),
#        press the   "Commit and Push..."   button.
#            Note: If it asks you to "Specify commit message", do so
#                  using   Done   or something like that for the message.
#  _
#   You can COMMIT-and-PUSH as often as you like.
#   DO IT FREQUENTLY; AT LEAST once per module.
###############################################################################


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
