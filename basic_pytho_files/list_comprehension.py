names=['ditto','naveen','joseph','midhun']    #names in list

l=[]  #empty list

for person in names: #simple way to append to new list
  l.append(person)
print(l)

print([person for person in names] ) #list comprehension same as above but single line

#operations
l=[]

for person in names: #simple way to append to list
  l.append(person + ' dumped me')
print(l)

print([person +' dumped me' for person in names] ) 

movies_and_rating ={"dark knight":5,"intersteller":9,"tom rider":6,"50 shades":3,"wonder women":4}

##appending movies with rating greater than 6 to new list
l=[]
for movies in movies_and_rating:
  if movies_and_rating[movies]>=6:
    l.append(movies)
print(l)

##same as above but single line
print([movies for movies in movies_and_rating if movies_and_rating[movies]>=6])

