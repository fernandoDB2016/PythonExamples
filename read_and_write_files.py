# Example on how to read and write files

# Write/create a file
# First we define a file object, so we define a variable.
# Using the open() function, open a file, prepare a file to be written or created.

file_write = open('suspicious_file.txt', 'w')
file_write.write('This is an example on how to write into a file\n')
file_write.write('this is really cool\n')
file_write.close()

# Read a file
# First we open the file. As we python can not work directly with the content of file,
# for that we create a variable 'text' to store the content of the file and from
# there we can print the content for example

file_read = open('suspicious_file.txt', 'r')
text = file_read.read()
print(text)
file_read.close()

# Reading a text file from Internet



