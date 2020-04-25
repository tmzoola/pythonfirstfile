# jabber = open("C:/Users/user/Downloads/original.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line,end='')
#
# jabber.close()

# with open("C:/Users/user/Downloads/original.txt", 'r') as jabber:
#     for line in jabber:
#         if "jab" in line.lower():
#             print(line, end='')

# with open("C:/Users/user/Downloads/original.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

with open("C:/Users/user/Downloads/original.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line,end='')