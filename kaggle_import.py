import csv
import psycopg2

username = 'Lutak01'
password = '1111'
database = 'lutak_db_lab3'

INPUT_CSV_FILE = 'F:\\players_fifa22.csv'
INPUT_CSV_FILE_2 = 'F:\\teams_fifa22.csv'

query_delete_1 = '''
DELETE FROM football_league
'''
query_delete_2 = '''
DELETE FROM football_team
'''
query_delete_3 = '''
DELETE FROM footballer
'''
query_name_league = '''
alter table football_league add constraint name_league_constraint unique (name_league)
'''
query_id_footballer = '''
alter table footballer add constraint id_footballer_constraint unique (id_footballer)
'''
query_1 = '''
INSERT INTO football_league (id_league, name_league) VALUES (%s, %s) ON CONFLICT (name_league) DO NOTHING
'''
query_2 = '''
INSERT INTO football_team (name_team, id_league, number_of_players) VALUES (%s, %s, %s)
'''
query_3 = '''
INSERT INTO footballer (id_footballer,  name_footballer, age) VALUES (%s, %s, %s) ON CONFLICT (id_footballer) DO NOTHING
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_delete_3)
    cur.execute(query_delete_2)
    cur.execute(query_delete_1)

    #cur.execute(query_name_league)
    #cur.execute(query_id_footballer)

    helper = {}
    with open(INPUT_CSV_FILE_2, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            values = (idx + 10000, row['League'])
            if row['League'] not in helper:
                helper[row['League']] = idx + 10000
            cur.execute(query_1, values)
            values_2 = ("Team" + str(idx), helper[row['League']], "25")
            cur.execute(query_2, values_2)
    conn.commit()

    helper_2 = {}
    with open(INPUT_CSV_FILE, 'r', encoding='utf-8') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            values_3 = (row['ID'], row['Name'], row['Age'])
            cur.execute(query_3, values_3)
    conn.commit()