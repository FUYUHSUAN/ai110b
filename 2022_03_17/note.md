# 本周雜記
* 講解如何更好的進行旅行推銷員問題
* 以下這是上周我做的作業(運用爬山演算法來作旅行推銷員)
* 老師上課講解，覺得這樣一個一個重複找，會花太多時間
* 因為我寫的這份作業，會一直找到相同的
* 所以老師，讓我們想想如何避免重複搜尋
* 可以試試看隨機的方法
```py
import random

def loss(ans):
    total = 0
    for i in range(num_citys-1):
        total += distance[ans[i]-1][ans[i+1]-1]
    total += distance[ans[num_citys-1]-1][ans[0]-1]
    return total

file = "datasets/five_d.txt"
num_citys = 5
distance = [[0.0 for _ in range(num_citys)] for _ in range(num_citys)] # 距離矩陣

with open(file, 'r') as f: #開檔案，用with的話作完後會消失
    buf = f.readlines()
    for i, line in enumerate(buf):
        for j, text in enumerate(line.rstrip().split()):
            distance[i][j] = float(text)

num_steps = 1000
ans = [i+1 for i in range(num_citys)]
random.shuffle(ans)
diff = 1
for step in range(num_steps):
    l = loss(ans)
    isforward = False
    for i in range(1, num_citys-diff): 
        tempans = ans[:] #代表陣列所有數值
        temploss = 0
        tempans[i:i+diff] = tempans[i+diff-1:i-1:-1]
        temploss = loss(tempans)
        if temploss < l:
            isforward = True
            diff = 1
            l = temploss
            ans = tempans[:]
            break
    if not isforward:
        diff += 1
    if diff > num_citys-1:
        break
    

print(ans, loss(ans))
# for i in range(num_citys):
#     for j in range(num_citys):
#         print(distance[i][j], end="\t")
#     print()
```

---

* 接著老師讓我們練習實作(從以下任選一題實做)
1. 老鼠走迷宮問題
2. 《狼、羊、甘藍菜》過河的問題
3. 八皇后問題

* 我選擇老鼠走迷宮問題來實作
>* 其中程式都是我自己實作的，並參考鍾誠老師所寫的[老鼠走迷宮問題](https://kinmen6.com/root/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E8%AA%B2%E7%A8%8B/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/03-search/Q1-mouse/%E7%BF%92%E9%A1%8C%EF%BC%9A%E4%BB%A5%E6%B7%B1%E5%BA%A6%E5%84%AA%E5%85%88%E6%90%9C%E5%B0%8B%E8%A7%A3%E6%B1%BA%E8%80%81%E9%BC%A0%E8%B5%B0%E8%BF%B7%E5%AE%AE%E5%95%8F%E9%A1%8C.md)來改用python實作

>* 並且將結果寫在[我練習的老鼠寫迷宮程式](HW/2022_03_17)