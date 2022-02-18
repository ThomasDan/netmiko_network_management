from Connection_Manager import disconnect
from Interface_Management import config_ints
from TestFolder.General_Management import config_hostname, config_motd, show_ints
from snmp_mib_handling.Mikkel_Mib import mikkel_mac_address_get
from mib_control import get, get_time

def user_select(user_input):
    if user_input == 1:
        config_hostname()
    elif user_input == 2:
        config_motd()
    elif user_input == 3:
        show_ints()
    elif user_input == 4:
        config_ints()
    elif user_input == 5:
        mikkel_mac_address_get()
    elif user_input == 6:
        up_time = get_time()
        print(up_time)
    else:
        print("Stopping Program!")
        return True
    return False

def start():
    done = False
    #reset_ssh_commands = [ 'exit', 'clear line vty 2', '', 'clear line vty 3', '', 'clear line vty 4', '' ]
    while not done:
        #config_sender(reset_ssh_commands)
        
        print("\n\nHallo what do you want to do today?\nPress 1: Set Hostname. 2: Set Motd. 3: See Interfaces. 4: Configure Interface IPs. 5: See Mac Addresses in Network.")

        user_input = int(input())
        done = user_select(user_input)
    disconnect()

start()
print('Done!')