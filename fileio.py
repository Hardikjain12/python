f = open("demo.txt","r")

# READ MODE

# data = f.read()
# print(data)
# print(type(data))
# particular_charcter_set = f.read(7)
# print(particular_charcter_set)
# read_linebyline = f.readline()
# print(read_linebyline)
f.close()

# WRITE MODE

'''
in this we hv two mode 

1 w = it is used to overwrite the whole entire data
2 a = it is appened mode it adds to the  file in last 

'''
g = open("sample.txt","w")
g.write(" hardik is a bad boy ")

g = open("sample.txt", "a")
g.write("\nbut hardik is superchill and good looking handsome guy")


# if we open file in w or a mode and the file not exit pyhton will create that file

s = open("h.txt","w")






# -------------------------------------------------