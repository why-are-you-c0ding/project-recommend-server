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