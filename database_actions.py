__author__ = 'Justin'

# ===========================================================================
# Database actions
# ===========================================================================

import pycurl
import json

print "Press CTRL+Z to exit"

db_database = 'iotdb_mongodb'
db_collection = 'events'
db_api_key = '5245ce77b91a11a1100003b9'
db_url = 'https://api.mongolab.com/api/1/databases/' + db_database \
         + '/collections/' + db_collection \
         + '?apiKey=' + db_api_key

while True:
    print("Inserting a new document.")

    data = json.dumps({"temperature": 99})
    c = pycurl.Curl()
    c.setopt(pycurl.URL, db_url)
    c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.perform()

    print("Insert complete.")