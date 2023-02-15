# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    result = sum(scores) / len(scores)  ## sum함수로 리스트 내 값 전부 합산 후 , 리스트 내 자료 갯수만큼 나누어 평균 계산
    return result
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores))    # 82.5