#with open('write_to_the_file.txt', 'r+', encoding='utf-8') as file1:
#    file1.write('rerecord line.\n')
    
# with open('write_to_the_file.txt', 'a', encoding='utf-8') as file1:
#   file1.write('second line.\n')
#    file1.write('third line.\n')
#    file1.write('fourth line.\n')

with open('write_to_the_file.txt', 'a', encoding='utf-8') as file1:
    print('print with', file=file1)