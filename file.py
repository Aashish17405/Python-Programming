import os
#print(os.getcwd())
#os.chdir('\Users\RAJU\Desktop\Aashish\aashish programming files\PYTHON progrmming')
#os.mkdir('Aashish')
#os.makedirs('Aashish/pyt')
#os.rmdir('Aashish')
#os.removedirs('Aashish/pyt')
#os.rename('files.py','file.py')
#print(os.stat('file.py'))
#print(os.stat('file.py').st_nlink)
#print(os.listdir())
#print(os.walk('desktop'))

#FILES
#f=open('kmit.txt')

with open('kmit.txt','r') as f:
    
    #f_contents=f.read()
    #f_contents=f.readlines()       #reads the lines of a file and stores into a list
    #f_contents=f.readline()        #reads the first line into a list
    #print(f_contents)
    size_to_read=10
    #print(f.read(size_to_read))               #read() takes size as an argument
    f_contents=f.read(size_to_read)
    '''for line in f:
        print(line,end='')'''

    #print(f.tell())                  #prints the position in the file
    #f.seek(0)                        #change the position in the file

    '''while len(f_contents)>0:
        print(f_contents,end='')
        f_contents=f.read(size_to_read)'''

#print(f.closed)

'''with open('text.txt','w') as f:
    f.write("test")
    f.seek(0)
    f.write("Reload")'''

#f=open('kmit.txt','r')
#print(f.name)
#print(f.mode)
#f.close()

'''with open('kmit.txt','r') as rf:            #Copy the contents of one file to another
    with open('test.txt','w') as wf:
        for line in rf:
            wf.write(line)'''

with open('bronx.jpg', 'rb') as rf:
    with open('bronx_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)