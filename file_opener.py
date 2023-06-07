def file_opener(file_name):
    my_file = open(file_name)
    my_file.close()

file_opener('text.txt')