sentence="i like the name govind because the name govind is best name in name"

word_counts={
  'i':1,
  'name':3,
  'like': 1 ,
  'the': 2,
  
}
print(word_counts) #prints dictionary
#dict.item()-total items in dictionary
print(list(word_counts.items()))   #casted to list

#dict.keys()
print(list(word_counts.keys())) #prints keys
##dict.values( )
print(list(word_counts.values())) #prints values

#dict.pop(item)
word_counts.pop('i') #delete elemsnt from dictionary
print(word_counts)

word_counts.popitem() ##to delete last item
print(word_counts)

word_counts['govind']=2 #add to dict
print(word_counts)

#word_counts.clear() ##clears full dict
print(word_counts)

#sorting dictionaires  in terms of va;ues
print((sorted(list(word_counts.values())))) #sorted list
print(dict(sorted(list(word_counts.items())))) 
