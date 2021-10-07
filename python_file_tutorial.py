

# In the following example, assume we have a file called "filename.txt" which has 10 lines in it.
# We only want to keep the even lines, so discard the odd ones.

file = open("filename_ex.txt", "r")

outfile = ""

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("filename_ex.txt", "w")
file.write(outfile)
file.close()

# The outfile is the variable in which we are storing the data we wish to keep.
# The readline in the else statement skips the lines which are odd.


