"""
This module lets you experience the POWER of FUNCTIONS and PARAMETERS.

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
    Calls the other functions in this module to test and/or demonstrate them.
    """
    drawing_speed = 10  # Bigger numbers mean faster drawing
    window = rg.TurtleWindow()
    window.tracer(drawing_speed)

    # -------------------------------------------------------------------------
    # When the _TODO_s ask you to test YOUR code,
    # comment-out the following two statements and replace them
    # by calls to   better_draw_circles   et al as needed.
    # -------------------------------------------------------------------------
    draw_circles(rg.Point(100, 50))
    draw_circles(rg.Point(-200, 0))

    window.update()
    window.close_on_mouse_click()


###############################################################################
# TODO: 2.
#   First, RUN this program.  You will see that it draws concentric circles
#   whose radii vary by 15.
#  _
#   Next, READ:
#     -- main.
#          Note that it  constructs a TurtleWindow and then calls the function
#             draw_circles
#          twice, sending   draw_circles  one Point the first time
#          and another Point the second time.
#     -- The function  draw_circles  is defined immediately below this _TODO_.
#            Be sure that you understand its code!  Ask questions as needed!
#  _
#   After you have done the above, change the above _TODO_ to DONE
#   and continue to the next _TODO_ below.
###############################################################################
def draw_circles(point):
    """
    Constructs a SimpleTurtle, then uses the SimpleTurtle to draw 10 circles
    such that:
      -- Each is centered at the given Point, and
      -- They have radii:  15  30  45  60  75  ..., respectively.
    """
    turtle = rg.SimpleTurtle()

    # -------------------------------------------------------------------------
    # Draw circles centered at the given Point, by telling the SimpleTurtle to:
    #  Step 1: Go to the given Point and point east (towards the right).
    #  Step 2:
    #      a) Put the Pen up (so that movement does NOT draw anything).
    #      b) Go 15  pixels DOWN, ending up pointing east again.
    #      c) Put the Pen down (so that movement will cause drawing).
    #      d) Draw a circle with radius 15.
    #    Note: The circle will be centered at the given Point,
    #    because of the way that the SimpleTurtle  draw_circle  method works.
    #  Step 3: Repeat Step 2, but using 30 pixels instead of 15, in both places.
    #  Step 4: Repeat Step 2, but using 45 pixels instead of 15.
    #  Step 5: Repeat Step 2, but using 60 pixels instead of 15.
    #    etc.
    # -------------------------------------------------------------------------

    turtle.pen_up()
    turtle.go_to(point)
    turtle.set_heading(0)  # Point "east" (towards the right)

    for k in range(1, 11):  # k becomes 1, 2, 3, ... 10

        turtle.pen_up()

        # Go DOWN 15 pixels, ending up pointing east again
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)

        turtle.pen_down()
        turtle.draw_circle(15 * k)  # Radius 15, 30, 45, 60, ...


###############################################################################
# TODO: 3a.
#   The function
#       better_draw_circles
#   defined below this _TODO_ starts out exactly the same as the code for
#       draw_circles
#   that you read above.
#  _
#   Your job is to make
#       better_draw_circles
#   "better" than   draw_circles   by adding a PARAMETER for the amount
#   by which the radii of the concentric circles increase, as described below.
#  _
#   The new   better_draw_circles   function can do the same  thing as
#   the   draw_circles  function, but additionally allows for the radii to
#   vary by ANY desired amount.  Hence, the new version will be MORE POWERFUL.
#  _
#   So, modify the   better_draw_circles   function defined BELOW so that
#   it has TWO parameters:
#     -- the same Point parameter that it already has, and
#     -- a single ADDITIONAL parameter that is the amount by which the radii of
#   the circles increase.  For example, if that parameter is given the value 15,
#   then the circles should have radii:  15  30  45  60  75 ..., respectively,
#   just as in   draw_circles.  But if that parameter is given the value 3,
#   then the circles should have radii:  3  6  9  12  15  18 ..., respectively.
#
# TODO: 3b.
#   In   main  at the place indicated, comment-out the two existing calls
#   to  draw_circles  and add at least two calls to the improved
#   better_draw_circles  function, to TEST that your modified code is correct
#   and does indeed allow for different amounts by which the radii can vary.
###############################################################################
def better_draw_circles(point):
    """
    Starts out the same as the   draw_circles   function defined ABOVE.
    You will make it an IMPROVED, MORE POWERFUL function per the above _TODO_.
    """
    turtle = rg.SimpleTurtle()
    turtle.pen_up()
    turtle.go_to(point)
    turtle.set_heading(0)  # Point "east" (towards the right)

    for k in range(1, 11):  # k becomes 1, 2, 3, ... 10

        turtle.pen_up()

        # Go DOWN 15 pixels, ending up pointing east again
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)

        turtle.pen_down()
        turtle.draw_circle(15 * k)  # Radius 15, 30, 45, 60, ...


###############################################################################
# TODO: 4a.
#   In the previous _TODO_, you made a MORE POWERFUL version
#   of   draw_circles   by introducing an additional PARAMETER
#   for the amount by which the radii of the concentric circles increase.
#  _
#   In this _TODO_, you will implement a function called
#      even_better_draw_circles
#   that has FIVE parameters, for:
#     -- The center of the concentric circles (as it started with)
#     -- The amount by which the radii vary (as you did above)
#     -- The number of concentric circles drawn
#     -- The pen color to use for the concentric circles
#     -- The pen thickness to use for the concentric circles
#  _
#   Hence, this   even_better_draw_circles   function will be
#   even more POWERFUL than the previous functions,
#   in that it can draw LOTS of different kinds of circles.
#  _
#   Start by copy-and-pasting the code from   better_draw_circles  above
#   to the body of the   even_better_draw_circles   function defined below.
#   Then add parameters and modify the code to make them work!
#
# TODO: 4b.
#   In   main  at the place indicated, comment-out the existing calls
#   to  better_draw_circles  and add at least two calls to the improved
#   even_better_draw_circles  function, to TEST that your modified code is
#   correct and does indeed use its parameters per their descriptions above.
###############################################################################
def even_better_draw_circles(point):
    """An improved version of draw_circles, per the _TODO_ above."""
    # READ the above _TODO_
    # and then copy-paste code from better_draw_circles here:


###############################################################################
# TODO: 5.
#   Finally, comment-out the existing calls to  even_better_draw_circles  and
#   add code in   main  to draw various circles that form a BEAUTIFUL picture!
###############################################################################


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# This unusual form is necessary for the special testing we sometimes provide.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
