import os
import keep_alive
import scratchattach as scratch3
from replit import db

keep_alive.keep_alive()

sessionID = os.environ["sessionID"]

session = scratch3.Session(sessionID , username="LoIdesMio")
conn = session.connect_cloud("750893980")
client = scratch3.CloudRequests(conn)

db_keys = db.keys()

@client.request
def save(argument1 , argument2):  
  db[argument1] = argument2
  print(db_keys)


@client.request
def load(argument1):
 name = argument1
 db_keys = db.keys()
 if name in db_keys:
  coins = db[argument1]
  return(coins)
  print(db_keys)
 else:
  return("FAIL")
  print(db_keys)


   

client.run()