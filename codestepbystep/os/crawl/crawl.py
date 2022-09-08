import os

def crawl(course: str):
    path = os.getcwd()
    print(path)
     
    for root, dir_names, file_names in os.walk(path):
        # print(f"The root is {root}")
        # print(f"The directory name is: {dir_names}")
        # print(f"The file names are: {file_names}")
        # print(f"*"*10)
        
        for i in dir_names:
            if course in i:
                print(f"found {course}:")
                print(i)
                
                
        for i in file_names:
            if course in i:
                print(f"found {course} in {root}:")
                print(i)
                
        
              
crawl("hw")
    