#NOTE:- 'silverhill_turtle.py' must be saved in the same folder as this program. It is a module that has to be imported into the program

#This is an old menu-based project I worked on in High School!

#This program allows a patient of SilverHill Hospital to
#	(1) Create an Account 
#	(2) Log into an Existing Account
#	(3) Book an Appointment with an available specialist upto 2 weeks in advance
#	(4) Delete Account
#	(5) Generate an Appointment Confirmation which can be saved onto the computer as a .txt file




#This Variable will be used for while loops when we validate user inputs
val = val2 = 0  

#This variable will be used to end the program if there are too many unsuccesful, continuous inputs
terminator = 0 

#This variable will be set to 'True' when the program gets Terminated
terminated = False 


import datetime
import sys


#This method will be called in any instance when the program needs to be ended
def terminate():



                    print("\n \n\t \t \t \t \t \t \t    We Wish You the Best of Health :)  The Program has been Terminated")

                    print("\n=====================================================================================================================================================================")

                    print(" \n  \t \t \t \t \t \t \t \t \t Silverhill Multispeciality Hospital",'', u"\u00A9")

                    print("\n======================================================================================================================================================================= ")
                    
                    #Here,'st' is an alias name of the silverhill_turtle module
                    st.goodbye()   
                    sys.exit()
                    


#This Function simply collects the user's personal info and returns it in a list.
#It does not return the Login ID and Password    
def info_collect():
    
    name = name_collect()
    DOB = dob_collect()
    gender = gender_collect()
    weight = weight_collect()
    height = height_collect()
    blood_group = blood_group_collect()
    no,emerg_name,emerg_no = emergency_collect()
    address = address_collect()
    
    data_list = [name,  age,  DOB,  gender,  weight,  height,  blood_group,  emerg_name,  emerg_no,  no,  address]
    
    return data_list
     
#This method takes the user's name as an input and performs validation checks on the input.     
def name_collect():
    
            global val, terminator,today,terminated
            global name,  age,  DOB,  gender,  weight,  height,  blood_group,  emerg_name,  emerg_no,  no,  address
            val = terminator = 0

            name=input("\n \t \t \t Full Name :")
            
            #Hyphens (-), Apostrophes (') and Whitespaces are also included in the set of acceptable characters for a name
            valid_characters = "-' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
            
            #Name Validation Check
            while(val == 0):   
                
                for i in name:
                    if i not in valid_characters:
                        name = input("\t \t \t Invalid. Please Enter a Valid Name (without digits and other special characters; name must contain atleast 1 character) : ")
                        terminator += 1
                        continue
                        
                        if terminator == 10:
                            print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                            terminate()
                            terminated = True
            
                if( name.isspace() or name.isdigit() or len(name) == 0 ):

                        name = input("\t \t \t Invalid. Please Enter a Valid Name (without digits and other special characters; name must contain atleast 1 character) : ")
                        terminator += 1
                        
                        if terminator == 10:
                            print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                            terminate()
                            terminated = True
             
                else:

                         val = 1

            #Resetting these variables so that they can be used again later
            val = terminator = 0   
            
            return name

#This method takes the user's date of birth as an input and performs validation checks on the inputs.
#The year, month and day are collected and validated seperately        
def dob_collect():
    
            val = terminator = 0
            import datetime
            global age
            
            #We store today's date in this variable
            today = datetime.date.today()       

            #We store the current year in this variable
            y = today.year                                 

            while(val == 0) :

                      try:

                          print("\n \t \t \t Hello Mr./Ms.",name,',',end=' ')

                          yob = int(input("What Year Were You Born In? (YYYY) :"))  #validation


                          #We need to check that the Year of birth is not greater than the current year.
                          if(yob>y or yob<1900):      

                                        print("\t \t \t\n The Year cannot be greater than",y,"or lesser than 1900.")
                                        terminator += 1
                                        if terminator == 10:
                                                                print("\t \t \t\nToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                                        

                          else:

                                        val = 1



                      except ValueError:

                                    print(" \t \t \t Note -  Input should not be an alphabet, decimal or empty space.")
                                    terminator += 1
                                    if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True

            
            #Resetting these variables so that they can be used again later
            val = terminator = 0


            #Calculating and storing the user's age so that it can be used later on
            age = y - int(yob)

                    

            print("\n \t \t \t  For Selection of Month : \n \t \t \t January -1 \n \t \t \t February -2 \n \t \t \t March - 3 \n \t \t \t April - 4 \n \t \t \t May - 5 \n \t \t \t June - 6 \n \t \t \t July - 7 \n \t \t \t August - 8 \n \t \t \t September - 9 \n \t \t \t October - 10 \n \t \t \t November  11 \n \t \t \t December - 12 \n ")

            while( val == 0 ):

                                    try:

                                        mob = int(input("\n \t \t \t Which Month? Please Make Your Choice (from 1 - 12) Accordingly (MM) :"))#(MM)

                                        if(mob<1 or mob>12):

                                                print("\t \t \t Invalid Entry, month entered must be between 1-12 : ")
                                                terminator += 1
                                                if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                                        else:

                                                val = 1

                                    except ValueError:

                                                print("Please Enter Numbers Only")
                                                terminator += 1
                                                if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True

            #Resetting these variables so that they can be used again later
            val = terminator = 0     
            
            #Validation Checks for Date
            while(val == 0): 

                                    try:

                                        dob = int(input("\n \t \t \t On What Date? (DD) : ")) #(DD)
                                        
                                        
                                        if(mob == 1 or mob == 3 or mob == 5 or mob == 7 or mob == 8 or mob == 10 or mob == 12): 

                                            if(dob<1 or dob>31):

                                                print("\t \t \t Date Entered must be between 1 and 31 :")
                                                terminator += 1
                                                if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                                            else:

                                                val = 1



                                        elif(mob ==  4 or mob == 6 or mob == 9 or mob == 11):  #mob is month of birth

                                            if(dob<1 or dob>30):

                                                print("\t \t \t Date Entered must be between 1 and 30 :")
                                                terminator += 1
                                                if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                                            else:

                                                 val = 1



                                        elif(mob == 2):   #If the Month is February



                                            if(yob % 4 == 0):    #Checking whether it is a leap year or not



                                                if(dob<1 or dob>29):

                                                    print("\t \t \t Date Entered must be between 1 and 29")
                                                    terminator += 1
                                                    if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                                                else:

                                                     val = 1



                                            elif(yob % 4 != 0 ):



                                                if(dob<1 or dob>28):

                                                    print("\t \t \t Date Entered must be between 1 and 28")
                                                    terminator += 1
                                                    if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                                                else:

                                                    val = 1

                                    except ValueError:

                                            print("\n \t \t \t Date May be Invalid, Please Re-enter")
                                            terminator += 1
                                            if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True

            #Resetting these variables so that they can be used again later
            val = terminator =  0

            import datetime

            #Combining the three inputs together into a datetime.date format
            DOB = datetime.date(yob,mob,dob)
            
            return DOB 
         

#This method takes the user's gender as an input and performs validation checks on the inputs.                    
def gender_collect():
    
            val = terminator = 0
    
            gender = input("\n \t \t \t Gender (Please Enter 'M' or 'Male' for MALE, 'F' or 'Female' for FEMALE or 'O' or 'Other' for OTHER): ")

            #Gender Validation Check
            while(val == 0):                                                         

                   if(gender.isdigit() or gender.isspace() or len(gender) == 0): 

                                    gender = input("\t \t \t\n Invalid Input, Please Enter 'M' or 'Male' for MALE, 'F' or 'Female' for FEMALE or 'O' or 'Other' for OTHER; \n \t \t \t Please Re-Enter Gender:")



                   elif(gender.lower() in  ['f','female']):

                                     gender = 'Female'

                                     val = 1

                         

                   elif(gender.lower() in ['o','other']):

                                     gender = 'Other'

                                     val = 1



                   elif(gender.lower() in ['m','male']):

                                     gender = 'Male' 

                                     val = 1



                   else:

                                gender = input("\n \t \t \t\n Invalid Input! Please Enter 'M' or 'Male' for MALE, 'F' or 'Female' for FEMALE or 'O' or 'Other' for OTHER; \n \t \t \t Please Re-Enter Gender:")
                                terminator += 1
                                if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True

            #Resetting these variables so that they can be used again later
            val = terminator = 0
            
            return gender

#This method takes the user's bodyweight as an input and performs validation checks on the inputs.
def weight_collect():
    
            val = terminator = 0
            weight = input("\n \t \t \t Weight (in kg) : ") #Weight Validation Check



            while(val == 0):

                if(weight.isalpha() or weight.isspace() or len(weight) == 0): 

                    weight = input(' \t \t \t\n Invalid Entry. Please Re-Enter Your Weight (in kg):')
                    terminator += 1
                    if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                elif(float(weight)<0.0):

                    weight = input ("\t \t \t Weight Must Not Be Negative")
                    terminator += 1
                    if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                else:

                    val = 1

            
            val = terminator = 0

            weight = float(weight)
            
            return weight

#This method takes the user's Height as an input and performs validation checks on the inputs.
def height_collect():
    
            val = terminator = 0
            height = input("\n \t \t \t Height (in cm) : ")

            #Height Validation Checks
            while (val == 0): 

                if(height.isalpha() or height.isspace() or len(height) == 0): 

                    height = input(' \t \t \t Invalid Entry. Please Re-Enter Your Height (in cm):')
                    terminator += 1
                    if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                elif(float(height)<0.0):

                    height = input(" \t \t \t Height must not be negative value : ")
                    terminator += 1
                    if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                else:

                    val = 1

            val = terminator = 0        

        

            height = float(height)
            
            return height

            
#This method takes the user's blood group as an input and performs validation checks on the input.
def blood_group_collect():        
            val = terminator = 0
            print("\n \t \t \t Enter Your Blood Group According to the List Below:")

            print("""\n\t\t \t  1  - AB+

        \t \t \t  2 -  AB-

        \t \t \t  3 -  A+

        \t \t \t  4 -  A-

        \t \t \t  5. - B+

        \t \t \t  6. - B-

        \t \t \t  7. - O+
    
        \t \t \t  8. - O-""")

            while(val == 0):

                              try:

                                    blood_groupCH = int(input("\n \t \t \t Enter Your Blood Group (choose from 1 - 8) Accordingly : "))

                                    if(blood_groupCH<1 or blood_groupCH>8):

                                        print("\n \t \t \t  Entry may be Invalid. Please Re-enter the Blood Group : ")
                                        terminator += 1
                                        if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                                    else:

                                        val = 1

                              except ValueError:

                                                      print("Please Enter Numbers Only")
                                                      terminator += 1
                                                      if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                                



            val = terminator =  0



            if(blood_groupCH == 1):

                blood_group = 'AB+'

            elif(blood_groupCH == 2):

                blood_group = 'AB-'

            elif(blood_groupCH == 3):

                blood_group = 'A+'

            elif(blood_groupCH == 4):

                blood_group = 'A-'

            elif(blood_groupCH == 5):

                blood_group = 'B+'

            elif(blood_groupCH == 6):

                blood_group = 'B-'

            elif(blood_groupCH == 7):

                blood_group = 'O+'

            elif(blood_groupCH == 8):

                blood_group = 'O-'
                
            return blood_group

                

#This method takes the user's emergency contact info as an input and performs validation checks on the inputs.                
def emergency_collect():
    
            val = terminator = 0
            print("\n \t \t \t Would you like to provide an Emergency Contact? ")

            print("\n \t \t \t \t \t 1 - 'Yes, I Would Like to Provide an Emergency Contact'")

            print("\n \t \t \t \t \t 2 - 'No, I Do Not Want to Provide an Emergency Contact'")



            ch3 = input("\n \t \t \t Please Enter 1 or 2 Accordingly :")


            #Validating the choice entry
            while(val == 0):  

               if(ch3.isalpha() or ch3.isspace() or len(ch3) == 0):

                    ch3 = input("\t \t \t Invalid Entry, Please Re-Enter: ")
                    terminator += 1
                    if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                    

               elif(int(ch3) != 1 and int(ch3) != 2):

                      ch3 = input("\t \t \t Invalid Entry, Please Re-Enter ('1' OR '2' ONLY):")
                      terminator += 1
                      if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


               else:

                    val = 1

            val = terminator = 0

            ch3 = int(ch3)



     

            
            #To Take NAME of Emergency Contact
            if(ch3 == 1): 

                emerg_name = input("\n \t \t \t Enter The NAME OF YOUR EMERGENCY CONTACT : ")
                terminator += 1
                if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                while(val == 0):
                            
                        valid_characters= "' -abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        
                        for i in emerg_name:
                            if i not in valid_characters:
                                emerg_name = input(" \t \t \t Invalid Entry. Please Re - Enter the NAME OF YOUR EMERGENCY CONTACT : ")
                                terminator += 1
                                continue
                                if terminator == 10:
                                    
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                                

                        if(emerg_name.isdigit() or emerg_name.isspace() or len(emerg_name) == 0):
                
                            emerg_name = input(" \t \t \t Invalid Entry. Please Re - Enter the NAME OF YOUR EMERGENCY CONTACT : ")
                            terminator += 1
                            if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                        else:

                            val = 1

            val = terminator =  0

            
            #To Take Emergency Contact NUMBER
            if(ch3 == 1): 
                        while(val == 0):

                                try:

                                      emerg_no = int(input("\n \t \t \t Enter The EMERGENCY CONTACT NUMBER :  +91 "))  # Emergency Contact



                                      if( (len(str(emerg_no))) != 10):

                                          print("\n \t \t \t Please Re-enter your EMERGENCY CONTACT NUMBER. It must be 10-Digits")
                                          terminator += 1
                                          if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                                      else:

                                          val = 1
                                          break



                                except ValueError:

                                        print("\n \t \t \t Emergency Contact Information is Invalid.")
                                        terminator += 1
                                        if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True




            val = terminator = 0                                   

                                                

           
            #To Take and Validate Account Holder's Contact Number
            while(val == 0):  

                    try:
                             #If they have chosen not to enter an emergency contact
                             if(ch3 == 2):   

                                emerg_name = 'NULL'

                                emerg_no = 'NULL'



                             if((ch3 == 1) or (ch3 ==  2)):

                                     
                                     if((ch3 == 1) or (ch3 ==  2)):
                                  

                                         no = int(input("\n \t \t \t Please Enter YOUR OWN CONTACT NUMBER : +91 "))
                                     
                                         if no  ==  emerg_no:
                                             print("\n\t \t \tEmergency contact and main contact number cannot be the same!")
                                             continue
                                        
                                         elif( (len(str(no))) != 10 or len(str(no)) == 0):

                                             print("\n \t \t \t Please Re-enter YOUR OWN CONTACT NUMBER. It must be 10-digits!")
                                             terminator += 1
                                             if terminator == 10:
                                                                    print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                    terminate()
                                                                    terminated = True


                                         else:

                                                     val = 1

                    except ValueError:

                                 print("\n \t \t \t Your Contact Information is Invalid")
                                 terminator += 1
                                 if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True




            val = terminator = 0
            return [no,emerg_name,emerg_no]

#This method takes the user's emergency contact info as an input and performs validation checks on the inputs.
def address_collect():
            
            val = terminator = 0
            address = input("\n \t \t \t Please Enter Your Residence Address (Separate using commas, press 'enter' key when done) : ")
            
            #Address ValidationCheck
            while(val == 0):
                
                #Hyphens (-), Apostrophes ('), Hashtags (#) and Whitespaces are included in the set of acceptable characters for an address
                valid_characters = "#/-' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
                
                for i in address:
                    if i not in valid_characters:
                          address = input("\t \t \t Address May be Invalid. Please re-enter : ")
                          continue
                          terminator += 1
                          if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True
                                                                
                if(address.isdigit() or address.isspace() or len(address) == 0):

                          address = input("\t \t \t Address May be Invalid. Please re-enter : ")
                          terminator += 1
                          if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                else:

                        val = 1

            val = terminator =  0

           
            return address


#This method uses the random module to generate a unique six-digit ID for a new user
def id_generator():

            import random
            import mysql.connector as sql
            connection = sql.connect(host = "localhost", user = "root", password = "tiger", database = "silverhill_hospital", autocommit = True)
            cursor = connection.cursor()

            cursor.execute("select Login_ID from patients;")
            ids = cursor.fetchall()
            val = 0
            while (val == 0):

                random_login = random.randrange(100000,1000000)     #Generating a 6-DIGIT ID
                
                #Ensuring that the ID doesn't already exist in our Database
                if tuple( [random_login] ) not in ids:    
                    log_id = random_login
                    val = 1
                else:
                    val = 0
                    continue

            print("\n\n\n\n\t \t \t YOUR LOGIN ID IS:", log_id)

            print("\n\t \t \t Please Do Make a Note of it!\n\n")

            return log_id


#This function will be used to Sign Up the user after they have entered their personal information
#It assigns a login_id as well as password to the user, and makes an entry in the database
def sign_up(user_data):

            global val, terminator,terminated
            val = terminator = 0
            global log_id, log_pwd, name,  age,  DOB,  gender,  weight,  height,  blood_group,  emerg_name,  emerg_no,  no,  address                                                                                                             # into the patients table.
            
            name,  age,  DOB,  gender,  weight,  height,  blood_group,  emerg_name,  emerg_no,  no,  address    =    user_data #Unpacking

            #The id_generator() function will randomly generate a unique six-digit ID number
            log_id = id_generator() 
            

            while (val == 0):
                
                print("\t \t \t Please Set a Password For Your Account.")
                print("\t \t \t We'd recommend using numbers and special characters for a good, strong password")

                print("""\n\t \t \t NOTE - It cannot be longer than 20 Characters

                                         - It has to be ATLEAST 8 characters long""")

                log_pwd = input("\t \t \t Your Password:")



                if ( len(log_pwd) == 0 or len(log_pwd)<8 or len(log_pwd) > 20 ) :

                    print("\n\t \t \t Please Enter the correct number of digits!")
                    terminator += 1
                    if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True




                else:

                    log_pwd2 = input("\t \t \t Confirm Password:")



                    if log_pwd2 != log_pwd:

                        print("\t \t \t Passwords Do Not Match!\n")
                        terminator += 1
                        if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True


                    else:

                        val = 1

            val = terminator = 0


            #We don't require this anymore
            del log_pwd2  



            print(f"\n\n\t \t \t Password for ID: {log_id},  NAME: {name} has been set succesfully.")

            print("\t \t \t PLEASE NEVER SHARE YOUR PASSWORD WITH ANYONE. WE WILL NEVER ASK YOU FOR IT. BEWARE OF SCAMMERS!")

             

            import mysql.connector as sql

            while (val == 0):

              

                        connection = sql.connect(host = "localhost", user = "root", password = "tiger", database = "silverhill_hospital", autocommit = True)

                        cursor = connection.cursor()



                        if connection.is_connected():

                            print("\n\t \t \t Connected Succesfully")

                            cursor.execute(f"insert into patients values( {log_id}, '{log_pwd}', '{name}', {age}, '{DOB}', '{gender}', {weight}, {height}, '{blood_group}',  '{emerg_name}', {emerg_no}, {no}, '{address}' );")

                            val = 1



                            connection.close()          

              

                        else:
                            print("\n\t \t \t Connection Unsuccesful. Please Try Again. \n\t \t \t If the issue persisits, try restarting the program.")

                            sign_up(user_data) #So that we can take the data again



            val = 0

            print("\t \t \t Data Entry Completed")

            print(f"\n\n\n\t \t \t You are now Signed-in as {name}, Your Login ID: {log_id}")

            val = 1


#This Function will verify the user's Login ID
def sign_in1(log_id): 

    global name,  age,  DOB,  gender,  weight,  height,  blood_group,  emerg_name,  emerg_no,  no,  address   #These variables have to be available for use in case the person signs in directly
    
    import mysql.connector as sql

    connection = sql.connect(host = 'localhost', user = 'root', database = 'silverhill_hospital', password = 'tiger')

    cursor = connection.cursor()

    cursor.execute("select name, age, DOB, gender, weight, height, Blood_Group, Emergency_Contact, Emergency_Contact_Number, Patient_Contact_Number, address from patients ; ")
    alldata = cursor.fetchall()
    alldata = alldata[0]
    name,  age,  DOB,  gender,  weight,  height,  blood_group,  emerg_name,  emerg_no,  no,  address = alldata    #Unpacking
        

    val = terminator = 0
    
    #For Validation
    while(val == 0): 
        
        
            cursor.execute("select Login_ID from patients;")

            data = cursor.fetchall()



            for row in data:



                 if tuple( [log_id] ) == row:

                     print("\t \t \tMatch Found")
                     

                     connection.close()

                     return True

                     val = 1

            else:
    
                  
                   return False
                   val = 1
                


        

    val = 0

  
#This Function will verify the user's password    
def sign_in2(log_id):         

                    global val,terminator,terminated
                    val = terminator = 0
                    print("\n\t \t \t Now we'll need your password. Don't worry, It's Safe to enter it here! \n\t \t \t \n\t \t \tNOTE - Do not Disclose this password Elsewhere")

                    while (val == 0):



                            log_pwd = input("\n\t \t \t Enter your password:")

                            if ( len(log_pwd) == 0 or len(log_pwd)<8 or len(log_pwd) > 20 ) :

                                print("\t \t \t Please Enter the correct password!")
                                terminator += 1
                                if terminator == 10:
                                                            print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                            terminate()
                                                            terminated = True

                                print("""\n\t \t \t NOTE - It cannot be longer than 20 Characters

                                                                         - It has to be ATLEAST 8 characters long""")

                                

                            else:

                                log_pwd = tuple( [log_pwd] )

                                import mysql.connector as sql

                                connection = sql.connect(host = 'localhost', user = 'root', database = 'silverhill_hospital', password = 'tiger')

                                cursor = connection.cursor()



                                cursor.execute(f"select pwd from patients where Login_ID = {log_id} ;")         #Retrieving password that matches with ID

                                pwd = cursor.fetchone()

                                



                                if pwd == log_pwd:

                                    return True

                                

                                else:

                                    return False

                            terminator = 0


#This method is called when the user wants to book an appointment with a Doctor                            
def appointment(field,today):    

              global  val,val2,terminator,terminated
              val = val2 = terminator = 0
              print("\n \t \t \t How many days from today would you like to book an appointment?")
              print("\n\t \t \t KINDLY NOTE - If you have to make an appointment for today, \n\t \t \t Please close the program and call the hospital reception at 080-2345-2113")
              print("\t \t \t This Program cannot book appointments immediately, for the same day.")
              print("\t \t \t This Program will not let you book an appointment more than 14 days in advance i.e. You can only book an appointment for the next 14 days")

              while (val == 0):
                  try:
                      
                          app_days = int(input("\n\t \t \t Enter the number of days (from today) after which you want to make an appointment:"))

                          if app_days < 1 or app_days >14:
                              print("\t \t \t Please enter within the specified limit!")
                              print("\n\t \t \t This Program cannot book appointments immediately, for the same day.")
                              print("\t \t \t This Program will not let you book an appointment more than 14 days in advance")
                              terminator += 1
                              if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True
                          else:
                              val = 1
                  except ValueError:
                           print("Enter Only Numbers please!")
                           terminator += 1
                           if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True
              val = terminator= 0
              
              import datetime
              
              #This will create a 'timedelta' (i.e. time difference) object which will be used to set the appointment date
              time_difference = datetime.timedelta(days = app_days)    
              app_date = today +  time_difference
              app_month = app_date.month
                 
              print(f"\n\t \t \t Alright! Your Appointment will be made for {app_date} (YYYY/MM/DD)")

              

              import mysql.connector as sql
              connection = sql.connect(host = 'localhost', user = 'root', database = 'silverhill_hospital', password = 'tiger', autocommit=True)
              cur= connection.cursor()
              
              print(f"\n \t \t \t You have selected {field}. The specialists in this field are as given below:")
              print("\n \n \n \n")
              print("\t\t\t ID \t \t Name \t \t \t Age \t \t Specialisation \t \t Gender")
              print("\t\t\t -----------------------------------------------------------------------------------------------")
              
              cur.execute(f"Select ID,name,age,dept,gender from doctors where dept like '{field}';")
              doc_data = cur.fetchall()
              for i in doc_data:
                   print("\t \t \t ",end='')   #For Aligning the Output
                   print(*i, sep='\t \t ')
              val = val2 = 0
              cur.execute (f" select ID from doctors where dept = '{field}' ; ")
              id1 = cur.fetchone() #To get ID of first doctor in this field
              id1 = id1[0]
              id2 = cur.fetchone() #To get ID of second Doctor in this field
              id2 = id2[0]
              
              while(val == 0):

                 while (val2 == 0):
                     #This is inside the Inner Loop (val2 == 0)
                      try:
                                  select=int(input("\n \t \t \tPlease select the Doctor you would Like to Book an Appointment with, based on their ID: "))
                                  if (select != id1) and (select !=  id2):              #If the ID entered deos not correspond with that of the doctors in this field
                                          print("\t \t \t Please make an appropriate entry!")
                                          terminator += 1
                                          if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True
                                  else:
                                          val2 = 1
                          
                      except ValueError:
                                  print("\n\t \t \t Please Enter Numbers only!")
                                  terminator += 1
                                  if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True
                
                 val2  = terminator = 0

                #This is inside the Outer Loop (val == 0)

                 cur.execute(f"select id,name,off_day from doctors where ID like {select};")
                 doc_data=cur.fetchall()
                 doc_id = doc_data[0][0] #Since it will be a Tuple within a List
                 doc_name = doc_data[0][1] #Since it will be a Tuple within a List
                 off_digit = doc_data[0][2] #Since it will be a Tuple within a List

                 
                 if off_digit == 6:             

                          if app_month <= 6:  #January to June
                              status = True
                          elif app_month > 6: #July to December
                              status = False

                 elif off_digit == 12:

                         if app_month <= 6:  #January to June
                              status = False
                         elif app_month > 6: #July to December
                              status = True

                 #If the Doctor is available for the desired appointment time, it can break out of both loops
                 if status:          
                    val2 = 1 
                    val = 1
                    
                 #If the Doctor is unavailable, loop has to reset so that input can be taken again   
                 else:               

                    val = 0
                    while(val == 0):
                                
                            print("\n\t \t \t We are very sorry, The Doctor won't be available at this time. Please Try Selecting the other Doctor.")
                            option_app_dr = int(input("\n\t \t \t If you would like to try again press '1' or to quit Press '2'."))

                            if option_app_dr == 1:
                                                    val3 = 1
                                                    val2 = 0
                                                    val =  0
                                                    break
                            elif option_app_dr == 2:
                                                    terminate()
                                                    terminated = True
                            elif option_app_dr != 2 and option_app_dr !=2:
                                                    print("\n\t \t \t Please Enter a Valid Input!")
                                                    terminator += 1
                                                    if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True
                                                    continue
                    if option_app_dr == 1:
                        continue
                    
                  

                      

                 print(f'\t \t \t {doc_name} will be available at the following times \n ')
                 print('\t \t \t 1 -  9:45 a.m.')                   
                 print('\t \t \t 2 - 11:15 a.m.')
                 print('\t \t \t 3 - 12:30 p.m.')
                 print('\t \t \t 4 - 3:00 p.m.')
                 print('\t \t \t 5 - 4:15 p.m.')
                 print('\t \t \t 6 - 5:15 p.m.')

                 print("\t \t \t At What Time Would You Like To Book Your Appointment?  ")
                 print("\t \t \t For E.g. - If you would like to book at 3:00 p.m. , Enter 4, For 11:15 a.m. enter 2 " )
                 option_app_time = input("\n\t\t\t Please Make a Choice (from 1 to 6) as per the list above : ")
                 
                 val6 = terminator = 0
                 
                 #Validation
                 while val6 == 0 : 

                                     if (( option_app_time.isalpha() )or (option_app_time.isspace() ) or (len(option_app_time) ) == 0 ):  
                                                     option_app_time = input("\t \t \t Invalid Entry, Please Choose Again : ")
                                                     terminator += 1
                                                     if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True
                                       
                                     elif(int(option_app_time)<1 or int(option_app_time)>6):
                                                     option_app_time = input ("\t \t \t Please Enter a Number Between 1-6 Only")
                                                     terminator += 1
                                                     if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True

                                     else:
                                         break
                 val6 = terminator = 0
                                                     

                 option_app_time = int(option_app_time)

                 if(option_app_time == 1):
                                         app_time = datetime.time(9,45,0) #HH:MM:SS
                 elif(option_app_time == 2):
                                         app_time = datetime.time(11,15,0)
                 elif(option_app_time == 3):
                                         app_time = datetime.time(12,30,0)
                 elif(option_app_time == 4):
                                         app_time = datetime.time(15,0,0)
                 elif(option_app_time== 5):
                                         app_time = datetime.time(16,15,0)
                 elif(option_app_time == 6):
                                         app_time = datetime.time(17,15,0)

                 app_data_ret = [doc_id,doc_name,field,app_date,app_time]
                 return app_data_ret

                            


import silverhill_turtle as st

#this method displays a welcome turtle graphic message when the program is executed
st.welcome()





print("=========================================================================================================================================================================== \n ")

print("""
\t\t\t\t┏━━┓┏━━┓┏┓╋┏┓╋┏┓┏━┓┏━┓┏┓┏┓┏━━┓┏┓╋┏┓
\t\t\t\t┃━━┫┗┃┃┛┃┃╋┃┗┳┛┃┃┳┛┃╋┃┃┗┛┃┗┃┃┛┃┃╋┃┃
\t\t\t\t┣━━┃┏┃┃┓┃┗┓┗┓┃┏┛┃┻┓┃┓┫┃┏┓┃┏┃┃┓┃┗┓┃┗┓
\t\t\t\t┗━━┛┗━━┛┗━┛╋┗━┛╋┗━┛┗┻┛┗┛┗┛┗━━┛┗━┛┗━┛
\t\t\t\t┏┓┏┓┏━┓┏━━┓┏━┓┏━━┓┏━━┓┏━━┓┏┓
\t\t\t\t┃┗┛┃┃┃┃┃━━┫┃╋┃┗┃┃┛┗┓┏┛┃┏┓┃┃┃
\t\t\t\t┃┏┓┃┃┃┃┣━━┃┃┏┛┏┃┃┓╋┃┃╋┃┣┫┃┃┗┓
\t\t\t\t┗┛┗┛┗━┛┗━━┛┗┛╋┗━━┛╋┗┛╋┗┛┗┛┗━┛
""")
print("\n =========================================================================================================================================================================== ")










print("\n\n\n  \t \t \t Silverhill Healthcare Limited is a leading integrated healthcare delivery service provider in India." + "\n" + "  \t \t \t The healthcare verticals of the company primarily comprise hospitals, diagnostics and day care specialty facilities.") 

print("  \t \t \t Currently, the company operates its healthcare delivery services mainly in India.") 

print("  \t \t \t The Silverhill brand is a synthesis of human values of trust, ethics and service and quality healthcare.") 

print("  \t \t \t Transparency in actions & high level of integrity and excellence are the values we strive to uphold.") 

print("  \t \t \t Our Mission is to be a globally respected healthcare organisation known for" + "\n" + "  \t \t \t Clinical Excellence and Distinctive Patient Care.") 

print("  \t \t \t We try to project this clinical excellence, distinctive patient care," + "\n" + "   \t \t \t human values of trust, ethics and service and quality healthcare.") 

print("\n" + "\n" + "  \t \t \t This is a Portal Through Which You can choose to book an appointment with one of our many specialists in numerous fields.")



print("\n\n\n\n")

ent = 0



        

while (val == 0):   

                acc = input("""\n\t \t \t Do You have an Account with SilverHill Hospital?

        \t \t \t Please enter 'Yes' if You do.

        \t \t \t If you do not, Please enter 'No' and we'll get you signed up in no time!

        \t \t \t If You'd like to exit, please enter 'quit'



        \t \t \t Please Enter:""")



                if acc.lower() in ['y','yes']:

                    val = 1

                    log = 1 

                    print("\n\n\t \t \t Welcome Back! We would like to assist you as fast as possible.")



                elif acc.lower() in ['no','n']:
    
                    log = 2 

                    print("\n \t \t  \t Would you like to Sign-Up or Quit?")

                    print("\n\t \t \t  NOTE- To operate on this applet further, you require an account.")

                    val = 1



                elif acc.lower() in ['quit','q','exit'] :

                    terminate()
                    terminated = True

                elif acc.isdigit() or acc.isspace() or len(acc) == 0:

                    print("\n\t \t \t Something Went wrong! Please try entering your data in the right format \n \n ")
                    terminator += 1
                    if terminator == 10:
                                                            print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                            terminate()
                                                            terminated = True
                else:
                  print("\n\t \t \t Something Went wrong! Please try entering your data in the right format \n \n ")
                  terminator += 1
                  if terminator == 10:
                                                            print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                            terminate()
                                                            terminated = True


val = terminator = 0

       

while (val == 0):


            if log == 1:


                try:

                        log_id = int(input("\t \t \t Please Enter your Login ID (Provided to you during sign-up):"))
                        print("\n\t\t\t If you have Forgotten your Login ID or Password \n\t\t\tsend an SMS 'RECOVERY' to +91 9432614891 or send an e-mail to silverhill_recovery@gmail.com and await further instructions")

                        if (len(str(log_id)) != 6):

                            print("\t \t \t Your ID has to be Exactly 6 Digits! Try Again:")
                            terminator += 1
                            if terminator == 10:
                                                            print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                            terminate()
                                                            terminated = True

                            continue

                        else:
                            log_id = tuple( [log_id] )
                            log_id = log_id[0] #So that it becomes an int

                            log_test = sign_in1(log_id)  #The function sign_in1() returns True if A match is found

                            


                            #If Login ID has been matched Successfully
                            if log_test:            
                                            #Returns True to pwd_test if Password Matches
                                            pwd_test = sign_in2(log_id)   
                                            



                                            if pwd_test:

                                               val = 1

                                               break



                                            else:

                                                print("\t \t \t Password Doesn't Match! Please Try Again!")
                                                terminator += 1
                                                if terminator == 10:
                                                            print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                            terminate()
                                                            terminated = True



                                                try:



                                                    pwd_choice = int(input("""\t \t \t Enter '1' to Re-enter details

                                                                                                          Enter '3' to exit"""))



                                                    if pwd_choice == 3:

                                                        terminate()
                                                        terminated = True



                                                    else:

                                                        print("\t \t \tTry again:")

                                                        terminator += 1

                                                        if terminator == 10:

                                                            print("\t \t \tToo many Unsuccesful Attempts. Program Terminated")

                                                            terminate()
                                                            terminated = True

                                                        

                                                        

                                        

                                                except ValueError:

                                                    print("\t \t \t Please Enter properly!")

                                                

                            else:

                                print("\n\t \t \t No Such Login ID found!")

                                log_choice = int(input("""\n \t \t \t To Re-enter Login ID Press '1'

           \t\t To Sign-Up Press '2'

           \t\t To exit, Press '3' """))



                                if log_choice == 3:

                                        terminate()
                                        terminated = True


                                elif log_choice == 2:

                                        log = 2   #Now, when the loop resets (because of continue) log (variable) will be 2 so the next if-block will be executed

                                        continue



                                elif log_choice == 1:

                                        print("\t \t \tRetry below: \n")
                        
                                        del log_test
                                        log = 1
                                        continue



                except ValueError:

                        print("\t \t \t Your ID consists of Digits only!")
                        terminator += 1
                        if terminator == 10:
                                                            print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                            terminate()
                                                            terminated = True
            

            elif log == 2:

                        
                        val = 0
                        while (val == 0):

                            log2_ch =  input("\n\n \t \t \t Enter ' 1 ' to Sign-Up or 'Quit' to exit")
                            



                            if log2_ch.lower() in ['quit','q','exit'] :

                                terminate()
                                terminated = True

             

                            elif log2_ch != '1':

                                    print("\n\t \t \t Please Enter '1' or 'Quit' Only!")



                            elif log2_ch == '1':

                                    print("\n\t \t \t Great! We'll just need some information from you.")

                                    user_data = info_collect()      # info_collect() function will return a LIST with all the user data into  'user_data' variable
                                    sign_up(user_data)                 # Now the same list will be passed to the function
                                    

                                    val = 1

                                    break

                        break



val = 0


st.loading()


print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n\n\n\n\n")

#Once ALL login stuff (from both) parts is done

print("\n\n\t \t \t \t Awesome! You're Logged in! \n\n\t \t \t How can we Help You?")

print("\n\t \t \t 1. View Your Information")

print("\t \t \t 2. Book an Appointment")

print("\t \t \t 3. Exit")


val=0
while val==0:
    try:
        op = int(input("\t \t \t Please Enter an Option from 1-3 Accordingly"))
        if op<1 or op>3:
            print("\t \t \tPlease Enter a Number between 1 and 3 only")
            terminator += 1
            if terminator == 10:
                                                            print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                            terminate()
                                                            terminated = True
        else:
            val=1
    except:
        print("\t \t \tPlease enter Numbers only")
        terminator += 1
        if terminator == 10:
                                                        print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                        terminate()
                                                        terminated = True

val = terminator = 0





#Variables:
    # userid_v  -- User entering user id
    # all_login_id_v --  All login ids in the Table
    # details_v -- Details of person
    # options_v  -- What they want to do after viewing info

val = val2 = val3 = 0
while (val == 0):
    if op==1:
    
        import mysql.connector as ms
        con=ms.connect(user='root',host='localhost',password='tiger',database='silverhill_hospital',autocommit=True)
            
        cur=con.cursor()
        
        
    
        cur.execute(f"select * from patients where Login_ID = {log_id} ; " )
        details_v= cur.fetchone()
        
        print("\t \t The Following Data is the Most Recent Information you have given us - ")
        print("\n\t\t\t Your Log-In ID is   :",   details_v[0])

        ln_pwd = len(details_v[1])
        
        #This Variable is being used to help us replace all characters of the password (except first and last) with ' * '
        asterisk = ln_pwd - 2
        
        print("\n\t\t\t Your Login Password is   :",   details_v[1][0] + (asterisk *  '*') + details_v[1][-1]) #details_v[1] is a string
        print("\n\t\t\t Your Registered Name is   :",   details_v[2])
        print("\n\t\t\t Your Registered Age is   :",   details_v[3])
        print("\n\t\t\t Your Registered Date of Birth (YYYY/MM/DD) is   :",   details_v[4])
        print("\n\t\t\t Your Registered Gender is   :",   details_v[5])
        print("\n\t\t\t Your Registered Weight is   :",   details_v[6])
        print("\n\t\t\t Your Registered Height is   :",   details_v[7])
        print("\n\t\t\t Your Registered Blood Group is   :",   details_v[8])
        print("\n\t\t\t Your Registered Emergency Contact is   :",   details_v[9])
        print("\n\t\t\t Your Registered Emergency Contact Number is   :",   details_v[10])
        print("\n\t\t\t Your Registered Phone Number is   :",   details_v[11])
        print("\n\t\t\t Your Registered Address is   :",   details_v[12])

        con.close()


        val2 = val3 =  0
        while (val2 == 0):
            print("\n\n\n\n\n\n\n\t\t\t Enter 1 if you would like to Update this Personal Information.")
            print("\t\t\t Enter 2 to Book an Appointment with one of our specilaists")
            print("\t\t\t Enter 3 to Delete your Account")
            print("\t\t\t Enter 4 to Exit the program")
            
            while (val3 == 0):
                try:
                    option_v = int(input("\n\t\t\t Please enter your choice (from 1-4) : "))
                    
                    if (option_v > 4) or (option_v < 1):
                              print("\n\t\t\t Please enter number between 1 and 4 only")
                              terminator += 1
                              if terminator == 10:
                                                                    print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                    terminate()
                                                                    terminated = True
                    else:
                        val3 = 1
                except ValueError:
                    print("\n\t\t\t Please enter a number only")
                    terminator += 1
                    if terminator == 10:
                                                                    print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")

               #This is Inside Second While Loop (val2 == 0)
                                                                    
            val2 = terminator = 0
            if option_v == 1:
                #UPDATE THIS WITH VARUN'S CODE
                    print("\t\t\t\t 1.NAME")
                    print("\t\t\t\t 2.DATE OF BIRTH")
                    print("\t\t\t\t 3.GENDER")
                    print("\t\t\t\t 4.WEIGHT")
                    print("\t\t\t\t 5.HEIGHT")
                    print("\t\t\t\t 6.BLOOD GROUP")
                    print("\t\t\t\t 7.EMERGENCY CONTACT INFORMATION")
                    print("\t\t\t\t 8.RESIDENTIAL ADDRESS")
                    
                    update_col = input("\n\t\t\t According to this menu pick ONE thing you'd like to change:")
                    vall = 0
                    while( vall == 0 ):
                        
                        if (( update_col.isalpha() )or (update_col.isspace() ) or (len(update_col) ) == 0 ):  
                                                     update_col = input("\t \t \t Invalid Entry, Please Choose Again : ")
                                                     terminator += 1
                                                     if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True
                                       
                        elif(int(update_col)<1 or int(update_col)>8):
                                                     update_col = input ("\t \t \t Please Enter a Number Between 1-6 Only")
                                                     terminator += 1
                                                     if terminator == 10:
                                                                print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                terminate()
                                                                terminated = True

                        else:
                                         vall = 1
                    vall = terminator = 0
                     
                     
                         
                    
                    import mysql.connector as ms
                    con=ms.connect(user='root',host='localhost',password='tiger',database='silverhill_hospital',autocommit=True)
            
                    cur=con.cursor()
                    print("\t \t \tPlease Enter Your Information Again:")
                    
                    update_col = int(update_col)
                    if update_col == 1:
                        cur.execute(f"update patients set name = '{name_collect()}' where Login_ID= {str(log_id)};")
                    
                    elif update_col == 2:
                        cur.execute(f"update patients set DOB = '{dob_collect()}' where Login_ID="+str(log_id))
                        cur.execute("update patients set age="+ str(age) +" where Login_ID="+str(log_id))
                        
                    elif update_col == 3:
                        cur.execute(f"update patients set gender= '{gender_collect()}' where Login_ID="+str(log_id))
                    
                    elif update_col == 4:
                        cur.execute("update patients set weight="+ str(weight_collect()) +" where Login_ID="+str(log_id))
                    
                    elif update_col == 5:
                        cur.execute("update patients set height="+ str(height_collect()) +" where Login_ID="+str(log_id))
                        
                    elif update_col == 6:
                        cur.execute("update patients set Blood_Group= '{blood_group_collect()}' where Login_ID="+str(log_id))
                    
                    elif update_col == 7:
                        
                        u_no,u_emerg_name,u_emerg_no = emergency_collect()
                    
                        cur.execute(f"update patients set Emergency_Contact= '{u_emerg_name}' where Login_ID="+str(log_id))
                        cur.execute("update patients set Emergency_Contact_Number="+ str(u_emerg_no) +" where Login_ID="+str(log_id))
                        cur.execute("update patients set Patient_Contact_Number="+ str(u_no) +" where Login_ID="+str(log_id))
                        
                    elif update_col == 8:
                        
                        cur.execute("update patients set address= '{address_collect()}'  where Login_ID="+str(log_id))
                        
                               
                    print("\n\t\t\t Your Information has Successfully Been Updated")
                    print("\n\t\t\t Your Updated information is as Follows")

                    cur.execute("select * from patients where Login_ID="+str(log_id))
                    y=cur.fetchone()
                    print("\n\t\t\t Your Registered Name is   :",   y[2])
                    print("\n\t\t\t Your Registered Age is   :",   y[3])
                    print("\n\t\t\t Your Registered Date of Birth (YYYY/MM/DD) is   :",   y[4])
                    print("\n\t\t\t Your Registered Gender is   :",   y[5])
                    print("\n\t\t\t Your Registered Weight is   :",   y[6])
                    print("\n\t\t\t Your Registered Height is   :",   y[7])
                    print("\n\t\t\t Your Registered Blood Group is   :",   y[8])
                    print("\n\t\t\t Your Registered Emergency Contact is   :",   y[9])
                    print("\n\t\t\t Your Registered Emergency Contact Number is   :",   y[10])
                    print("\n\t\t\t Your Registered Phone Number is   :",   y[11])
                    print("\n\t\t\t Your Registered Address is   :",   y[12])
                    
                    print("\t \t \t Done")
                    option_v_reset = int(input("\n \t \t \t Press '1' to back to the Main Menu or Press '2' to end the program."))
                    print("\t\t\t Did you want to update any other information? No problem just go back to the main menu and pick again!")

                    terminator = val0 = 0
                    while(val0 == 0 ):

                        try:
                            
                            if option_v_reset == 1:
                                    val2 = val3 = 0
                                    val0 = 1
                                    continue
                            elif option_v_reset == 2:
                                    terminate()
                                    terminated = True
                            else:
                                print("Please Enter an Appropriate Input!")
                                terminator += 1
                                if terminator == 10:
                                                                    print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                            if option_v_reset == 1:
                                continue
                                    
                        except ValueError:
                            print("Please Enter Numbers only!")
                            terminator += 1
                            if terminator == 10:
                                                                    print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")

                
            if option_v == 2:
                            op = 2
                            val2 = val3 = 1
                            val = 0
                            continue

            if option_v == 3:

                            val4 = terminator = 0
                            while val4==0:
                                try:
                                    option_delete_v=int(input("""\n\t\t\t Are you sure you want to delete your account? \n\t \t \tNOTE - All your data will be permanently removed from our Database.
                                                                                                Press 1 to confirm or Press 2 to Exit"""))
                                    if option_delete_v>2 or option_delete_v<1 :
                                        
                                        print("\n\t\t\t please enter between 1 and 2 only")
                                        terminator += 1
                                        if terminator == 10:
                                                                    print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                    terminate()
                                                                    terminated = True
                                    else:
                                        val4 = 1
                                except ValueError:
                                    print("\n\t\t\t Please Enter A Number only")
                                    terminator += 1
                                    if terminator == 10:
                                                                    print("\t \t \tToo many Unsuccesful Attempts. Please Re-start the Program")
                                                                    terminate()
                                                                    terminated = True
                            val4 = terminator =  0

                            if option_delete_v==1:

                                import mysql.connector as sql
                                connection = sql.connect(host = 'localhost', user = 'root', database = 'silverhill_hospital', password = 'tiger')
                                cur= connection.cursor()
                                
                                print("\n \t \t \t We're Sad to see you go! :(")
                                cur.execute("delete from patients where Login_ID="+str(log_id))  #SQL Query
                                st.loading()
                                print("\n\t \t \t Your account has been Deleted Successfully.")
                                print("\t \t \t Cleared all Records of Your Data.")
                                print("\t \t \tThe Program will End Now.")
                                connection.close()
                                terminate()
                                terminated = True
                            else:
                                print("\t \t \tThe Program will End Now.")
                                terminate()
                                terminated = True



            if option_v==4:
                       terminate()
                       terminated = True

    #If they Want to Book an Appointment
    elif op==2:  
        
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
        print("\t\t\t This is the appointment booking portal.")
        print("\t\t\t We offer Medical Services in the following Fields:")
        print("\t \t \t  1.Pathology")
        print("\t \t \t  2.Endocrinology")
        print("\t \t \t  3.Neurology")
        print("\t \t \t  4.Dermatology")
        print("\t \t \t  5.Cardiology")
        print("\t \t \t  6.Gynaecology")
        print("\t \t \t  7.Orthopaedics")
        while val==0:
             try:
                  option_field=int(input("""\n\t \t \t Which Specialist Would You like to Consult?
                                            Please Enter your choice as per the list (from 1-7) above:"""))
                  if  option_field<1 or option_field>7:
                        print("\n\t \t \t Please enter a Valid number between 1 and 7 ONLY")
                        val=0
                  else:
                         val = 1
             except ValueError:
                         print("\n\t\t\tPlease Enter Numbers Only")
                 
        if option_field==1:
            field = 'Pathology'
        elif option_field == 2:
            field = 'Endocrinology'
        elif option_field == 3:
            field = 'Neurology'
        elif option_field == 4:
            field = 'Dermatology'
        elif option_field == 5:
            field = 'Cardiology'
        elif option_field == 6:
            field = 'Gynaecology'
        elif option_field == 7:
            field = 'Orthopaedics'

        import datetime
        today = datetime.date.today()
        app_data_ret2 = appointment(field,today)
        doc_id, doc_name, field, app_date, app_time = app_data_ret2
    elif op == 3:
       terminate()
       terminated = True
        
if terminated == True:
        pass
else:

        st.loading()
        star = 170 * '*'
        print(star)
        print()
        print("   \t \t \t \t \t \t \t Silverhill Multispeciality Hospital",'', u"\u00A9")
        print()
        print(star)
        
        print('\n \n   \t \t \t \t \t \t \t APPOINTMENT CONFIRMATION \n \n')
        print("\n\t \t \t PATIENT")
        print("\t \t \t Patient Name : ",name.upper())
        print("\t \t \t Age :",age)
        print("\t \t \t Date Of Birth : ",DOB, "   (YYYY/MM/DD)")
        print("\t \t \t Gender :", gender)
        print("\t \t \t Weight : ", weight,'kg')
        print("\t \t \t Height : ", height,'cm')
        print("\t \t \t Body Mass Index (BMI) : ",(weight/((height/100)**2))) #BMI = kg/m^2
        print("\t \t \t Contact Number : ",no)
        print("\t \t \t Name of Emergency Contact : " ,emerg_name.upper())
        print("\t \t \t Emergency Contact (Number) : ",emerg_no)
        print("\t \t \t Address : ",address.upper())
        print("\t \t \t Blood Group : ",blood_group.upper())
        print("\n\t \t \t APPOINTMENT")
        print("\t \t \t Selected Field : ",field)
        print("\t \t \t Name of Doctor : ",doc_name)
        print("\t \t \t Appointment Date :" ,app_date, "(YYYY/MM/DD)")
        print("\t \t \t Appointment Time (24-Hour Format) : " ,app_time)

        print("\n \t \t \t Please Produce A Copy of this Confirmation at the reception and to the doctor on the day of your appointment \n")
        print("\t \t \t Thank You For Choosing Silverhill Multispeciality Hospital!",'', u"\u00A9", '\n \t \t \t We hope you are satisfied with our services.')
        print("\t \t \t For Cancellations or any queries Please Call +91 9885678973 \n \t \t \t For any Complaints Call +91  9123309765 \n")
              

        print(star)
        print()
        print("   \t \t \t \t \t \t \t Silverhill Multispeciality Hospital",'', u"\u00A9")
        print()
        print(star)
        print()

        #BILL EXPORT

        option_bill = input("""\n\n\t \t \t Would You Like to Export this a Copy of this Confirmation onto your Computer?
                                                Enter 'Yes' to create a copy
                                                or Enter 'No' or 'Exit' to End the Program""")

        if option_bill.isdigit():
                option_bill = input("\n\t \t \tPlease Enter Appropriately:")
        elif option_bill.lower() in ['y','yes']:
            

            file = open("SilverHill Hospital Appointment Confirmation.txt","w+")
            
            write_data=[f"{star} \n\n",
                        "\t \t \t \t \t \t \t Silverhill Multispeciality Hospital"+ u"\u00A9",
                        f"\n\n{star} \n",
                        '\n \n   \t \t \t \t \t \t \t APPOINTMENT CONFIRMATION \n \n\n',
                        "\n\t \t \t PATIENT \n",
                        f"\t \t \t Patient Name : {name} \n",
                        f"\t \t \t Age : {age} \n",
                        f"\t \t \t Date Of Birth : {DOB} (YYYY/MM/DD) \n",
                        f"\t \t \t Gender : {gender} \n",
                        f"\t \t \t Weight : {weight} kg \n",
                        f"\t \t \t Height : {height} cm \n",
                        f"\t \t \t Body Mass Index (BMI) :" + str( (weight/((height/100)**2))) + "\n", #BMI = kg/m^2
                        f"\t \t \t Contact Number : {no} \n",
                        f"\t \t \t Name of Emergency Contact : {emerg_name} \n",
                        f"\t \t \t Emergency Contact (Number) : {emerg_no} \n",
                        f"\t \t \t Address : {address} \n",
                        f"\t \t \t Blood Group :{blood_group} \n",
                        f"\n\t \t \t APPOINTMENT \n",
                        f"\t \t \t Selected Field : {field} \n",
                        f"\t \t \t Name of Doctor : {doc_name} \n",
                        f"\t \t \t Appointment Date : {app_date} (YY/MM/DD) \n",
                        f"\t \t \t Appointment Time (24-Hour Format) : {app_time} \n",
                        f"\n \t \t \t Please Produce A Copy of this Confirmation at the reception and to the doctor on the day of your appointment \n\n",                                          
                        f"\t \t \t Thank You For Choosing Silverhill Multispeciality Hospital!" +  u"\u00A9" + '\n \t \t \t We hope you are satisfied with our services.\n',
                        f"\t \t \t For Cancellations or any queries Please Call +91 9885678973 \n \t \t \t For any Complaints Call +91  9123309765 \n",
                        f"\n\n{star} \n\n",
                        "\t \t \t \t \t \t \t Silverhill Multispeciality Hospital" + u"\u00A9",
                        f"\n\n{star} \n" ]
                        
                        
                        
            file.writelines(write_data)
            file.close()
            terminate()

        elif option_bill.lower() in ['n','no','exit','quit','q']:
            terminate()
            terminated = True
            