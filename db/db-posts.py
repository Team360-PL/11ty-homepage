import mysql.connector
import os
from datetime import datetime
import re


def split_year(tag):
    x = re.search("(.*)(20\d\d)$", tag)
    if (x):
        return {x.group(1), x.group(2)}
    else:
        return tag

mydb = mysql.connector.connect(
  host="localhost",
  user="ebbe",
  password="ebbe"
)

cursor = mydb.cursor(dictionary=True,buffered=True)
query= 'SELECT nid, uid, title, created FROM team360.node where type="article" and nid > 12000 order by nid'
cursor.execute(query)
# myresult = mycursor.fetchall()
records = cursor.fetchall()
print("Total number of entries: ", cursor.rowcount)

print("\nPrinting each row")
for row in records:     

  title = row['title'].replace('"', '\'')
  postcursor = mydb.cursor(dictionary=True,buffered=True)
  query = 'SELECT * FROM team360.field_data_body where entity_id=' + str(row['nid']) + ';' 
  postcursor.execute(query)
  post = postcursor.fetchone()


  timestamp = row['created']
  dt_object = datetime.fromtimestamp(timestamp)

  query = 'SELECT uid, name FROM team360.users where uid=' + str(row['uid']) + ';' 
  postcursor.execute(query)
  usr = postcursor.fetchone()

  dt = dt_object.strftime("%Y-%m-%d")

  query = 'SELECT entity_id, tid, name FROM team360.field_data_field_tags \
        left join team360.taxonomy_term_data \
        on team360.taxonomy_term_data.tid=team360.field_data_field_tags.field_tags_tid \
        where team360.field_data_field_tags.entity_id=' + str(row['nid']) + ';' 

  postcursor.execute(query)
  tags = postcursor.fetchall()

  dt = dt_object.strftime("%Y-%m-%d")

  filename = "../posts/db/" + dt + ".md"
  if os.path.exists(filename):
    os.remove(filename)
  else:
    print("The file does not exist" + filename)
    
  f = open(filename, "a")

  f.write('---' + "\n")
  f.write('title: "' + title + '"' + "\n")
  f.write('short: ' + "\n")
  f.write('lead: ' + "\n")
  f.write('author: ' + usr['name'] + "\n")
  f.write('date: ' + dt + "\n")
  f.write('id: ' + str(row['nid']) + "\n")
  f.write('tags: '+ "\n")
  for tag in tags:    
   #for t in split_year(tag['name']):
   #   f.write('    - ' + t + "\n")
    f.write('    - ' + tag['name'] + "\n")
  f.write('coverImage: '+ "\n")
  f.write('coverImageCredits: '+ "\n")
  f.write('---' + "\n")

  f.write(post['body_value'])

#   xml = \
#         '<div xml:id="P_{nid}">' + "\n" \
#         '  <head>{title}</head>' + "\n" \
#         '  <date resp="Team_{uid}" when="' + dt_object.strftime("%Y-%m-%d") + '">' + usr['name'] + '</date>' + "\n" \
#         '  <div type="content">' +  "\n" \
#         + post['body_value'] + \
#         '  </div>' + "\n" \
#         '</div>' + "\n"
  #xml2 = xml.format(**row) 
  #f.write(xml2)

  
  f.close()
