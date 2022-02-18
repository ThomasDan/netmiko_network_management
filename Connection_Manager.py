from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host': '10.10.1.1',
    'username': 'cisco',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco'
    }
net_connect = ConnectHandler(**cisco_881)


def command_sender(command):
    try:
        return net_connect.send_command(command, delay_factor = 5)
    except:
        return 'command fucked up i don\'t know why'

def config_sender(commands):
    try:
        return net_connect.send_config_set(commands, delay_factor = 5)
    except:
        return 'config set fucked up i don\'t know why'

def disconnect():
    net_connect.disconnect()


def reset_ssh_connections():
    #net_connect.exit_config_mode()
    
    cmds = ['end']
    
    net_connect.enable()
    for i in range(5):
        try:
            print('Clearing ssh line ' + str(i))
            net_connect.send_command('clear line vty ' + str(i))
            
        except:
            print('Unable to close ssh line ' + str(i))
            # err :D
    #net_connect.send_config_set(cmds)

def show_ssh():
    print(net_connect.send_command('show ssh'))