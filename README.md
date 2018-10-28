# generative-mess
generates out patterns of broken lines and small circles.

# About

hello! welcome to my first Processing.py code i'm putting up here.
the idea behind this code was to generate out a long line made up by many smaller lines back to back, every time moving in a random direction, and each connection between the lines the line would then be broken with small circles almost falling off. it was supposed to emulate a pile of debris falling.

the code initializes random points to begin, then adds random integers to them to create the next point. the line is drawn to this next point, and then the new x and y values are appended into the list to continue the process.
the lines are broken up by a white circle with no transparency or stroke drawn at that new point for iter.
there is also a 1 in 10 chance a visible circle can be initialized near a point after it is drawn.

feel free to play with the randomness (which also equals the max line distance), line count, ellipse sizes and the random seed.

# Examples

![alt text](https://mir-s3-cdn-cf.behance.net/project_modules/1400/0cbe5771890893.5bd4b5df114ea.png)

![alt text](https://mir-s3-cdn-cf.behance.net/project_modules/1400/85151571890893.5bd4b5df10fb3.png)
