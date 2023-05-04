vae = VAE(
    input_dim = (28, 28, 1),
    z_dim = 2,
    encoder_conv_filters = [32, 64, 64, 64],
    encoder_conv_kernel_size = [3, 3, 3, 3],
    encoder_conv_strides = [1, 2, 2, 1],
    decoder_conv_t_filters = [64, 64, 32, 1],
    decoder_conv_t_kernel_size = [3, 3, 3, 3],
    decoder_conv_t_strides = [1, 2, 2, 1]
)