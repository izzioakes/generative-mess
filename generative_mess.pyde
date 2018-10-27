def setup():
    size(1500,800)
    add_library("pdf")
    beginRecord(PDF, "ddddd.pdf")
    
def draw():
    background(255)
    randomSeed(10)
    
    randomness = 30
    linecount = 10000
    
    ellipsesize = 4
    
    points = [random(100,width-50), random(100,height-50)]
    
    for i in range(linecount):
        stroke(0)
        strokeWeight(0.5)
        z = random(randomness)
        x = points[-2]
        y = points[-1]
        x2 = x+random(-z,z)
        
        
        while x2 > width-50 or x2 < 50:
            x2 = x+random(-z,z)
        y2 = y+random(-z,z)
        while y2 > height-50 or y2 < 50:
            y2 = y+random(-z,z)
            
        line(x,y,x2, y2)
        points.append(x2)
        points.append(y2)
        fill(255,255)
        noStroke()
        ellipse(x,y,ellipsesize,ellipsesize)
        
    #line(points[0], points[1], points[-2], points[-1])
    noStroke()
    ellipse(points[-2],points[-1], ellipsesize, ellipsesize)
    
    endRecord()
