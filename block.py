import pymysql
import secret


def read_block_item(user_id):
    conn = pymysql.connect(host='localhost', user='root', password=secret.PASSWORD, db='ai_db', charset='utf8')
    cur = conn.cursor()
    sql1 = "select genres from item as i join block as b on b.item_id = i.item_id where b.user_id = %s order by b.id desc limit 1"
    cur.execute(sql1,(user_id))
    genres = cur.fetchone()[0];
    return genres.split('|')[0].strip()

def create_block_item(item_id, user_id):
    conn = pymysql.connect(host='localhost', user='root', password=secret.PASSWORD, db='ai_db', charset='utf8')
    cur = conn.cursor()
    query = "insert into block (item_id, user_id) values (%s, %s)"
    cur.execute(query, (item_id, user_id))
    cur.close();
    conn.commit();
    conn.close();
