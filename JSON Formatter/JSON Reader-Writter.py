import json


def read_json():
    
    #Read the file
    with open('json_test_file.jsonld') as f:
        data = json.load(f)
        
    #Get specific data through the use of 2d array
    print(data)
        
 
    
def write_json():
    
    #Create some data
    person1 = {
        "name":"tom",
        "age":"10"
        }
    person2 = {
        "name":"callumn",
        "age":"10"
        }
    person3 = {
        "name":"toby",
        "age":"10"
        }    
    
    people = {
        0 : person1,
        1 : person2,
        2 : person3
        }
    
   
    
    #Write to file
    
    with open('json_test_file_write.jsonld', 'w') as json_file:
      json.dump(people, json_file,indent = 4)    
    
    
    
    
read_json()
write_json()
    
