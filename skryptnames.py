with open("names.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)