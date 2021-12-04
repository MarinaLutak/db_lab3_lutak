import psycopg2
import matplotlib.pyplot as plt

username = 'Lutak01'
password = '1111'
database = 'lutak_db_lab2'
host = 'localhost'
port = '5432'

query_1 = '''
create view AgeFootballer as
select trim(name_footballer), age from footballer
'''
query_2 = '''
create view FrequencyFootballer as
select trim(name_team), count(footballer.name_team) as pie_team from football_team left join footballer using(name_team) group by name_team
'''
query_3 = '''
create view NumberFootballer as
select number_of_players, trim(name_team) from football_team
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    cur.execute('drop view if exists AgeFootballer')
    cur.execute(query_1)
    cur.execute('select * from AgeFootballer')
    footballer = []
    age = []
    for row in cur:
        footballer.append(row[0])
        age.append(row[1])
    plt.bar(footballer, age, width=0.5)
    plt.xticks(rotation=15)
    plt.title('Вік футболістів')
    plt.xlabel('Футболіст')
    plt.ylabel('Вік')
    plt.show()

    cur.execute('drop view if exists FrequencyFootballer')
    cur.execute(query_2)
    cur.execute('select * from FrequencyFootballer')
    name_team = []
    num = []
    for row in cur:
        name_team.append(row[0])
        num.append(row[1])
    plt.pie(num, labels=name_team, autopct='%1.1f%%')
    plt.title('Частка футболістів, що грають за команду')
    plt.show()

    cur.execute('drop view if exists NumberFootballer')
    cur.execute(query_3)
    cur.execute('select * from NumberFootballer')
    name_team = []
    number_of_players = []
    for row in cur:
        name_team.append(row[0])
        number_of_players.append(row[1])
    plt.plot(number_of_players, name_team, marker='o')
    plt.title('Кількість футболістів в команді')
    plt.show()

