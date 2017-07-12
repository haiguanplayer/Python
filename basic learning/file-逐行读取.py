file_path = 'C:\\Users\\liu customs\\Desktop\\pi.txt'#必须用双“\\”
with open(file_path) as file_object:
    for line in file_object:
        print(line.strip())