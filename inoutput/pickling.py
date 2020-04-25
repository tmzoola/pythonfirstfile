import pickle

# imelda = ("More Mayhem",
#          "IMelda May",
#           "2011",
#           ((1, "Pulling the Rug"),
#            (2, "Psycho"),
#            (3, "Mayhem"),
#            (4, "Kentish Town")))
# with open("C:/Users/user/Downloads/imelda2.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file )


# with open("C:/Users/user/Downloads/imelda2.pickle", 'rb') as imelda_pickle:
#      imelda2 = pickle.load(imelda_pickle)
#
#
# album, artist, year, track_list = imelda2
#
# print(album)
# print(artist)
# print(year)
#
# for track2 in track_list:
#     track2_num, track2_title = track2
#     print(track2_num, track2_title)

imelda = ("More Mayhem",
         "IMelda May",
          "2011",
          ((1, "Pulling the Rug"),
           (2, "Psycho"),
           (3, "Mayhem"),
           (4, "Kentish Town")))
even = list(range(0,10,2))
odd = list(range(1,10,2))

with open("C:/Users/user/Downloads/imelda2.pickle", 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=0)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=0)
    pickle.dump('2998302', pickle_file, protocol=0)

with open("C:/Users/user/Downloads/imelda2.pickle", 'rb') as imelda_pickle:
     imelda2 = pickle.load(imelda_pickle)
     even_list = pickle.load(imelda_pickle)
     odd_list = pickle.load(imelda_pickle)
     x = pickle.load(imelda_pickle)

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)

for track2 in track_list:
    track2_num, track2_title = track2
    print(track2_num, track2_title)


print("=" * 40)
for i in even_list:
    print(i)

print("=" * 40)
for i in odd_list:
    print(i)

print("=" * 40)
print(x)