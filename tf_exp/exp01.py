import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

hello = tf.constant('Hello, Tensorflow')
print(hello)

a = tf.constant(10)
b = tf.constant(32)
c = tf.add(a, b)
print(c)

sess = tf.Session()
print(sess.run(hello))
print(sess.run([a,b,c]))
sess.close()

