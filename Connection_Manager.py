from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host': '10.10.10.1',
    'username': 'cisco',
    'password': 'cisco',
    'port': 22,
    'secret': ''
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