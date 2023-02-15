# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def min_max(scores):
    min_value = 9999   # 시작 min 값을 매우 큰 값을 줌 점수는 100점이 최대일테니 9999 정도면 충분
    max_value = -9999   # 시작 max 값을 매우 작은 값을 줌 점수는 0점이 최소 일테니 -9999 정도면 충분

    for score in scores: # 하나씩 검사
        if score < min_value :   # min 값이 작으면 다시 설정
            min_value = score
        if score > max_value :   # max 값이 크면 다시 설정
            max_value = score

    result = (min_value,max_value)   # 결과 튜플로

    return result   # 결과 리턴
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
