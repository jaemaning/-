# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    # 이동한 위치
    nx = position[0] + dx[M]
    ny = position[1] + dy[M]

    # 이동한 위치가 사각틀을 벗어날 경우 False
    if nx <= -1 or ny <= -1 or nx+1 > N or ny+1 > N:
        return False

    # 아니라면 True
    return True

    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
