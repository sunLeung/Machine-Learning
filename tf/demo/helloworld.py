import tensorflow as tf


def helloworld():
    hello = tf.constant('hello tensorflow')

    with tf.Session() as session:
        result = session.run(hello)
        print(result)


def demo01():
    a = tf.constant(2)
    b = tf.constant(3)
    with tf.Session() as session:
        print(session.run(a + b))
        print(session.run(a * b))


def demo02():
    a = tf.placeholder(tf.float32)
    b = tf.placeholder(tf.float32)
    add = tf.add(a, b)
    mul = tf.multiply(a, b)
    with tf.Session() as session:
        print(session.run(add, feed_dict={a: 2, b: 3}))
        print(session.run(mul, feed_dict={a: 2, b: 3}))


def demo03():
    matrix1 = tf.constant([[3., 3.]])
    matrix2 = tf.constant([[2.]
                              , [2.]])
    product = tf.matmul(matrix1, matrix2)
    with tf.Session() as sess:
        print(sess.run(product))


if __name__ == '__main__':
    demo03()
