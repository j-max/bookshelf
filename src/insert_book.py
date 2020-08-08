import psycopg2

conn=psycopg2.connect(dbname='book_list')
cursor = conn.cursor()

# not certain this is necessary
# trying to automate input
table_name = 'books'
col_names_query = f"""select column_name
                      from information_schema.columns 
                      where table_name ='{table_name}'"""


cursor.execute(col_names_query)

names = cursor.fetchall()

title = input('What is the title of the book\n>>>')
publication_date =  int(input('What is the publication year of the book\n>>>'))
length = int(input('What is the length in pages of the book\n>>>'))

# This will be turned into a prompt
query = f"""
INSERT INTO books(title, publication_date, pages) 
VALUES({title, publication_date, length});
"""

cursor.execute(query)
conn.commit()
