
# This is a separate, user-defined module that has been defined specifically for turtle graphics,
# which will be displayed at different times during the execution of the Hospital Project

#So that there is no confusion during testing:
# You can call the fucntions at the end to test them
# The try-except blocks have been added to some function definitions to handle some possible invalid inputs during excecution of the main program
# Therefore, some modules may not work here when they are called alone (in this program)
# E.g. - goodbye().......... will not give any output

#      - welcome()
#      - goodbye() ......... will give us goodbye()'s output after giving welcome()'s output

#They will work as intended in the main program

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#'time' module will be used to create delays 
import time
import turtle
turtle.bgcolor("black")

#Creates a blue, rectangular border
def border():          
    b = turtle.Turtle()
    b.hideturtle()

    b.pensize(12)
    b.speed(10)
    b.penup()
    b.pencolor("blue")
    b.goto(0,300)

    b.pendown()
    b.forward(450)
    b.right(90)
    b.forward(600)
    b.right(90)
    b.forward(900)
    b.right(90)
    b.forward(600)
    b.right(90)
    b.forward(450)

    
#Creates the Green Plus(+) Sign
def plus():       

    pen1 = turtle.Turtle() 
    pen1.hideturtle()

    #Selecting the color of the boundary of the plus sign
    pen1.pencolor("#006400")  
    pen1.pensize(5)
    pen1.speed(10)    
    
    #Selecting the color to be filled inside the plus sign
    pen1.fillcolor("#00FF00")
    
    #From here, everything that is drawn will be filled with a colour once end_fill() is called.
    pen1.begin_fill()
    
    for i in range(0,24,2):       
        
        if i % 2 == 0:
            pen1.forward(100)
            pen1.right(90)
        
        #Once it turns right by 90, it should turn around left into the opposite direction (180)
        if i % 3 == 0:        
            
            pen1.left(180)
            
        elif i % 2 != 0:
            pen1.forward(50)
            pen1.right(90)

    #Once this function executes, everything that has been drawn so far will be filled with the chosen colour.
    pen1.end_fill()   
    
    

#Prints the 'SilverHill Hospital' welcome text
def welcome_text():      
    
    pen2 = turtle.Turtle()  #WRITING
    pen2.hideturtle()

    pen2.penup()
    pen2.goto(-325,-50)
    pen2.pendown()
    pen2.pencolor('white')
    pen2.write("SilverHill" ,font=("Times New Roman",36,"italic"))

    pen2.penup()
    pen2.goto(-325,-105)
    pen2.pendown()
    pen2.write("Hospital" ,font=("Times New Roman",36,"italic"))

#This function combines the 3 fucntions defined above to create the actual welcome message    
def welcome():    
        
    
        try:
            s1 = turtle.Screen()
            
            border()
            plus()
            welcome_text()
            
            #There is a pause for 1.3 seconds where nothing happens
            time.sleep(1.3)    
            s1.bye()
                     
        except turtle.Terminator:
            pass
         

#This function has been used to create the loading screen
def loading():
    
    try:
        pen3 = turtle.Turtle()
    except turtle.Terminator:
            
            s2 = turtle.Screen()

            pen3 = turtle.Turtle()
            s2.bgcolor("black")
            pen3.hideturtle()
            
            #Calling The border() function which has been defined earlier
            border()                                                        
            
            pen3.goto(-150,0)
            pen3.pencolor("white")
            pen3.write("Loading",font=("Calibri",54,"italic"))

            pen3.penup()
            pen3.goto(135,20)
            
            # To print 3 Dots
            for i in range(3): 
                pen3.speed(25)
                pen3.pendown()
                pen3.pensize(8)
                 
                #Creates each Dot
                pen3.forward(2)  

                pen3.penup()
                pen3.forward(15)
            
            #There is a pause for 1.5s where nothing happens
            time.sleep(1.5)   
            pen3.goto(-150,-1)
            pen3.speed(1)
            pen3.pencolor("green")
            pen3.pensize(5)
            pen3.pendown()
            pen3.forward(325)
            
            s2.bye()


    
#This function has been used to create the goodbye message, which will be displayed before the main program terminates
def goodbye():             
    
    try:
            pen4 = turtle.Turtle()
    
    
    except:
                
            s3 = turtle.Screen()
            s3.bgcolor("black")
            pen4 = turtle.Turtle()
            pen4.hideturtle()
            
            #Calling The border() function which has been defined earlier
            border()      
            
            pen4.pencolor("white")
            
            pen4.penup()
            pen4.goto(-320,200)
            pen4.pendown()
            pen4.write("Thank You for Choosing SilverHill Hospital.",font=("Times New Roman",22,"italic","underline"))
            
            time.sleep(1.3)
            
            pen4.penup()
            pen4.goto(-200,0)
            pen4.pendown()
            pen4.write("Goodbye",font=("Times New Roman",54,"italic"))

            pen4.penup()
            pen4.goto(125,0)                 
            
            pen4.write(" :)",font=("Calibri",54,"italic"))
            
            #There is a pause for 1.5s where nothing happens
            time.sleep(1.5)        
            
            #For the Green Line
            pen4.goto(-200,-1)    
            pen4.speed(1)
            pen4.pencolor("green")
            pen4.pensize(5)
            pen4.pendown()
            pen4.forward(375)
            
            
            s3.bye()
