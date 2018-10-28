def setup():
    #performing setup and creating pdf capture
    size(1500,800)
    add_library("pdf")
    beginRecord(PDF, "ddddd.pdf")
    
def draw():
    #intializing background and random seed
    background(255)
    randomSeed(10)
    
    #variables to play with
    randomness = 30
    linecount = 10000
    
    ellipsesize = 4
    
    #point initilization
    points = [random(100,width-50), random(100,height-50)]
    
    for i in range(linecount):
        #last points in list are referenced, random values added to create new x and y
        stroke(0)
        strokeWeight(0.5)
        z = random(randomness)
        x = points[-2]
        y = points[-1]
        x2 = x+random(-z,z)
        
        #recalculates random values if new point is too far off the screen
        while x2 > width-50 or x2 < 50:
            x2 = x+random(-z,z)
        y2 = y+random(-z,z)
        while y2 > height-50 or y2 < 50:
            y2 = y+random(-z,z)
        
        #line is drawn from last known point to new point, x2 and y2 are appended and white circle added on new point
        line(x,y,x2, y2)
        points.append(x2)
        points.append(y2)
        fill(255,255)
        noStroke()
        ellipse(x,y,ellipsesize,ellipsesize)
        
        #fill behavior changed to visible. 1/10 chance that that a circle of random size will be drawn near (x2, y2)
        stroke(0)
        fill(255,0)
        if int(random(10)) == 3:
            otherellipse = int(random(4))
            otherellipse2 = otherellipse + random(-1,1)
            ellipse(x+random(2),y+random(2), otherellipse, otherellipse2)
        
    #optionary line if you want the last point in the list to draw to the first point to complete the shape
    #line(points[0], points[1], points[-2], points[-1]) 
    
    #final circle added to last point)
    noStroke()
    ellipse(points[-2],points[-1], ellipsesize, ellipsesize)
    
    endRecord()
