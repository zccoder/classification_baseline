# classification_baseline
pytorch，transfer learning based on inception_v4

# version
## CUDA 8.0, cudnn6, pytorch 1.4.0

## some tips
### 模型及结果文件分别创建，并分别输出
### 模型应有另外的python文件
### 模型结果应同时保存checkpoint，最低loss， 最高acc等多种情况
### 应该有log文件，log中保存每一轮输出的acc及val acc的值，最后打印最佳的结果

## some tricks
### 少用keras，即使搭建速度快，同样的逻辑，keras没有高分，而且速度相对慢
### 调参时不用冻结高层，以较小的lr全部调
### 考虑的点
#### 数据：数据质量及大小。如果数据量小，那么train_test_split取最佳的结构把所有的数据当作train进行训练
#### 模型：选用同时具有宽度及深度学习能力的incep系列
#### 调参：调优函数及lr并没有太大决定因素，主要在于训练步骤
