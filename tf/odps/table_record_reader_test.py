import tensorflow as tf
import time

tf.app.flags.DEFINE_string("tables", "", "tables info")

FLAGS = tf.app.flags.FLAGS

print("tables:", FLAGS.tables)

tables = [FLAGS.tables]

filename_queue = tf.train.string_input_producer(tables, num_epochs=1)

print(filename_queue)

reader = tf.TableRecordReader()
key,value=reader.read(filename_queue)
record_defaults = [[1.0], [1.0], [1.0], [1.0], ["Iris-virginica"]]
col1, col2, col3, col4, col5 = tf.decode_csv(value, record_defaults = record_defaults)
features = tf.pack([col1, col2, col3, col4])
init = tf.initialize_all_variables()

with tf.Session() as sess:
    with tf.device("/cpu:0"):
        sess.run(init)
        sess.run(tf.initialize_local_variables())
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        try:
            step = 0
            while not coord.should_stop():
                step += 1
                example, label = sess.run([features, col5])
                print("line:", step, example, label)
        except tf.errors.OutOfRangeError:
            print(' training for 1 epochs, %d steps', step)
        finally:
            coord.request_stop()
            coord.join(threads)
