import pymysql
import pandas as pd
import unseen
import recommend

import secret

from surprise import Reader
from surprise.dataset import DatasetAutoFolds
from surprise import SVD

def recomm_items(user_id):
    conn = pymysql.connect(host='localhost', user='root', password=secret.PASSWORD, db='ai_db', charset='utf8')
    cur = conn.cursor()


    sql1 = "select item_id, rating, timestamp, user_id from item_rating"
    cur.execute(sql1)

    rat = cur.fetchall()

    sql2 = "select genres, item_id, title from item;"
    cur.execute(sql2)

    items2 = cur.fetchall()


    ratList = []
    for i in rat:
        ratList.append({'userId':i[3], 'itemId':i[0], 'rating':i[1], 'tiemstamp':i[2] })

    del ratList[0]


    ratings = pd.DataFrame(ratList)

    itemsList = []
    for i in items2:
        itemsList.append({'itemId':i[1], 'title':i[2],'category':i[0] })

    item = pd.DataFrame(itemsList)
    reader = Reader(line_format='user item rating timestamp', sep=',', rating_scale=(0.5, 5))

    # DatasetAutoFolds 객체 생성
    data_folds = DatasetAutoFolds(ratings_file=secret.FILE_PATH, reader=reader)

    # 전체 데이터를 train으로 지정
    trainset = data_folds.build_full_trainset()
    trainset

    algo = SVD(n_epochs=20, n_factors=50, random_state=0)
    algo.fit(trainset)

    # 사용자 아이디, 아이템 아이디 문자열로 입력
    #uid = str(77)
    #iid = str(55)

    # 추천 예측 평점 (.predict)
    #pred = algo.predict(uid, iid, verbose=True)


    unseen_item = unseen.get_unseen_surprise(ratings, item, 9)

    return recommend.recomm_movie_by_surprise(algo, user_id, unseen_item, item, top_n=10)




