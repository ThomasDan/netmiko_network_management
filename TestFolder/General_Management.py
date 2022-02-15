from Connection_Manager import config_sender, command_sender

def config_hostname():
    print('What do you want the hostname to be?')
    input_hostname = input()
    hostname_output = config_sender('hostname '+ input_hostname)
    command_sender('show hostname')
    print('The hostname is: ' + input_hostname)

def config_motd():
    print('What is the message of the day?')
    input_motd = input()
    motd_output = config_sender('banner motd #'+ input_motd +'#')
    command_sender('show banner motd')
    print('The message of the day is #' + input_motd + '#')

def show_ints():
    output = command_sender('show ip int brief')
    print(output)