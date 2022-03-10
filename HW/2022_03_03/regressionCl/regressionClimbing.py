import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([2, 3, 4, 5, 6], dtype=np.float32)
# x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
# y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

def predict(a, xt):
	return a[0]+a[1]*xt

def MSE(a, x, y):
	total = 0
	for i in range(len(x)):
		total += (y[i]-predict(a,x[i]))**2
	return total

def loss(p):
	return MSE(p, x, y)

# p = [0.0, 0.0]
# plearn = optimize(loss, p, max_loops=3000, dump_period=1)
def optimize():
    p = [0.0, 0.0]
    i = 0

    while i < 3000:
        p1 = [p[0] + 0.01 ,p[1]]
        p2 = [p[0] ,p[1] + 0.01]
        p3 = [p[0] - 0.01 ,p[1]]
        p4 = [p[0] ,p[1] - 0.01]

        tmp = [p1 ,p2, p3, p4]
        precord = p
        less = loss(p)
        for i in range(0, 4):
            if(loss(tmp[i]) < less):
                precord = tmp[i]
                less = loss(tmp[i])
                
        if precord == p:
            break
        p = precord
        i += 1
    return p
           
    # 請修改這個函數，自動找出讓 loss 最小的 p
    #p = [2,1] # 這個值目前是手動填的，請改為自動尋找。(即使改了 x,y 仍然能找到最適合的回歸線)
    #return p

p = optimize()

# Plot the graph
y_predicted = list(map(lambda t: p[0]+p[1]*t, x))
print('y_predicted=', y_predicted)
plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt.legend()
plt.show()