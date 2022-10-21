def recomm_movie_by_surprise(algo, userId, unseen_item, item, top_n=10):

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