# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
# s=''
def dec_to_bin(number):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    global s
    s=''
    if number==0:
        return 
    dec_to_bin(number//2)
    s+=str(number%2)
    return s
    
    


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010