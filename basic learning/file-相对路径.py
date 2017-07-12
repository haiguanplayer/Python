with open('text_files\pi.txt' ) as file_object:
    contents = file_object.read()
    print(contents.strip())