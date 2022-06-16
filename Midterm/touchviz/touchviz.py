from torchviz import make_dot
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    """policy-value network module"""
    def __init__(self, board_width, board_height):
        super(Net, self).__init__()

        self.board_width = board_width
        self.board_height = board_height
        # common layers
        self.conv1 = nn.Conv2d(4, 32, kernel_size=3, padding=1)   #輸入大小4個棋盤，輸出32棋盤 kernel_size 表示卷積層的長和寬(kernel_size=3就是3*3的卷積核) ，padding 表示往外一圈為0的值
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        # action policy layers
        self.act_conv1 = nn.Conv2d(128, 4, kernel_size=1)
        self.act_fc1 = nn.Linear(4*board_width*board_height,
                                 board_width*board_height)
        # state value layers
        self.val_conv1 = nn.Conv2d(128, 2, kernel_size=1)
        self.val_fc1 = nn.Linear(2*board_width*board_height, 64)
        self.val_fc2 = nn.Linear(64, 1) # Linear 全連接層
        
    def forward(self, state_input):
        # common layers
        x = F.relu(self.conv1(state_input))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        # action policy layers
        x_act = F.relu(self.act_conv1(x)) #relu激發含式，讓輸入能讓機器比較了解
        x_act = x_act.view(-1, 4*self.board_width*self.board_height) #轉換成Linear
        x_act = F.log_softmax(self.act_fc1(x_act)) #softmax 想成機率，log_softmax()，全部input轉成0~1之間並且加總 = 1
        # state value layers
        x_val = F.relu(self.val_conv1(x))
        x_val = x_val.view(-1, 2*self.board_width*self.board_height)
        x_val = F.relu(self.val_fc1(x_val))
        x_val = F.tanh(self.val_fc2(x_val))
        return x_act, x_val # 棋盤的下子機率，另一個式棋盤的分數

MyConvNet = Net(16, 16)
print(MyConvNet)
x = torch.randn(16*16, 4, 1, 1).requires_grad_(True)  # 定义一个网络的输入值
y = MyConvNet(x)    # 获取网络的预测值

MyConvNetVis = make_dot(y, params=dict(list(MyConvNet.named_parameters()) + [('x', x)]))
MyConvNetVis.format = "png"
# 指定文件生成的文件夹
MyConvNetVis.directory = "data"
# 生成文件
MyConvNetVis.view()