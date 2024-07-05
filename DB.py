# sozdayom BD
import sqlite3

# podklyuceniye k BD
conn = sqlite3.connect("delivery.db", check_same_thread=False)

# python + sql
sql = conn.cursor()

# sozdaniye tablitsi usera
sql.execute('CREATE TABLE IF NOT EXISTS users''(id INTEGER, name TEXT, number TEXT);')

# sozdaniye tablisti produktov
sql.execute('CREATE TABLE IF NOT EXISTS products''(pr_id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'pr_name TEXT, pd_desc TEXT, pr_price REAL, pr_count INTEGER, pr_photo TEXT);')

#sozdayom tablitsu karzini
sql.execute('CREATE TABLE IF NOT EXISTS card''(user_id INTEGER, user_products TEXT, user_pr_quantity INTEGER);')

##metodi dlya polzovatelya
# registratsiya

def register(user_id, user_name, user_num):
    sql.execute('INSERT INTO users VALUES (?,?,?);',(user_id, user_name, user_num))



#proverka polzovatelya na naliceye v BD
def check_user(user_id):
    if sql.execute('SELECT * FROM users WHERE id=?;',(user_id,)).fetchone():
        return True
    else:
        return False

# fiksiruem izmeneniya
conn.commit()