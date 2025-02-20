# pr03_middleMoney.py
## 클래스와 함수 선언 부분
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for j in range(i+1, n):
            if ary[minIdx] > ary[j]:
                minIdx = j
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
        # ary[i], ary[minIdx] = ary[minIdx], ary[i]

    return ary

## 전역 변수 선언 부분
moneyAry = [7, 5, 11, 6, 9, 80000, 10, 6, 15, 12]

## 메인코드 부분
print(f'용돈 정렬 전 -> {moneyAry}')
moneyAry = selectionSort(moneyAry)
print(f'용돈 정렬 후 -> {moneyAry}')
print(f'용돈 중앙값 -> {moneyAry[len(moneyAry)//2]}')