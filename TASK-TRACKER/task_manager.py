import file_handaler
import task_manager
from main import command_taker
from colorama import Fore
def read_task():
    file_handaler.iniclitze_file()
    Datas=file_handaler.Read_file()
    return Datas

def read_task_and_print():
    file_handaler.iniclitze_file()
    Datas=file_handaler.Read_file()
    for task in Datas:# writes the output of the read command
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Status: {task['status']}")
        print("-" * 30)
    
def update_task():
    Datas=task_manager.read_task()
    print(Fore.LIGHTRED_EX+"please enter the task id you want to update:")
    id=input()
    print("enter the updated title:")
    title=input()
    print("enter the updated status:")
    status=input()
        
    for i in range(len(Datas)):
        if Datas[i]["id"]==int(id):
            Datas[i]={"id":int(id),"title":title,"status":status}
            break
    
    file_handaler.write_file_or_update_file_or_delete_task(Datas)
    print("YOUR TASK IS UPDATED")
    command_taker()

def delete_task():
    Datas=task_manager.read_task()
    print(Fore.MAGENTA+ "SELECT THE ID OF THE TASK YOU WANT TO DELETE:")
    id=input()
    for i in range(len(Datas)):
        if Datas[i]["id"]==int(id):
           del Datas[i]
           break
    else:
        print("TASK ID NOT FOUND:")     
    file_handaler.write_file_or_update_file_or_delete_task(Datas)
    print("YOUR TASK IS DELETED")
    command_taker()

def create_task():
    print("ENTER THE NUMBER OF THAK YOU WANT TO ADD:")
    number=int(input())
    for i in range(number):
        print("ENTER THE TITLE OF THE TASK:")
        TITLE=input()
        print("ENTER THE STATUS OF THE TASK")
        STATUS=input()
        list=file_handaler.Read_file()
        idd=len(list)+1
        data={"id":idd,"title":TITLE,"status":STATUS}
        data_for_file=list.append(data)
        
        file_handaler.write_file_or_update_file_or_delete_task(data_for_file)

    



    



if __name__=="__main__":
    read_task()
    update_task()
    read_task_and_print()
    delete_task()
    create_task()