import json
import os
json_file="Task_data.json"



def iniclitze_file():
    #checks either the file is there or not if not creates new file
    try:
        with open(json_file,"x") as f:
            pass
    except FileExistsError:
        pass
    

def Read_file():
    ##reads created file and write file data
    try:
        with open(json_file,"r") as f:
            if(os.path.getsize(json_file)==0):
                print("NO TASKS INCLUDED TILL NOW")
            else:
                Data=json.load(f)
                return Data
    except:
        print("Something went wrong")
    
    
def write_file_or_update_file_or_delete_task(new_data):
    with open(json_file,"w") as f:
        json.dump(new_data,f) 
    



if __name__=="__main__":
    iniclitze_file()
    Read_file()
    write_file_or_update_file_or_delete_task()
   