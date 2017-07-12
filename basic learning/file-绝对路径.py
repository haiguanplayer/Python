file_path = 'C:\\Users\\liu customs\\Desktop\\pi.txt'#必须用双“\\”
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.strip())