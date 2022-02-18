from Connection_Manager import disconnect, reset_ssh_connections
from Interface_Management import config_ints
from TestFolder.General_Management import config_hostname, config_motd, show_ints
from snmp_mib_handling.Mikkel_Mib import mikkel_mac_address_get
from snmp_mib_handling.SNMP_MIB_Handler import get_int_bulk_result, get_time


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
    elif user_input == 7:
        get_int_bulk_result()
    elif user_input == 8:
        reset_ssh_connections()
    else:
        print("Stopping Program!")
        return True
    return False

def start():
    done = False
    
    while not done:
        
        print("\n\nHallo what do you want to do today?\n\n 1: Set hostname.\n 2: Motd.\n 3: See interfaces.\n 4: Configure Interfaces.\n 5: See Mac Addresses in Network.\n 6: See Up-Time\n 7: MIB_Interfaces\n 8: Reset SSH Connections")
        user_input = int(input())
        done = user_select(user_input)
    disconnect()

start()
print('Done!')