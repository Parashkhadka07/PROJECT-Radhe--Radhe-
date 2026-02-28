import json
import os
json_file="Task_data.json"

def load_task():

#checks either the file is there or not if not creates new file
    try:
        with open(json_file,"x") as f:#checks if the file exists if not create new
            f.write([])
    except FileExistsError:
        pass
    f.close(json_file)


##reads created file and write file data
    try:
        with open(json_file,"r") as f:
            if(os.path.getsize==0):
                print("NO TASKS INCLUDED")
            else:
                Data=f.load()
                print(Data)

            
    except:
        print("Something went wrong")
    
    f.close()


def Read_task(id):
    pass


def update_task(id,):
    pass

def delete_task(id):
    pass

if __name__=="__main__":
    load_task()
    Read_task()
    update_task()
    delete_task()