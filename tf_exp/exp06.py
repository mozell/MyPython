import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 포유류와 조류를 분류(classfication) 하는 모델 구현
# [털, 날개]
x_data = np.array([[0,0], [1,0], [1,1], [0,0], [0,0], [0,1]])

# [1,0,0]:기타, [0,1,0]:포유류, [0,0,1]:조류
y_data = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1],
    [1,0,0],
    [1,0,0],
    [0,0,1],
])

# [0,0] -> [1,0,0] :기타
# [1,0] -> [0,1,0] :포유류
# [1,1] -> [0,0,1] :조류
# [0,0] -> [1,0,0] :기타
# [0,0] -> [1,0,0] :기타
# [0,1] -> [0,0,1] :조류

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_uniform([2,3], -1., 1.))
b = tf.Variable(tf.zeros([3]))

L = tf.add(tf.matmul(X, W), b)
L = tf.nn.relu(L)


model = tf.nn.softmax(L)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(model), axis= 1))

# 학습
optimizer = tf.train.GradientDescentOptimizer(learning_rate= 0.01)
train_op = optimizer.minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(100):
    sess.run(train_op, feed_dict= {X: x_data, Y: y_data})

    if (step+1) % 10 == 0:
        print(step+1, sess.run(cost, feed_dict={X: x_data, Y: y_data}))

#확인
prediction = tf.argmax(model, axis= 1)
target = tf.argmax(Y, axis = 1)
print('예측값: ',sess.run(prediction, feed_dict={X: x_data}))
print('실제값: ',sess.run(target, feed_dict={Y: y_data}))

#정확도
is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도: %.2f'%sess.run(accuracy*100, feed_dict={X: x_data, Y: y_data}))