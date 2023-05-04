vae.compile(optimizer=keras.optimizers.Adam())
vae.fit(x_train, epochs= 200, batch_size= 128)