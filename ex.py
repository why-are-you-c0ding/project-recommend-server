import pymysql
import pandas as pd
conn = pymysql.connect(host='localhost', user='root', password='an06270711', db='ai_db', charset='utf8')
cur = conn.cursor()


sql1 = "select * from item_ratings;"
cur.execute(sql1)

rat = cur.fetchall()

sql2 = "select * from items2;"
cur.execute(sql2)

items2 = cur.fetchall()


ratList = []
for i in rat:
    ratList.append({'userId':i[4], 'itemId':i[1], 'rating':i[2], 'tiemstamp':i[3] })

del ratList[0]


ratings = pd.DataFrame(ratList)

itemsList = []
for i in items2:
    itemsList.append({'itemId':i[2], 'title':i[3],'category':i[1] })

item = pd.DataFrame(itemsList)




# 오류 코드
# data = Dataset.load_from_df(ratings[['userId', 'itemId', 'rating']], reader)
# algo = SVD(n_factors=50, random_state=0)
# algo.fit(data)

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import warnings

from surprise import Reader

from surprise.dataset import DatasetAutoFolds



# Reader 객체 생성
reader = Reader(line_format='user item rating timestamp', sep=',', rating_scale=(0.5, 5))

# DatasetAutoFolds 객체 생성
data_folds = DatasetAutoFolds(ratings_file='C:\\Users\\asb07\\Desktop\\ItemRatings_noh.csv', reader=reader)

# 전체 데이터를 train으로 지정
trainset = data_folds.build_full_trainset()
trainset

from surprise import SVD

# SVD를 이용한 잠재 요인 협업 필터링 (잠재 요인 크기 = 50)
algo = SVD(n_epochs=20, n_factors=50, random_state=0)
algo.fit(trainset)

# 사용자 아이디, 아이템 아이디 문자열로 입력
uid = str(77)
iid = str(55)

# 추천 예측 평점 (.predict)
pred = algo.predict(uid, iid, verbose=True)

# 아직 보지 않은 아이템 리스트 함수
def get_unseen_surprise(ratings, item, userId):
     # 특정 userId가 평점을 매긴 모든 아이템 리스트
    seen_item = ratings[ratings['userId']== userId]['itemId'].tolist()

    # 모든 아이템명을 list 객체로 만듬. 
    total_item = item['itemId'].tolist()

    # 한줄 for + if문으로 안 본 아이템 리스트 생성
    unseen_item = [ movie for movie in total_item if movie not in seen_item]

    # 일부 정보 출력
    total_movie_cnt = len(total_item)
    seen_cnt = len(seen_item)
    unseen_cnt = len(unseen_item)

    print(f"전체 아이템 수: {total_movie_cnt}, 평점 매긴 아이템 수: {seen_cnt}, 추천 대상 아이템 수: {unseen_cnt}")

    return unseen_item


unseen_item = get_unseen_surprise(ratings, item, 9)


def recomm_movie_by_surprise(algo, userId, unseen_item, top_n=10):

    # 아직 보지 않은 아이템의 예측 평점: prediction 객체 생성
    predictions = []
    for itemId in unseen_item:
        predictions.append(algo.predict(str(userId), str(itemId)))

    # 리스트 내의 prediction 객체의 est를 기준으로 내림차순 정렬
    def sortkey_est(pred):
        return pred.est

    predictions.sort(key=sortkey_est, reverse=True) # key에 리스트 내 객체의 정렬 기준을 입력

    # 상위 top_n개의 prediction 객체
    top_predictions = predictions[:top_n]

    # 아이템 아이디, 제목, 예측 평점 출력
    print(f"Top-{top_n} 추천 아이템 리스트")


    for pred in top_predictions:

        movie_id = int(float(pred.iid))
        movie_title = item[item["itemId"] == movie_id]["title"].tolist()
        movie_rating = pred.est

        print(f"{movie_title}: {movie_rating:.2f}")


recomm_movie_by_surprise(algo, 3, unseen_item, top_n=10)