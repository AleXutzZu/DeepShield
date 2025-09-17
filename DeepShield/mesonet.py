from keras.models import Model
from keras.layers import Input, Conv2D, BatchNormalization, Activation, AveragePooling2D, Flatten, Dense, Dropout

def MesoNet(input_shape=(256, 256, 3)):
    x = Input(shape=input_shape)

    y = Conv2D(8, (3, 3), strides=1, padding='same')(x)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)
    y = AveragePooling2D(pool_size=(2, 2))(y)

    y = Conv2D(8, (5, 5), strides=1, padding='same')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)
    y = AveragePooling2D(pool_size=(2, 2))(y)

    y = Conv2D(16, (5, 5), strides=1, padding='same')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)
    y = AveragePooling2D(pool_size=(2, 2))(y)

    y = Conv2D(16, (5, 5), strides=1, padding='same')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)
    y = AveragePooling2D(pool_size=(4, 4))(y)

    y = Flatten()(y)
    y = Dropout(0.5)(y)
    y = Dense(16)(y)
    y = Activation('relu')(y)
    y = Dropout(0.5)(y)
    y = Dense(1, activation='sigmoid')(y)

    model = Model(inputs=x, outputs=y)
    return model
