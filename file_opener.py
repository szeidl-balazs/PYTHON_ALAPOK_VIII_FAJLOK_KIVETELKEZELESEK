def file_opener(file_name):
    current_file = open(file_name)
    print(current_file)
    current_file.close()

file_opener('text.txt')
