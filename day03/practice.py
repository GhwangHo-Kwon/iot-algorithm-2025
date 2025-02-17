# # da02_practice.py

# ## 클래스와 함수 선언 부분 ##
# class Node():
#     def __init__(self):
#         self.data = None
#         self.link = None

# def printNodes(start):
#     current = start
#     if current == None:
#         return
#     print(current.data, end=' ')
#     while current.link != None:
#         current = current.link
#         print(current.data, end=' ')
#     print()

# def makeSimpleLinkedList(namePhone):
#     global memory, head, current, pre
#     printNodes(head)

#     node = Node()
#     node.data = namePhone
#     memory.append(node)
#     if head == None:        # 첫번째 노드일 때
#         head = node
#         return
    
#     if head.data[0] > namePhone[0]:  # 첫번째 노드보다 작을 때
#         node.link = head
#         head = node
#         return

#     # 중간 노드로 삽입하는 경우
#     current = head
#     while current.link != None:
#         pre = current
#         current = current.link
#         if current.data[0] > namePhone[0]:
#             pre.link = node
#             node.link = current
#             return
    
#     # 삽입하는 노드가 가장 큰 경우
#     current.link = node

# ## 전역 변수 선언 부분
# memory = []
# head, current, pre = None, None, None
# dataArray = [['지민', '010-1111-1111'], ['정국', '010-2222-2222'],
#              ['뷔', '010-3333-3333'], ['슈가', '010-4444-4444'],
#              ['진', '010-5555-5555']]

# ## 메인 코드 부분
# if __name__ == '__main__':

#     for data in dataArray:
#         makeSimpleLinkedList(data)

#     printNodes(head)

#####################

# import webbrowser
# import time

# ## 함수 선언 부분
# def isStackFull(): # 스택이 꽉 찼는지 확인하는 함수
#     global SIZE, stack, top
#     if (top == SIZE - 1): # Full / 실무에서 쓰는 스택은 거의 무제한
#         return True
#     else:
#         return False
    
# def isStackEmpty():  # 스택이 비었는지 확인
#     global SIZE, stack, top
#     if (top == -1): # Empty
#         return True
#     else:
#         return False

# def push(data):  # 스택에 데이터 추가
#     global SIZE, stack, top
#     if isStackFull(): # isStackFull() == True와 동일
#         print('Stack is full!')
#         # return 생략
#     else:
#         top += 1
#         stack[top] = data

# def pop(): # 스택에서 데이터 추출
#     global SIZE, stack, top
#     if isStackEmpty():
#         print('Stack is empty.')
#         return None
#     else:
#         data = stack[top]
#         stack[top] = None
#         top -= 1
#         return data

# def peek():  # 스택의 top위치의 데이터 확인(살짝보기)
#     global SIZE, stack, top
#     if isStackEmpty():
#         print('Stack is empty.')
#         return None
#     else:
#         return stack[top]

# ## 전역 변수 선언 부분
# SIZE = 100
# stack = [None for _ in range(SIZE)]
# top = -1

# ## 메인 코드 부분
# if __name__ == '__main__':
#     urls = ['naver.com', 'daum.net', 'nate.com']

#     for url in urls:
#         push(url)
#         webbrowser.open('http://'+url)
#         print(url, end='-->')
#         time.sleep(1)
    
#     print('방문 종료')
#     time.sleep(5)

#     while True:
#         url = pop()
#         if url == None:
#             break
#         webbrowser.open('http://'+url)
#         print(url, end='-->')
#         time.sleep(1)
    
#     print('방문 종료')

#####################

# def checkBracket(expr):
#     for ch in expr:
#         if ch in '([{<':
#             push(ch)
#         elif ch in '>}])':
#             out = pop()
#             if ch == ')' and out == '(':
#                 pass
#             elif ch == ']' and out == '[':
#                 pass
#             elif ch == '}' and out == '{':
#                 pass
#             elif ch == '>' and out == '<':
#                 pass
#             else:
#                 return False
#         else:
#             pass
#     if isStackEmpty():
#         return True
#     else:
#         return False

# ## 전역 변수 선언 부분
# SIZE = 100
# stack = [None for _ in range(SIZE)]
# top = -1

# if __name__ == '__main__':

#     exprAry = ['(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']
#     for expr in exprAry:
#         top = -1
#         print(f'{expr} ==> {checkBracket(expr)}')

#####################

import random

## 함수 선언 부분
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False
    
def push(data):
    global SIZE, stack, top
    if isStackFull():
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if isStackEmpty():
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if isStackEmpty():
        return None
    return stack[top]

## 전역 변수 선언 부분
SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1

## 메인 코드 부분
if __name__ == '__main__':

    stoneAry = ['빨강', '파랑', '초록', '노랑', '보라', '주황']
    random.shuffle(stoneAry)

    print('과자집에 가는길 : ', end=' ')
    for stone in stoneAry:
        push(stone)
        print(stone, '-->', end=' ')
    print('과자집')

    print('우리집에 오는길 : ', end=' ')
    while True:
        stone = pop()
        if stone == None:
            break
        print(f'{stone} -->', end=' ')
    print('우리집')