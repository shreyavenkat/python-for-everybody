# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
li = list()
di = dict()
char = 'From '
for line in handle:
    if char in line:
        address = line.split()
        addr = str(address[1])
        if addr not in li:
            li.append(addr)
            di[addr] = 1
        else:
            di[addr] += 1
maxi = 0
maxKey = ''
for key in di:
    if di[key] > maxi:
        maxi = di[key]
        maxKey = key
print(maxKey, maxi)          
        
