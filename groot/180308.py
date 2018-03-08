import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


#1
hello = tf.constant("hello world")

sess = tf.Session()

print(sess.run(hello))

sess.close()
print("#1 end"); print()

#2
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print("node1: ",node1)
print("node2: ",node2)
print("node3: ",node3)

sess = tf.Session()
print("sess.run([node1, node2]) :", sess.run([node1, node2]))
print("sess.run(node3) :", sess.run(node3))

sess.close()
print("#2 end"); print()

#3
node1 = tf.placeholder(tf.float32)
node2 = tf.placeholder(tf.float32)
adder_node = node1 + node2

print("node1: ",node1)
print("node2: ",node2)
print("adder_node: ",adder_node)

sess = tf.Session()
print(sess.run(adder_node, feed_dict = {node1: 1, node2: 3.5}))
print(sess.run(adder_node, feed_dict = {node1: [2, 3.5], node2: [1, 4]}))

sess.close()
print("#3 end"); print()

# Rank : 차원수, Shape : Tensor의 모양


#4
x_train = [1, 2, 3]
y_train = [1, 2, 3]

W = tf.Variable(tf.random_normal([1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis = W * x_train - b

cost = tf.reduce_mean(tf.square(hypothesis - y_train))

optimizer = tf.train.GradientDescentOptimizer(learning_rate= 0.01)
train = optimizer.minimize(cost)

sess = tf.Session()

# w, b가 지역변수가되면 세션이실행되고 w, b가 초기화됨
# w, b를 전역변수로 사용하기 위해 다음코드작성
sess.run(tf.global_variables_initializer())

for steps in range(2001):
    sess.run(train)
    if steps % 50 == 0 :
        print(steps, sess.run(cost), sess.run(W), sess.run(b))

sess.close()
print("#4 end"); print()

# https://ghebook.blogspot.kr/2011/06/tensor.html