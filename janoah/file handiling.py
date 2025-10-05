# file handiling allows us to store data permanently in files and retrive it when needed python
#  provides buit in factors to work with files make it easy to read and write
# type of files
# text files store dadta in hukman readable from txt
# binary file:store data in byte form (bin,images audios etc)
# r=read,open file for reading
# w=write,open file for writing
# a=append,
# b=binary,
# x=exclusive,
# r+read+write,open file for both
# t=text defalt ode for text


# f=open("data.txt","r") #open in read mode
# # writing a data
# # write()writes a single string to the File.
# # example
# f=open("data.txt","w")
# f.write("hello,Python!\n")

# writelines=writes a list of strings to the file 
f=open("data.txt","w")
f.writelines(["line1\n","line2\n"])
f.close()

# reading data from a File.
# reads the whole file 
f=open("data.txt","r")
print(f.read())
print(f.read(5))

# readline() read one line at a time
f=open("data.txt","r")
print(f.readline())
print(f.readline())


f=open("data.txt","r")
lines=f.readlines()
print(lines)
f.close()

# Random access file operations
# tell()returns current file pointer position

# seek (offset  from where) move file pointer to a specific position
# example:
f=open("data.txt","r")
print(f.read(5))
print("pointer at:",f.tell())
f.seek(0)
print(f.read(5))
f.close()