# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):

    if len(numbers) == 0 :
        return 0  # 만약 아무것도 들어오지 않는다면 0리턴

    elif len(numbers) == 1:  # 들어온 입력값 numbers 길이가 1이라면
        result = (numbers[0] **2) * 3.14  # 원의 넓이 계산 튜플형태로 받으므로 0번째 인덱스 슬라이싱
    
    elif len(numbers) == 2:  # 들어온 입력값 numbers 길이가 2라면
        if (numbers[0] + numbers[1]) % 2 == 0: # 두 입력값의 합이 짝수라면
            result = numbers[0] * numbers[1]  # 사각형의 넓이
        else: # 두 입력값의 합이 홀수라면
            result = (numbers[0] * numbers[1]) / 2 # 삼각형 넓이

    else:  # 들어온 입력값 numbers가 3개 이상일 때
        sum_value = sum(numbers)  # 총 합
        avg_value = sum_value / len(numbers)  # 평균
        result = (sum_value,avg_value)  # 튜플로 저장

    return result #결과 리턴
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0