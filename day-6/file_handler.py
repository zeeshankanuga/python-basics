# file_obj=open('my_file.txt','r')    #open
# print(file_obj.readlines())   #process
# file_obj.close()    #close


# ################

# file_obj=open('my_file.txt','w')    #open
# print(file_obj.write("this is my first line"))   #process
# file_obj.close()    #close


################
file_obj_new=open('my_new_file2.txt','w+')    #open

try:
    file_obj_new=open('my_new_file2.txt','r')   #process

except FileNotFoundError:
    print("file not found")
    file_obj_new=open('my_new_file2.txt','w+')    #open

finally:
    file_obj_new.close()
    
file=open('my_new_file2.txt','w+')    #open
print(file.write("this is my first line")) #process   
file=open('my_new_file2.txt','r')
print(file.readlines())   #process
file.close()    #close