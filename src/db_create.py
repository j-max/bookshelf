import psycopg2

conn=psycopg2.connect(dbname='book_list')
cursor = conn.cursor()

drop_books= "DROP TABLE IF EXISTS books;"
drop_authors= "DROP TABLE IF EXISTS authors;"

create_table_authors= '''
CREATE TABLE authors 
(
    author_id SERIAL primary KEY,
    first_name CHAR(50),
    middle_name CHAR(50),
    last_name CHAR(50)
);
'''

query2 = '''
CREATE TABLE books
(
    book_id SERIAL primary KEY,
    author_id INT,
    title CHAR(100),
    publication_date int, 
    input_date DATE NOT NULL DEFAULT CURRENT_DATE,
    pages INT,
    CONSTRAINT fk_author
       FOREIGN KEY(author_id)
           REFERENCES authors(author_id)
);
'''


cursor.execute(drop_books)
conn.commit()

cursor.execute(drop_authors)
conn.commit()
 
cursor.execute(create_table_authors)
conn.commit()

cursor.execute(query2)
conn.commit()
 
