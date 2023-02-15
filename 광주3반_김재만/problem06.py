# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def over_24(people):

    cnt = 0  # 24 세 이상인 사람 수를 카운트 하므로 카운트변수생성

    for person in people:   # people 리스트를 돌며 한사람씩 검사
        if person.get('age') > 24:  # 딕셔너리내 age값이 24 초과이면 cnt 1씩 증가
            cnt += 1

    return cnt  # cnt 를 리턴
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    people = [
        {'name': '김싸피', 'age': 25},
        {'name': '이싸피', 'age': 28},
        {'name': '조싸피', 'age': 29},
        {'name': '아싸피', 'age': 23},
        {'name': '최싸피', 'age': 22},
        {'name': '고싸피', 'age': 21},
        {'name': '유싸피', 'age': 26},
        {'name': '후싸피', 'age': 20},
    ]

    print(over_24(people))  # 4