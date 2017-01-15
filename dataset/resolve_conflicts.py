"""
resolving conflicts in Wypozyczenia
it's only a draft, but it works
"""

import MySQLdb
import datetime

f = '%Y-%m-%d %H:%M:%S'

conn = MySQLdb.connect(user="root", database="bd3")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(id), wolumen_id FROM wypozyczenie GROUP BY wolumen_id")

multiples = set()

"""find wolumens for which there is more than 1 wypozyczenie"""
for row in cursor:
    if(row[0] > 1):
        multiples.add(row[1])


print(multiples)


def find_conflicts(rows):
    to_delete_ids = []
    n = len(rows)
    for i in range(n):
        stop_date = rows[i][2]
        for j in range(i+1, n):
            if stop_date - rows[j][1] > datetime.timedelta(0):  # wypozyczenie 2 przed zwrotem 1
                to_delete_ids.append(rows[j][0])
            else:
                break
    return to_delete_ids


to_delete_ids = []

for m in multiples:  # every wolumen
    cursor.execute("SELECT id, data, data_zwrotu, wolumen_id FROM wypozyczenie WHERE wolumen_id={} ORDER BY data".format(m))
    rows = []
    for row in cursor:
        rows.append(row)
    to_delete_ids += find_conflicts(rows)

with open("conflicts.sql", "w") as f:
    for i in to_delete_ids:
        f.write("delete from Wypozyczenie where ID={};\n".format(i))

conn.close()
