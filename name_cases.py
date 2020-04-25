guests = ['john', 'ban','mike']
print(guests)

message = guests[0]
print(message)

message = guests[1]
print(message)

message = guests[2]
print(message)

guests[0]='like'
print(guests)
message = guests[0]
print(message)

message = guests[1]
print(message)

message = guests[2]
print(message)

guests.insert(0,'john')
print(guests)

guests.insert(2,'joshua')
print(guests)

guests.append('fire')
print(guests)



message = guests.pop(0)
print("I am sorry I can not invite " + message.title() + " for dinner." )


message = guests.pop(0)
print("I am sorry I can not invite " + message.title() + " for dinner." )

message = guests.pop(0)
print("I am sorry I can not invite " + message.title() + " for dinner." )

message = guests.pop(0)
print("I am sorry I can not invite " + message.title() + " for dinner." )

print(guests)


del guests[0]
del guests[0]
print(guests)