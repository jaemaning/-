# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 len 사용 금지
def title_length(movie):

    cnt = 0 # len 함수 사용 불가로 직접 세기위해 cnt 변수 만듬

    for _ in movie.get('title'):  ## 제목을 가져와 string형식을 그대로 for문
        cnt += 1  # 제목 길이 만큼 cnt 증가

    return cnt  # 제목 길이를 센 횟수인 cnt 변수 리턴
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    movie = {
            "id": 1,
            "user_rating": 8.1,
            "title": "그리고 내일",
            "overview": "과거보다 더 성장한 당신은 드디어 꿈을 이루게 된다.",
        }

    print(title_length(movie))  # 6 (공백 포함 길이)