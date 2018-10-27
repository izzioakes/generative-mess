# generative-mess
generates out patterns of broken lines and small circles.

# About

hello! welcome to my first Processing.py code i'm putting up here.
the idea behind this code was to generate out a long line made up by many smaller lines back to back, every time moving in a random direction.

the code initializes random points, then adds random integers to them to create the next point. the line is drawn to this next point, and then the x and y values appended into the list to continue the process.
the lines are broken up by a white circle drawn at that point.
there is also a 1 in 5 chance a circle can be initialized near a point after it is drawn.

feel free to play with the randomness (which also equals the max line distance), line count, ellipse sizes and the random seed.
