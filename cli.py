from colorama import Fore,Style
import task_manager

def commands(command):
    if command=="1":
        print(Fore.YELLOW +"Your tasks are:")
        task_manager.read_task_and_print()
       
    elif command=="2":
        
        print("YOUR TASKS ARE:")
        task_manager.read_task_and_print()
        task_manager.update_task()

    elif command=="3":
        
        task_manager.read_task_and_print()
        task_manager.delete_task()
        pass
    elif command=="4":
        pass
    else:
        print("PLEASE ENTER THE VALID COMMAND")