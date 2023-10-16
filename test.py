import tensorflow as tf

#print(tf.__version__)
#print(tf.test.gpu_device_name())

config = tf.compat.v1.ConfigProto()
print(config.list_physical_devices('GPU'))
 
a = tf.constant(2.)
b = tf.constant(4.)
 
print(a * b)
ccc