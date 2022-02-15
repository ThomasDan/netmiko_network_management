from Connection_Manager import command_sender, config_sender


def acquire_ints():
    raw = command_sender('show int accounting')
    
    temp_text = raw.splitlines()
    output = []
    
    for _str in temp_text:
        if _str[:1] != ' ':
            _str = _str.replace(' is disabled', '')
            _str = _str.replace('Interface ', '')
            if _str[-1:] == ' ':
                _str = _str[:-1]
            if _str != '':
                output.append(_str)
    
    return output

def print_ints(ints):
    print('-' * 10)
    for i in range(0, len(ints)):
        print(str(i+1) + '. ' + ints[i])
    print('-' * 10)

def config_ints():
    ints = acquire_ints()
    satisfied = False
    while not satisfied:
        print('\n\n-------------------------\nWelcome to Interface Configuration!\nWhich interface would you like to mess with?')
        
        print_ints(ints)
        
        interface = int(input())-1
        
        
        print('\nGreat!\n' + ints[interface] + ', what IP should it have (plus subnet mask :))?')
        
        int_ip = input()
        
        cmds = [
            'int ' + ints[interface],
            'ip address ' + int_ip
            ]
        
        config_sender(cmds)
        
        print('\nBueno!\nWould you like to config more? Y/N')
        satisfied = input().upper() != 'Y'
    print('All set and done!\nCongratulations!\nYour interface(s) is/are now configured!');
