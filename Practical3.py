# Taking input of size of each group
K = int(input('\nEnter the size of each group::'))

# Taking input of room number list(string)
room_no = input('\nEnter the room list::')

# converting room number string to list
roomlist=[int(i) for i in room_no.split()]

# fetching all unqiue room number from list using set 
rooms = set(roomlist)

# searching element with single count in roomlist
for val in rooms:
    count = roomlist.count(val)
    if count == 1:
        print('\nCaptain\'s Room number::'+str(val))
        break
    