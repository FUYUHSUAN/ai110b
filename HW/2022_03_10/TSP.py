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