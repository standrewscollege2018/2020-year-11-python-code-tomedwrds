#Bookstore catalouge

def display_book_list():
    #Book list
    
    print("\n(x)---BOOK LIST---(x)\n")
    
    for x in range(len(catalouge)):
        
        #Print book information
        print(catalouge[x][NAME] + " ({}/{})".format(x+1,len(catalouge)))
        print("By: {}".format(AUTHOUR))
        print("Price: {}".format(PRICE))   
        print("Stock: {}".format(STOCK))
        
        #Break a line for redability

        print("\n")
        
        
#Define macros/constants
NAME = 0
AUTHOUR = 1
PRICE = 2
STOCK = 3

#Index to be used when adding books
book_index = 0



catalouge = []

running_program = True
OPTION_NUMBERS = 5

while(running_program):
    
    selecting_option = True
    
    while(selecting_option):
        #Present options to users
        print("1) Add books")
        print("2) Delete books")
        print("3) Modify books")
        print("4) Display books list")
        print("5) End program")
        
        
        #Take user input
        try:
            user_input = int(input("Please choose an option: "))
            
            if user_input > 0 and user_input <= OPTION_NUMBERS:
                selecting_option = False
            else:
                print("ERROR: Please enter a valid option")
        
        except: 
            print("ERROR: Please enter a valid option")
        
        
    #Add books
    if user_input == 1:
        
        #Take input from user to use in dictonary
        print("\n()---Add Book---()\n")
        name = input("Book Title: ")
        authour = input("Authour of {}: ".format(name))
        
        #Error check on price and stock to prevent invalid entries
        
        price_input = True
       
        while(price_input):
            try:
                price = int(input("Price of {}: ".format(name)))
                
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
                stock = int(input("Stock of {}: ".format(name)))

                #Check for values less than 0
                if stock > 0:
                    stock_input = False
        
                else:
                    print("ERROR: Please enter a valid option")
        
        
            except:
                print("ERROR: Please enter a valid option")
        
        
        #Add the values to the list
        catalouge.append([name,authour,price,stock])
      
        
        #Increment the book_index value
        book_index += 1
     
     
     
    #Delete books
    if user_input == 2:
        
        finding_book = True
        book_exsists = False
        
        while finding_book:
            #Find book through input
            print("\n()---Deleting Books---()\n")
            print("Enter '-1' to go back")
            print("Enter '0' to display book list")
            print("Enter books title to delete it: ")
            book_name_delete = input()
            
            #Loop through the array to see if value exists
            for x in range(len(catalouge)):
                
                #Delete book should it be found
                if book_name_delete == catalouge[x][NAME]:
                    
                    catalouge.pop(x)
                    
                    
                    print("{} has been succesfully deleted".format(book_name_delete))
                    
                    
                    #set vars accordinhly to exit while loop
                    book_exsists = True
                    finding_book = False
                    
            
            #Check if the book isnt found
            if book_exsists == False:  
        
                if book_name_delete == "-1":
                    
                    finding_book = False
                    
                elif book_name_delete == "0":
                        
                    display_book_list()               
                    
                else:
                    print("ERROR: The book you are looking for doesnt exsist")
                
            
                
    
    #Modify books
    if user_input == 3:   
        
        finding_book = True
        book_exsists = False
        
        while finding_book:
            #Find book through input
            print("()---Modify Books---()")
            print("Enter -1 to go backwards")
            book_name_modify = input("Enter book name to modify: ")
            
            #Loop through the array to see if value exists
            for x in range(len(catalouge)):
                
                #Delete book should it be found
                if book_name_modify == catalouge[x][NAME]:
                    
                    #Find out what aspect of the book to modify
                   
                    selecting_book_value_to_modify = True
                    
                    while selecting_book_value_to_modify:
                        
                        try:
                            
                            print("What aspect of {} do you wish to modify: ".format(book_name_modify))
                            print("-1) Back")
                            print("1) Title")
                            print("2) Authour")
                            print("3) Price")
                            print("4) Stock")
                            print("5) Display List of Books")
                            
                            
                            
                                     
                            value_to_modify = int(input())
                            
                            if value_to_modify == -1:
                                
                                selecting_book_value_to_modify = False
                                
                            elif value_to_modify == 1:
                                
                                catalouge[x][NAME] = input("Please enter a new title: ")
                                selecting_book_value_to_modify = False
                                
                            elif value_to_modify == 2:
                                
                                catalouge[x][AUTHOUR] = input("Please enter a new authour: ")
                                selecting_book_value_to_modify = False
                                
                            elif value_to_modify == 3:
                        
                                price_input = True
                        
                        
                                while(stock_input):
                                    try:
                                        catalouge[x][PRICE] = int(input("Please enter a new price: "))
                        
                                        #Check for values less than 0
                                        if catalouge[x][PRICE] > 0:
                                            price_input = False
                        
                                        else:
                                            print("ERROR: Please enter a valid option")
                        
                        
                                    except:
                                        print("ERROR: Please enter a valid option")
                                        
                            elif value_to_modify == 4:
                                
                                stock_input = True


                                while(stock_input):
                                    try:
                                        catalouge[x][STOCK] = int(input("Please enter a new stock: "))
                        
                                        #Check for values less than 0
                                        if catalouge[x][STOCK] > 0:
                                            stock_input = False
                                
                                        else:
                                            print("ERROR: Please enter a valid option")
                                
                                
                                    except:
                                        print("ERROR: Please enter a valid option")
                                
                                
                            elif value_to_modify == 5:
                                display_book_list()
                                
                                
                                
                               
                                
                                

                                
                                
                                
                            
                        except:
                            print("ERROR: Please enter a valid value")
                    
                    
                    
                    book_exsists = True
                    finding_book = False
                    
            
            #Check if the book isnt found
            if book_exsists == False:  
        
                if book_name_modify == "-1":
                    
                    finding_book = False
                    
                else:
                    print("ERROR: The book you are looking for doesnt exsist")
        
        
        
        
     
    
    
    #Display book list   
    if user_input == 4:
        display_book_list()
        

