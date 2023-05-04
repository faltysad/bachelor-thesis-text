def reparameterization(self, z_mean, z_log_var):
    batch = tf.shape(z_mean)[0]
    dim = tf.shape(z_mean)[1]
    epsilon = tf.keras.backend.random_normal(shape=(batch, dim))
    z =  z_mean + tf.exp(0.5 * z_log_var) * epsilon
    return z