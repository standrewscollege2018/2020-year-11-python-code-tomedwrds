#Bookstore catalouge

#Define macros/constants
NAME = 0
AUTHOUR = 1
PRICE = 2
STOCK = 3

#Index to be used when adding books
book_index = 0

catalouge = [["name","authour","price","stock"],["name","authour","price","stock"]]



running_program = True

while(running_program):
    
    selecting_option = True
    
    while(selecting_option):
        #Present options to users
        print("1) Add books")
        print("2) Delete books")
        print("3) Modify books")
        print("4) End program")
        
        
        #Take user input
        try:
            user_input = int(input("Please choose an option: "))
            
            if user_input > 0 and user_input <= 4:
                selecting_option = False
            else:
                print("ERROR: Please enter a valid option")
        
        except: 
            print("ERROR: Please enter a valid option")
        
        
    #Add books
    if user_input == 1:
        
        #Take input from user to use in dictonary
        name = input("name")
        authour = input("authour")
        
        #Error check on price and stock to prevent invalid entries
        
        price_input = True
       
        while(price_input):
            try:
                price = int(input("price"))
                
                #Check for values less than 0
                if price > 0:
                    price_input = False
                    
                else:
                    print("ERROR: Please enter a valid option")
                    
                    
            except:
                print("ERROR: Please enter a valid option")
            
            
    
        stock_input = True


        while(stock_input):
            try:
                stock = int(input("stock"))

                #Check for values less than 0
                if stock > 0:
                    stock_input = False
        
                else:
                    print("ERROR: Please enter a valid option")
        
        
            except:
                print("ERROR: Please enter a valid option")
        
        
        #Add the values to the list
        catalouge[book_index, NAME] = name
        catalouge[book_index, AUTHOUR] = authour
        catalouge[book_index, PRICE] = price
        catalouge[book_index, STOCK] = stock
        
        #Increment the book_index value
        book_index += 1
                  
        
        
                
        
                    
            
            
                    
                    
                    
                    
                    
            
                
        
            
            
            
