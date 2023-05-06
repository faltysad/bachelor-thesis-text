def train_step(self, data):
  with tf.GradientTape() as tape:
    z_mean, z_log_var = self.encode(data)
    z = self.reparameterization(z_mean, z_log_var)
    reconstruction = self.decode(z)

    reconstruction_loss = tf.reduce_mean(
      tf.reduce_sum(keras.losses.binary_crossentropy(data, reconstruction), axis=(1, 2))
    )
    kl_loss = -0.5 * (1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var))
    total_loss = reconstruction_loss + kl_loss

    grads = tape.gradient(total_loss, self.trainable_weights)
    self.optimizer.apply_gradients(zip(grads, self.trainable_weights))

    self.total_loss_tracker.update_state(total_loss)
    self.reconstruction_loss_tracker.update_state(reconstruction_loss)
    self.kl_loss_tracker.update_state(kl_loss)

    return {
      "total_loss": self.total_loss_tracker.result(),
      "reconstruction_loss": self.reconstruction_loss_tracker.result(),
      "kl_loss": self.kl_loss_tracker.result(),
    }