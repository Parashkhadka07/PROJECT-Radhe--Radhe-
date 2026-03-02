import file_handaler
import sys
import task_manager
from main import command_taker
from colorama import Fore

Task_state=["done","inprocess","todo"]

def read_task():
    
    Datas=file_handaler.Read_file()
    return Datas



def read_task_and_print():
    
    Datas=file_handaler.Read_file()
    if Datas==[]:
        print(Fore.RED+"NO TASKS INCLUDED TILL NOW"+Fore.RESET)
        
        
    else:
        for task in Datas:# writes the output of the read command
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Status: {task['status']}")
            print("-" * 30)
    
        
    
    
def update_task():
    Datas=read_task()
    read_task_and_print()
    print(Fore.BLUE+"please enter the task id you want to update:"+Fore.RESET)
    id=input()
    
    for i in range(len(Datas)):       
        if Datas[i]["id"]==int(id):
            print("enter the updated title:")
            title=input()
            print("enter the updated status:\n-todo\n-inprocess\n-done")
            status=input().lower()

            if status in Task_state:
                Datas[i]={"id":int(id),"title":title,"status":status}
                file_handaler.write_file_or_update_file_or_delete_task(Datas)
                print(Fore.GREEN+"YOUR TASK IS UPDATED"+Fore.RESET)
            else:
                print(Fore.RED+"PLEASE ENTER THE VALID STATUS"+Fore.RESET)
                update_task()  
            break
    else:
        print(Fore.RED+"TASK DOESNOT EXIST"+Fore.RESET)
        
   
    
    command_taker()



def delete_task():
    Datas=task_manager.read_task()
    if Datas==[]:
        print(Fore.RED+"NO TASKS INCLUDED TILL NOW"+Fore.RESET)
        command_taker()
    else:
        for task in Datas:# writes the output of the read command
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Status: {task['status']}")
            print("-" * 30)
    print(Fore.MAGENTA+ "SELECT THE ID OF THE TASK YOU WANT TO DELETE:"+Fore.RESET)
    id=input()
    for i in range(len(Datas)):
        if Datas[i]["id"]==int(id):
           del Datas[i]
           file_handaler.write_file_or_update_file_or_delete_task(Datas)
           print(Fore.RED+"YOUR TASK IS DELETED"+Fore.RESET)
           break
    else:
        print(Fore.red+"TASK ID NOT FOUND:"+Fore.RESET)     
    
    command_taker()



def create_task():
    print(Fore.GREEN+"\nENTER THE NUMBER OF TASK YOU WANT TO ADD:"+Fore.RESET)
    number=int(input())
    for i in range(number):
        print(Fore.BLUE+f"\nENTER THE TITLE OF THE {i+1}st TASK:"+Fore.RESET)
        TITLE=input()
        print(Fore.BLUE+f"ENTER THE STATUS OF THE {i+1}st TASK:\n-todo\n-inprocess\n-done\n"+Fore.RESET)
        STATUS=input().lower()
        listt=file_handaler.Read_file()
        
        if listt==[]:
            new_id = 1
        else:
            max_id = max(task["id"] for task in listt)
            new_id = max_id + 1

        if STATUS in Task_state:
            Data={"id":new_id,"title":TITLE,"status":STATUS}
            listt.append(Data)
            file_handaler.write_file_or_update_file_or_delete_task(listt)
            print(Fore.GREEN+"YOUR TASK IS CREATED"+Fore.RESET)
        else:
            print(Fore.RED+"PLEASE ENTER THE VALID STATUS\n"+Fore.RESET)
            create_task()  
        
    command_taker()


def exit_program():
    print(Fore.YELLOW+"EXITING THE PROGEAM......GOODBYE....."+Fore.RESET)
    sys.exit()

def sorter(status_entry):
    Data=file_handaler.Read_file()
    for task in Data:
        if status_entry==task["status"]:
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Status: {task['status']}")
            print("-" * 30)
    command_taker()      
        



    



if __name__=="__main__":
    read_task()
    update_task()
    read_task_and_print()
    delete_task()
    create_task()
    exit_program()