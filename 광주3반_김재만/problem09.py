# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):

    if number == 1 :  ## 나머지 or number 목으로 나누어 끝까지 간경우
        return 1  # 1을 리턴
    if number == 0 :  ## 나머지가 0인경우
        return 0  # 0을 리턴

    return str(dec_to_bin(number//2)) + str(dec_to_bin(number%2))  # 스트링자료형으로 차곡차곡 쌓기.
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
