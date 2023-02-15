# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):

    result = ""  # 값을 저장할곳

    for letter in word:  # 문자 하나하나 씩 검사
        if letter.islower():  # 만약 소문자이면?
            asc_num = ord(letter) + n  # 숫자코드로 변환후 n만큼 더한값을 미리 저장
            if asc_num > 122:  # 그 값이 z범위를 넘어서면
                asc_num = asc_num - 26 ## -26(알파벳이 26개)으로 뒤로 넘어가 소문자 a부터 다시 진행
        
        # z 범위를 안넘으면 그대로 진행

        else: # 만약 대문자라면?
            asc_num = ord(letter) + n # 소문자와 동일하게 진행
            if asc_num > 90: # Z 의 아스키코드 값을 넘어서면
                asc_num = asc_num - 26

        result += chr(asc_num)  # 다시 아스키코드를 문자로 변환후 하나씩 저장

    return result # 결과 리턴
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
