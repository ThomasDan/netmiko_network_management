from Connection_Manager import disconnect
from Interface_Management import config_ints
from TestFolder.General_Management import config_hostname, config_motd, show_ints


def user_select(user_input):
    if user_input == 1:
        config_hostname()
    elif user_input == 2:
        config_motd()
    elif user_input == 3:
        show_ints()
    elif user_input == 4:
        config_ints()
    else:
        print("Stopping Program!")
        return True
    return False

def start():
    done = False
    #reset_ssh_commands = [ 'exit', 'clear line vty 2', '', 'clear line vty 3', '', 'clear line vty 4', '' ]
    while not done:
        #config_sender(reset_ssh_commands)
        
        print("\n\nHallo what do you want to do today?\nPress 1: Set hostname. 2: Motd. 3: See interfaces. 4: Configure Interfaces.")
        user_input = int(input())
        done = user_select(user_input)
    disconnect()

start()
print('Done!')