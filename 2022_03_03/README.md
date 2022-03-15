爬山演算法:往距離現在這個點相對較高的點去走，往往使用高度來使用
梯度下降法:往往使用能能量，錯誤率來表示
練習老師所
```
# 簡易爬山演算法 -- 針對單變數函數
def hillClimbing(f, x, dx=0.01):
    while (True):
        print('x={0:.5f} f(x)={1:.5f}'.format(x, f(x)))
        if f(x+dx)>f(x): # 如果右邊的高度 f(x+dx) > 目前高度 f(x) ，那麼就往右走
            x = x + dx
        elif f(x-dx)>f(x): # 如果左邊的高度 f(x-dx) > 目前高度 f(x) ，那麼就往左走
            x = x - dx
        else: # 如果兩邊都沒有比現在的 f(x) 高，那麼這裡就是區域最高點，直接中斷傳回
            break
    return x

# 高度函數
def f(x):
    return -1*(x*x-2*x+1)
    # return -1*(x*x+3*x+5)
    # return -1*abs(x*x-4)

hillClimbing(f, 0) # 以 x=0 為起點，開始呼叫爬山演算法

```
執行結果
```
s1108@DESKTOP-IJI9NA5 MINGW64 /d/Vscode/AI110/ai/02-optimize/01-hillclimbing/02-var1 (master)
$ python hillClimbing1.py 
x=0.00000 f(x)=-1.00000
x=0.01000 f(x)=-0.98010
x=0.02000 f(x)=-0.96040
x=0.03000 f(x)=-0.94090
x=0.04000 f(x)=-0.92160
x=0.05000 f(x)=-0.90250
x=0.06000 f(x)=-0.88360
x=0.07000 f(x)=-0.86490
x=0.08000 f(x)=-0.84640
x=0.09000 f(x)=-0.82810
x=0.10000 f(x)=-0.81000
x=0.11000 f(x)=-0.79210
x=0.12000 f(x)=-0.77440
x=0.13000 f(x)=-0.75690
x=0.14000 f(x)=-0.73960
x=0.15000 f(x)=-0.72250
x=0.16000 f(x)=-0.70560
x=0.17000 f(x)=-0.68890
x=0.18000 f(x)=-0.67240
x=0.19000 f(x)=-0.65610
x=0.20000 f(x)=-0.64000
x=0.21000 f(x)=-0.62410
x=0.22000 f(x)=-0.60840
x=0.23000 f(x)=-0.59290
x=0.24000 f(x)=-0.57760
x=0.25000 f(x)=-0.56250
x=0.26000 f(x)=-0.54760
x=0.27000 f(x)=-0.53290
x=0.28000 f(x)=-0.51840
x=0.29000 f(x)=-0.50410
x=0.30000 f(x)=-0.49000
x=0.31000 f(x)=-0.47610
x=0.32000 f(x)=-0.46240
x=0.33000 f(x)=-0.44890
x=0.34000 f(x)=-0.43560
x=0.35000 f(x)=-0.42250
x=0.36000 f(x)=-0.40960
x=0.37000 f(x)=-0.39690
x=0.38000 f(x)=-0.38440
x=0.39000 f(x)=-0.37210
x=0.40000 f(x)=-0.36000
x=0.41000 f(x)=-0.34810
x=0.42000 f(x)=-0.33640
x=0.43000 f(x)=-0.32490
x=0.44000 f(x)=-0.31360
x=0.45000 f(x)=-0.30250
x=0.46000 f(x)=-0.29160
x=0.47000 f(x)=-0.28090
x=0.48000 f(x)=-0.27040
x=0.49000 f(x)=-0.26010
x=0.50000 f(x)=-0.25000
x=0.51000 f(x)=-0.24010
x=0.52000 f(x)=-0.23040
x=0.53000 f(x)=-0.22090
x=0.54000 f(x)=-0.21160
x=0.55000 f(x)=-0.20250
x=0.56000 f(x)=-0.19360
x=0.57000 f(x)=-0.18490
x=0.58000 f(x)=-0.17640
x=0.59000 f(x)=-0.16810
x=0.60000 f(x)=-0.16000
x=0.61000 f(x)=-0.15210
x=0.62000 f(x)=-0.14440
x=0.63000 f(x)=-0.13690
x=0.64000 f(x)=-0.12960
x=0.65000 f(x)=-0.12250
x=0.66000 f(x)=-0.11560
x=0.67000 f(x)=-0.10890
x=0.68000 f(x)=-0.10240
x=0.69000 f(x)=-0.09610
x=0.70000 f(x)=-0.09000
x=0.71000 f(x)=-0.08410
x=0.72000 f(x)=-0.07840
x=0.73000 f(x)=-0.07290
x=0.74000 f(x)=-0.06760
x=0.75000 f(x)=-0.06250
x=0.76000 f(x)=-0.05760
x=0.77000 f(x)=-0.05290
x=0.78000 f(x)=-0.04840
x=0.79000 f(x)=-0.04410
x=0.80000 f(x)=-0.04000
x=0.81000 f(x)=-0.03610
x=0.82000 f(x)=-0.03240
x=0.83000 f(x)=-0.02890
x=0.84000 f(x)=-0.02560
x=0.85000 f(x)=-0.02250
x=0.86000 f(x)=-0.01960
x=0.87000 f(x)=-0.01690
x=0.88000 f(x)=-0.01440
x=0.89000 f(x)=-0.01210
x=0.90000 f(x)=-0.01000
x=0.91000 f(x)=-0.00810
x=0.92000 f(x)=-0.00640
x=0.93000 f(x)=-0.00490
x=0.94000 f(x)=-0.00360
x=0.95000 f(x)=-0.00250
x=0.96000 f(x)=-0.00160
x=0.97000 f(x)=-0.00090
x=0.98000 f(x)=-0.00040
x=0.99000 f(x)=-0.00010
x=1.00000 f(x)=-0.00000
```