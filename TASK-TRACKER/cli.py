from colorama import Fore,Style
import task_manager
import sys
from main import command_taker
def commands(command):
    if command=="1":
        print(Fore.GREEN+"\n1.ALL Task\n2.Done Task\n3.TODO task\n4.Inprocess Task\n"+Fore.RESET)
        commandd=int(input())
        if commandd==1:
            print(Fore.YELLOW +"Your tasks are:"+Fore.RESET)
            Datas=task_manager.read_task()
            if Datas==[]:
                print("NO TASKS INCLUDED TILL NOW")
        
        
            else:
                for task in Datas:# writes the output of the read command
                    print(f"ID: {task['id']}")
                    print(f"Title: {task['title']}")
                    print(f"Status: {task['status']}")
                    print(f"createdAt: {task['createdAt']}")
                    print(f"updatedAt: {task['updatedAt']}")
                    print("-" * 30)
            command_taker()
        elif commandd==2:
            task_manager.sorter("done")
        elif commandd==3:
            task_manager.sorter("todo")
        elif commandd==4:
            task_manager.sorter("inprocess")
        else:
            print(Fore.RED+"Please choose the valid status"+Fore.RESET)



        
    elif command=="2":
        print(Fore.YELLOW +"Your tasks are:"+Fore.RESET)
        task_manager.update_task()
    elif command=="3":
        task_manager.delete_task()
    elif command=="4":
        task_manager.create_task()
    elif command=="5":
        task_manager.exit_program()
    else:
        print(Fore.RED+"PLEASE ENTER THE VALID COMMAND"+Fore.RESET)