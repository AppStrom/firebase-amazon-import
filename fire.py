#!.\firebase\Scripts\python.exe

import firebase_admin
import json

from firebase_admin import credentials, firestore
cred = credentials.Certificate("service_account.json")
firebase_admin.initialize_app(cred)

firestore_db = firestore.client()

# add data
#firestore_db.collection(u'songs').add({'song': 'Imagine', 'artist': 'John Lennon'})

# read data
# snapshots = list(firestore_db.collection(u'amazon-products').get())
# for snapshot in snapshots:
#     tSnapshot = snapshot.to_dict()
#     #print(json.dumps(tSnapshot, indent=2))
#     print(tSnapshot['asin'])


# Using readline()
file1 = open('meta_All_Beauty.json', 'r')
count = 0

while count < 100:
    count += 1

    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break

    jsonLine = json.loads(line)
    #print(json.dumps(jsonLine, indent=2))
    print(jsonLine['category'])
    #print("Line{}: {}".format(count, line.strip()))

file1.close()
