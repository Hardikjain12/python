'''
1) r+ = open for read and write. The pointer is positoned at begning of file 
        it means it overwrite in starting of file 

'''
# f = open("h.txt","r+")
# f.write("ABC")
# print(f.read())
# f.close()

'''
2) w+ = open for reading and writing . The the file get complete truncate(wiped out hogi)
'''
# f = open("h.txt","w+")
# # f.write("ABC")
# print(f.read())
# f.close()

'''
3) a+ = open for reading and writing . The pointer is positioned at end of the file
'''

f = open("h.txt","a+")
# f.write("ABC")
print(f.read())
f.write("ABC")
f.write("harik dmsnzx ")
f.close()