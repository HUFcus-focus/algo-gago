"""
문제 :
- N*M 크기의 2차원 배열에서 메뉴얼에 따라 특정 위치의 캐릭터를 이동시킨 횟수 카운팅
- 배열은 육지(0)와 바다(0)로 이루어져있다( 바다로는 전진할 수 없다 )
- 움직임 메뉴얼 :
  1) 바라보는 방향에서 왼쪽 방향으로 회전
  2) 1칸 전진
  3) 이미 방문한 칸이라면 전진X, 왼쪽 방향으로 회전, 다시 1)로 회귀
  4) 사방이 모두 전진할 수 없다면 1칸 후진, 1)로 회귀
  5) 뒤가 바다라면 종료
- 풀이 :
  1) 메뉴얼을 상황에 따라 분기하여 조건문을 걸 수 있는 부분을 찾는다
     -> 1) > 2) > 3,4,5 > 1 or 종료
  2) 방향벡터를 사용하여 방향에 따른 움직임을 좌표이동으로 표현한다
  3) 방문여부를 판단하기 위한 2차원 배열을 만들어 사용한다
"""
#입력
n,m = map(int, input().split())
x,y,d = map(int,input().split())
area = []
for i in range(n):
  area[i].append(list(map(int,input().split)))

#풀이2. 방향에 따른 좌표이동을 표현한다
#해당 축의 이동 리스트의 인덱스와 방향은 일치한다
directions = [0,1,2,3]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#풀이3. 방문여부를 판단하기 위한 배열을 생성하여 사용한다
visited = [[0]*m for _ in range(n)]
count = 0 #방문한 칸의 횟수
cant = 0  #연속적으로 전진할 수 없는 횟수

#풀이1. 메뉴얼을 분기할 수 있는 부분을 찾아 조건문을 건다
while(1): #더이상 움직일 수 없을때까지 반복한다
  d = directions[d-1] #방향회전은 방향리스트[현재방향-1]이다
  if visited[x+dx[d]][y+dy[d]] == 0 and area[x+dx[d]][y+dy[d]] == 0: #방문한적없는 육지
    x += dx[d]
    y += dy[d]
    visited[x+dx[d]][y+dy[d]] = 1
    count += 1
    cant = 0
  else: #이미방문했거나 바다이거나 둘다인 경우
    if cant == 4: #사방이 모두 전진할 수 없는 경우
      if area[x-dx[d]][y-dy[d]] == 1: #후진할 수 없는 경우
        break
      else: #후진할 수 있는 경우
        x -= dx[d]
        y -= dy[d]
        count += 1
        cant = 0
    cant += 1
    d = directions[d-1]

#출력
print(count)