import tensorflow as tf


def read_image(file_queue):
    reader = tf.TFRecordReader()
    key, value = reader.read(file_queue)
    _, serialized_example = reader.read(file_queue)
    features = tf.parse_single_example(
        serialized_example,
        features={
            'image_raw': tf.FixedLenFeature([], tf.string),
            'label': tf.FixedLenFeature([], tf.int64),
        })

    image = tf.decode_raw(features['image_raw'], tf.uint8)
    image.set_shape([784])
    image = tf.cast(image, tf.float32) * (1. / 255) - 0.5
    label = tf.cast(features['label'], tf.int32)
    return image, label


def read_image_batch(file_queue, batch_size):
    img, label = read_image(file_queue)
    capacity = 3 * batch_size
    image_batch, label_batch = tf.train.batch([img, label], batch_size=batch_size, capacity=capacity, num_threads=10)
    one_hot_labels = tf.to_float(tf.one_hot(label_batch, 10, 1, 0))
    return image_batch, one_hot_labels


if __name__ == '__main__':
    tf.app.flags.DEFINE_string("volumes", "", "volumes info")
    FLAGS = tf.app.flags.FLAGS

    volumes = FLAGS.volumes.split(",");

    train_file_path = volumes[0] + "/*.tfrecords"
    test_file_path = volumes[1] + "/*.tfrecords"

    train_image_filename_queue = tf.train.string_input_producer(tf.train.match_filenames_once(train_file_path))
    train_images, train_labels = read_image_batch(train_image_filename_queue, 100)

    test_image_filename_queue = tf.train.string_input_producer(tf.train.match_filenames_once(test_file_path))
    test_images, test_labels = read_image_batch(test_image_filename_queue, 100)

    x = tf.reshape(train_images, [-1, 784])
    w = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x, w) + b)
    y_ = tf.to_float(train_labels)
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    x_test = tf.reshape(test_images, [-1, 784])
    y_pred = tf.nn.softmax(tf.matmul(x_test, w) + b)
    y_test = tf.to_float(test_labels)

    correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y_test, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    init = tf.initialize_all_variables()

    with tf.Session() as sess:
        sess.run(init)

        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)
        for i in range(1000):
            sess.run(train_step)
            if ((i + 1) % 20 == 0):
                print("step:", i + 1, "accuracy:", sess.run(accuracy))
        print(sess.run(accuracy))
        coord.request_stop()
        coord.join(threads)
