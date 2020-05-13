#dictionary
from collections import OrderedDict

##python 3.7 onwars dictionaires keep a specific order in which it was created
contacts={'joe':{'phone':'165-456-7809','email':'joe@gamil.com'},
'john':'674564891'}
print(contacts) ##prints dictionary
print(contacts.get('joe').get('phone')) ##prints joe's phone number

