from colorama import Fore
import file_handaler
import cli
def command_taker():
    file_handaler.iniclitze_file()
    print(Fore.BLUE+"\nENTER COMMAND:"+Fore.RESET,Fore.GREEN+"\n1.Tasks\n2.Update tasks\n3.Delete Tasks\n4.Create Tasks\n5.EXIT\n"+Fore.RESET)
    cli_command=input()
    cli.commands(cli_command)



if __name__=="__main__":  
    print(Fore.YELLOW+"\nWELCOME TO THE TASK TRACKER APP:"+Fore.RESET)
    command_taker()