"""
att_nam = set()

cnt = int(input("how many attendees: "))
for i in range(cnt):
    att_nam.add(input("enter antendees: "))

print(att_nam)
"""

your_playlist = set({
    "All I Want for Christmas is You",
    "Silent Night, Holy Night",
    "Star ng Pasko",
    "Pasko na Sinta Ko",
})

friend_playlist = set({
    "Baby, It's Cold Outside",
    "All I Want for Christmas is You",
    "Kampana ng Simbahan",
    "Christmas Bonus",
})

#print(your_playlist.union(friend_playlist))
#print(your_playlist | friend_playlist)

#print(your_playlist.intersection(friend_playlist))
#print(your_playlist & friend_playlist)

#print(your_playlist.difference(friend_playlist))
#print(your_playlist - friend_playlist)

#print(your_playlist.symmetric_difference(friend_playlist))
#print(your_playlist ^ friend_playlist)