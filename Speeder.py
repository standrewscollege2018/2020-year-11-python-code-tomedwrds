print("Welcome to the speeders fine calculation system")

#Create an exiting while loop
day = True

#Set up varialbles
total_fines = 0
total_fine_money = 0
wanted_list = ["John Smith", "Helga Norman", "Zach Conroy"]

while day:
    
    
    
    #Take inputs
    name = input("Enter the name of the offender:")
    
    #Set up a while loop to prevent incorent speed inputs
    driver_speed_input = True
    while driver_speed_input:
        
        try:
            speed = int(input("Enter the offenders speed:"))
            driver_speed_input = False
        except: 
            print("Please enter a valid speed")
            
            
    speed_limit_input = True
    while speed_limit_input:
        
        try:
            speed_limit = int(input("Enter the speed limit:"))
            speed_limit_input = False
        except: 
            print("Please enter a valid speed limit")
            
            
            
    margain_over_speed_limit = speed - speed_limit
    fine = 0
    
    if margain_over_speed_limit <= 0:
         print("The speed limit was not breached\n\n")
    else:
        if margain_over_speed_limit < 10:
            fine = 30
        elif margain_over_speed_limit < 20:
            fine = 80
        elif margain_over_speed_limit < 30:
            fine = 130
        elif margain_over_speed_limit > 29:
            fine = 180
        
        print("{} should be fined ${}\n\n".format(name,str(fine)))
        total_fines += 1
        total_fine_money += fine
            
           
        
        
    
    
     
        
        
    
    
    
    #Exit condition
    if name == "end" :
        
        print("End of day summary")
        print("Total number of fines: {}".format(total_fines))
        print("Total money of fines: {}".format(total_fine_money))
        
        day = false