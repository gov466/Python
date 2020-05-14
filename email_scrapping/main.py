import re
text='random5614561 string bob.mndy@gmail.com bobg@gmail.com iam.m@comoany.com govind-raj@gmail.com very bad at programming.ing@yahoo.in'
pattern= re.compile('A random string')
result=pattern.search(text)
print(result)

pattern= re.compile('[ABC]')
result=pattern.search(text)
print(result)

pattern= re.compile('[rdm]')
result=pattern.search(text)
print(result)

pattern= re.compile('[c-mC-M]') #both uppercase and lower case
result=pattern.search(text)
print(result)

pattern= re.compile('[a-zA-Z]+') #both uppercase and lower case 
result=pattern.search(text)
print(result)

pattern= re.compile('[a-zA-Z0-9]+') #both uppercase and lower case 
result=pattern.search(text)
print(result)

pattern= re.compile(' [a-zA-Z0-9]+@[a-zA-Z0-9]+\.+[a-zA-Z0-9]+') #both uppercase and lower case 
result=pattern.search(text) #search gives only a single mail address
print(result)

pattern2= re.compile('[a-zA-Z0-9\.\_\-]+@[a-zA-Z0-9]+\.+[a-zA-Z0-9]+') #both uppercase and lower case 
result=pattern2.findall(text) ##finall searches for all mail id
print(result) ##


##output

<re.Match object; span=(0, 1), match='r'>
<re.Match object; span=(3, 4), match='d'>
<re.Match object; span=(0, 6), match='random'>
<re.Match object; span=(0, 13), match='random5614561'>
<re.Match object; span=(39, 54), match=' bobg@gmail.com'>
['bob.mndy@gmail.com', 'bobg@gmail.com', 'iam.m@comoany.com', 'govind-raj@gmail.com', 'programming.ing@yahoo.in']
