#Examples
speed=8
import random
import time
speed1=2
speed2=3
speed3=4
x1=50
x2=random.randint(100,450)
y2=-99
x3=random.randint(450, 900)
y3=-98
x4=random.randint(100, 450)
y4=-99
x5=random.randint(450, 900)
y5=-99
x6=random.randint(100, 450)
y6=-99
x7=random.randint(450, 900)
y7=-99
x8=random.randint(100, 450)
y8=-99
x9=random.randint(450, 900)
y9=-99
x10=random.randint(100, 450)
y10=-99
x11=random.randint(450, 900)
y11=-99
x12=random.randint(100, 450)
y12=-99
x13=random.randint(450, 900)
y13=-99
x14=random.randint(100, 450)
y14=-99
x15=random.randint(450, 900)
y15=-99
x16=random.randint(100, 450)
y16=-99
x17=random.randint(450, 900)
y17=-99
x18=random.randint(100, 450)
y18=-99
x19=random.randint(450, 900)
y19=-99
x20=random.randint(100, 450)
y20=-99
x21=random.randint(450, 900)
y21=-99
x22=random.randint(100, 450)
y22=-99
x23=random.randint(450, 900)
y23=-99
x24=random.randint(100, 450)
y24=-99
x25=random.randint(450, 900)
y25=-99
x26=random.randint(100, 450)
y26=-99
x27=random.randint(450, 900)
y27=-99
x28=random.randint(100, 450)
y28=-99
x29=random.randint(450, 900)
y29=-99
x30=random.randint(100, 450)
y30=-99
y0=-10000
speed0=1
speed01=10000

x50=0

def setup ():
    size(1000,1000)
    background(100)
def keyPressed():
    global x1

    
    #z:shadowraze 
    #x:shadowraze
    #c:shadowraze
    if key=='d':
        x1=x1+speed
    if key=='a':
        x1=x1-speed
    if y25>1000:
        if key=='r':                                                                                             
            exit()
    if key=='ESKAPE':
        exit(0)
    

    
def draw():
    global game_over,x1,y0,speed0
    y0=y0+speed0
    square(1,y0,1)
    background(175,224,230)
    fill(255,255,255)
    textSize(50)
    text("G   A   M   E  ", width/2-150, 100)
    textSize(30)
    circle(250,950,100)
    fill(230,177,187)
    square(500,300,100)
    fill(177,230,184)
    square(700,600,100)
    fill(177,187,230)
    square(100,500,100)
    fill(175,224,230)
    rect(width/2-175,150,340,100)
    fill(255,255,255)
    text("Press 'g' to play",width/2-125,200)
    
    
    
    
    
    
    
    
   
    
    if key=='g':
        speed0=speed01
    if y0>0:
        game_over=False
        if (game_over == False) :
            if x1 in xrange(50,950):
                background(102,102,102)
                noStroke()
                fill(255,255,255)
                circle(x1,950,100)
            global y2,y3,x3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25,y26,y27,y28,y29,y30
            y2=y2+speed1
            fill(255,255,255)
            text("Press 'Esc' to leave",10,100)
            noStroke()
            fill(255,255,255)
            textSize(50)
            text("First part  ", width/2-150, 100)
            fill(177,230,184)
            strokeWeight(3)
            stroke(255,255,255)
            square(x50,y2,100)
            if y2>150:
                y3=y3+speed1
                square(x3,y3,100)
                if y3>150:
                    y4=y4+speed1
                    square(x4,y4,100)
                    if y4>150:
                        y5=y5+speed1
                        square(x5,y5,100)
                        if y5>150:
                            y6=y6+speed1
                            square(x6,y6,100)
                            if y6>150:
                                y8=y8+speed1
                                square(x8,y8,100)
                                if y8>150:
                                    y9=y9+speed1
                                    square(x9,y9,100)
                                    if y9>150:
                                        y10=y10+speed1
                                        square(x10,y10,100)
                                        if y10>150: 
                                            fill(177,187,230)
                                            y11=y11+speed2 
                                            square(x11,y11,100)
                                            if y11>150:
                                                textSize(50)    
                                                strokeWeight(5)
                                                stroke(255,255,255)
                                                line(width/2-145,85,width/2+60,85)                                            
                                                textSize(50)
                                                fill(255,255,255)
                                                text("Second part  ", width/2-170, 200)
                                                strokeWeight(3)
                                                fill(255,255,255)                                        
                                                fill(177,187,230)
                                                y12=y12+speed2 
                                                square(x12,y12,100) 
                                                if y12>150: 
                                                    y13=y13+speed2 
                                                    square(x13,y13,100)
                                                    if y13>150: 
                                                        y14=y14+speed2 
                                                        square(x14,y14,100)
                                                        if y14>150: 
                                                            y15=y15+speed2 
                                                            square(x15,y15,100)
                                                            if y15>150: 
                                                                y16=y16+speed2 
                                                                square(x50,y16,100) 
                                                                if y16>150: 
                                                                    y17=y17+speed2 
                                                                    square(x17,y17,100) 
                                                                    if y17>150: 
                                                                        y18=y18+speed2 
                                                                        square(x18,y18,100) 
                                                                        if y18>150: 
                                                                            y19=y19+speed2 
                                                                            square(x19,y19,100) 
                                                                            if y19>150: 
                                                                                y20=y20+speed2 
                                                                                square(x20,y20,100) 
                                                                                if y20>150:
                                                                                    fill(230,177,187) 
                                                                                    y21=y21+speed3
                                                                                    textSize(50)    
                                                                                    strokeWeight(5)
                                                                                    stroke(255,255,255)
                                                                                    line(width/2-160,185,width/2+115,185)
                                                                                    square(x50,y21,100) 
                                                                                    if y21>150: 
                                                                                        textSize(50)
                                                                                        fill(255,255,255)
                                                                                        text("Third part  ", width/2-150, 300)
                                                                                       
                                                                                        fill(230,177,187)
                                                                                        y22=y22+speed3 
                                                                                        square(x22,y22,100) 
                                                                                        if y22>150: 
                                                                                            y23=y23+speed3 
                                                                                            square(x23,y23,100) 
                                                                                            if y23>150: 
                                                                                                y24=y24+speed3 
                                                                                                square(x24,y24,100) 
                                                                                                if y24>150: 
                                                                                                    y25=y25+speed3 
                                                                                                    square(x25,y25,100)
                                                                                                    if y25>150: 
                                                                                                        y26=y26+speed3 
                                                                                                        square(x26,y26,100)
                                                                                                        if y26>150: 
                                                                                                            y27=y27+speed3 
                                                                                                            square(x27,y27,100)
                                                                                                            if y27>150: 
                                                                                                                y28=y28+speed3 
                                                                                                                square(x28,y28,100)
                                                                                                                if y28>150: 
                                                                                                                    y29=y29+speed3 
                                                                                                                    square(x29,y29,100)
                                                                                                                    if y29>150: 
                                                                                                                        textSize(50)    
                                                                                                                        strokeWeight(5)
                                                                                                                        stroke(255,255,255)
                                                                                                                        line(width/2-145,285,width/2+90,285)
                                                                                                                        y30=y30+speed3 
                                                                                                                        square(x30,y30,100)
                                                                                                    
                                                                                                                        if y30>1000:
                                                                                                                            background(175,224,230)
                                                                                                                            textSize(60)
                                                                                                                            filter(BLUR, 5)
                                                                                                                            fill(255,255,255)         
                                                                                                                            stroke(255,255,255)
                                                                                                                            text("G   A   M   E       E  N   D", width/2-425, 300)
                                                                                                                            text("You win", width/2-350, 375)
                                                                                                                            fill(255,255,255)
                                                                                                                            stroke(200,200,200)
                                                                                                                            textSize(20)
                                                                                                                            text("Press 'r' to exit game", width/2-100, 325)
                                                                                                                            fill(237,204,17)
                                                                                                                            stroke(175,224,230)
                                                                                                                            
                                                                                                                            noLoop()                                                                                 
            noFill()
            stroke(201,177,230)
            rect(10,10,56,20)
            if y2>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(230,201,177)
                line(10,10,10,30)
            if y3>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(12,10,12,30)
            if y4>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(14,10,14,30)
            if y5>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(16,10,16,30)
            if y6>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(18,10,18,30)
            if y7>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(18,10,18,30)
            if y8>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(20,10,20,30)
            if y9>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(23,10,23,30)
            if y10>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(28,10,28,30)
            if y11>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(26,10,26,30)
            if y12>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(30,10,30,30)
            if y13>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(32,10,32,30)
            if y14>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(34,10,34,30)
            if y15>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(36,10,36,30)
            if y16>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(38,10,38,30)
            if y17>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(40,10,40,30)
            if y18>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(42,10,42,30)
            if y19>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(44,10,44,30)
            if y20>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(48,10,48,30)
            if y21>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(46,10,46,30)
            if y22>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(50,10,50,30)
            if y23>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(52,10,52,30)
            if y24>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(54,10,54,30)
            if y25>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(56,10,56,30)
            if y26>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(58,10,58,30)
            if y27>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(60,10,60,30)
            if y28>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(62,10,62,30)
            if y29>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(64,10,64,30)
            if y30>1000:
                strokeWeight(3)
                stroke(201,177,230)
                fill(0)
                line(66,10,66,30)
                
                
            
            fill(255,255,255)                                                                                               
            if y2 in range(800,1000):                            
                if x50 in range(x1-50,x1+50):
                    game_over =  True
            if y3 in range(800,1000):                            
                if x3 in range(x1-50,x1+50):
                    game_over =  True
            if y4 in range(800,1000):                            
                if x4 in range(x1-50,x1+50):
                    game_over =  True
            if y5 in range(800,1000):                            
                if x5 in range(x1-50,x1+50):
                    game_over =  True
            if y6 in range(800,1000):                            
                if x6 in range(x1-50,x1+50):
                    game_over =  True
            if y7 in range(800,1000):                            
                if x7 in range(x1-50,x1+50):
                    game_over =  True
            if y8 in range(800,1000):                            
                if x8 in range(x1-50,x1+50):
                    game_over =  True
            if y9 in range(800,1000):                            
                if x9 in range(x1-50,x1+50):
                    game_over =  True
            if y10 in range(800,1000):                            
                if x10 in range(x1-50,x1+50):
                    game_over =  True
            if y11 in range(800,1000):                            
                if x11 in range(x1-50,x1+50):
                    game_over =  True
            if y12 in range(800,1000):                            
                if x12 in range(x1-50,x1+50):
                    game_over =  True
            if y13 in range(800,1000):                            
                if x13 in range(x1-50,x1+50):
                    game_over =  True
            if y14 in range(800,1000):                            
                if x14 in range(x1-50,x1+50):
                    game_over =  True
            if y15 in range(800,1000):                            
                if x15 in range(x1-50,x1+50):
                    game_over =  True
            if y16 in range(800,1000):                            
                if x50 in range(x1-50,x1+50):
                    game_over =  True
            if y17 in range(800,1000):                            
                if x17 in range(x1-50,x1+50):
                    game_over =  True
            if y18 in range(800,1000):                            
                if x18 in range(x1-50,x1+50):
                    game_over =  True
            if y19 in range(800,1000):                            
                if x19 in range(x1-50,x1+50):
                    game_over =  True
            if y20 in range(800,1000):                            
                if x20 in range(x1-50,x1+50):
                    game_over =  True
            if y21 in range(800,1000):                            
                if x50 in range(x1-50,x1+50):
                    game_over =  True
            if y22 in range(800,1000):                            
                if x22 in range(x1-50,x1+50):
                    game_over =  True
            if y23 in range(800,1000):                            
                if x23 in range(x1-50,x1+50):
                    game_over =  True
            if y24 in range(800,1000):                            
                if x24 in range(x1-50,x1+50):
                    game_over =  True
            if y25 in range(800,1000):                            
                if x25 in range(x1-50,x1+50):
                    game_over =  True
            if y26 in range(800,1000):                            
                if x26 in range(x1-50,x1+50):
                    game_over =  True
            if y27 in range(800,1000):                            
                if x27 in range(x1-50,x1+50):
                    game_over =  True
            if y28 in range(800,1000):                            
                if x28 in range(x1-50,x1+50):
                    game_over =  True                                                                                                
            if y29 in range(800,1000):                            
                if x29 in range(x1-50,x1+50):
                    game_over =  True                                                                                                
            if y30 in range(800,1000):                            
                if x30 in range(x1-50,x1+50):
                    game_over =  True                                                                                                                                                                                                
            if  (game_over == True):
                textSize(60)
                filter(BLUR, 5)
                fill(255,255,255)         
                stroke(255,255,255)
                text("G   A   M   E       O   V   E   R", width/2-425, 300)
                fill(200,200,200)
                stroke(200,200,200)
                textSize(20)
                fill(0, 255, 127)
                text("Escape  to exit game.", width/2-100, 325)
                fill(0, 255, 127)
                stroke(237,204,17)
                filter(GRAY)
                noLoop()
    
        
            
            
            
    
                                                                                                
        
