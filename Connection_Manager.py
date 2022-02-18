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
    
    cmds = ['end']
    # Here we find out which vty lines (SSH) are open
    raw_ssh_connections = command_sender('show ssh').splitlines()
    open_lines = []
    for line in raw_ssh_connections:
        try:
            #If the first character in the lien can be converted to an int..
            v = int(line[0][:1])
            line_already = False
            # And is not already set for closing..
            for line_ in open_lines:
                if v == line_:
                    line_already = True
                    break
            if not line_already:
                # Add to open_lines to be clsoed
                open_lines.append(v)
        except:
            b = 1 #No exception required, the int conversion is supposed to fail sometimes
    
    net_connect.enable()
    for i in open_lines:
        try:
            print('Clearing ssh line ' + str(i))
            net_connect.send_command('clear line vty ' + str(i))
            
        except:
            print('Unable to close ssh line ' + str(i))

def show_ssh():
    print(net_connect.send_command('show ssh'))