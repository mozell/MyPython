import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 플레이스 홀더 : 그래프에 입력값을 나중에 받기 위해 사용하는 매개변수
#         변수 : 그래프를 최적화하는 용도, 학습한 결과를 갱신하기 위해 사용하는 변수

X = tf.placeholder(tf.float32, [None, 3])
print(X)

x_data = [[1, 2, 3], [4, 5, 6]]
W = tf.Variable(tf.random_normal([3, 2])) # (3,2) 행렬형태의 텐서
b = tf.Variable(tf.random_normal([2, 1])) # (2,1) 행렬형태의 텐서

expr = tf.matmul(X, W) + b               # 행렬곱

sess = tf.Session()
sess.run(tf.global_variables_initializer())     # 아ㅠ에서 정의한 변수들을 초기화하는 함수

print(" === x_data === ")
print(x_data)
print(" =====  W ===== ")
print(sess.run(W))
print(" =====  b ===== ")
print(sess.run(b))
print(" ==== expr ==== ")
print(sess.run(expr, feed_dict= {X: x_data}))

sess.close()