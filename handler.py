import time

while True:
    command = input('Enter a command: ')
    with open('command.txt', 'w') as command_file:
        command_file.write(command)

    time.sleep(3)

    with open('stdout.txt', 'r') as stdout_file:
        for line in stdout_file:
            print(line.strip())
