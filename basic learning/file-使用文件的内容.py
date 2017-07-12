file_path = 'C:\\Users\\liu customs\\Desktop\\pi.txt'#必须用双“\\”
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip();
print (pi_string)
print (len(pi_string))