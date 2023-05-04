self.encoder = tf.keras.Sequential([
    InputLayer(input_shape=(img_height, img_width, img_channel)),
    Conv2D(32, 3, activation="relu", strides=2,
           padding="same", name='encoder_conv_1'),
    Conv2D(64, 3, activation="relu", strides=2,
           padding="same", name='encoder_conv_2'),
    Flatten(),
    Dense(16, activation="relu"),
    Dense(latent_dim),
])
