from colorama import Fore
import cli
def command_taker():
    print(Fore.BLUE+"WELCOME TO THE TASK TRACKER APP:","\nENTER COMMAND:\n1.Tasks\n2.Update tasks\n3.Delete Tasks\n4.Create Tasks")
    cli_command=input()
    cli.commands(cli_command)



if __name__=="__main__":
    command_taker()