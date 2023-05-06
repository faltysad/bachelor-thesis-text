vae.compile(optimizer = tf.keras.optimizers.Adam())
vae.fit(x_train, epochs = 500, batch_size = 128)