# pr01_compare_select_and_quick.py
import random
import time

## 클래스와 함수 선언 부분
def selectionSort(ary):
    n = len(ary)
    for i in range(n-1):
        minIdx = i
        for j in range(i+1, n):
            if ary[minIdx] > ary[j]:
                minIdx = j
        
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
        # ary[i], ary[minIdx] = ary[minIdx], ary[i]

    return ary

def qSort(arr, start, end):
    if end <= start:
        return
    low = start
    high = end

    pivot = arr[(low + high) // 2]   # 작은 값은 왼쪽, 큰 값은 오른쪽으로 분리
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1
    
    qSort(arr, start, low-1)
    qSort(arr, low, end)

def quickSort(ary):
    qSort(ary, 0, len(ary)-1)

## 메인 코드 부분
countAry = [1000, 10000, 12000, 15000]

for count in countAry:
    tempAry = [random.randint(10000, 99999) for _ in range(count)]
    selectAry = tempAry[:]
    quickAry = tempAry[:]

    print(f'## 데이터 수 : {count}개')
    start = time.time()
    selectionSort(selectAry)
    end = time.time()
    print(f'  선택 정렬 -> {(end-start):10.3f}초')
    start = time.time()
    quickSort(selectAry)
    end = time.time()
    print(f'    퀵 정렬 -> {(end-start):10.3f}초')
    print()

    count *= 5