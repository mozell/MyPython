import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 선형 회귀 모델구현

x_data = [1, 2, 3]
y_data = [1, 2, 3]

# x와 y의 상관관계를 설명하기 위한 변수들인 W, b 를 각각 -1.0~1.0 사이의 균등분포를 가진 무작위 값으로 초기화
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

# 자료를 입력받을 플레이스 홀더 설정
X = tf.placeholder(tf.float32, name= "X")
Y = tf.placeholder(tf.float32, name= "Y")

# 상관관계를 분석하기 위한 수식 작성(W: 가중치, b: 편향)
hypothesis = W * X + b

# 손실함수 작성
# (x, y)한 쌍의 데이터에 대한 손실값을 계산하는 함수
# 손실값: 실제 값과 예측한 값이 얼마나 차이 나는지?, 손실값이 작을수록 X, Y관계를 잘 파악한 모델

# 비용 : 손실을 전체 데이터에 대해 구한 경우
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# 경사하강법 최적화 함수를 이용해 손실값을 최소화하는 연산 그래프 생성
optimizer = tf.train.GradientDescentOptimizer(learning_rate= 0.1)
train_op = optimizer.minimize(cost)

# 결과 확인
with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())

    for step in range(100):
        _, cost_val = sess.run([train_op, cost], feed_dict= {X: x_data,
                                                             Y: y_data})
        print(step, cost_val, sess.run(W), sess.run(b))

    print("X:   5, Y: ", sess.run(hypothesis, feed_dict={X: 5}))
    print("X: 2.5, Y: ", sess.run(hypothesis, feed_dict={X: 2.5}))
    # 5와 2.5를 정확하게 예측!!!