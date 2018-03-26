from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.preprocessing import image

import numpy as np
import os
import time
import sys

import readlev

X = []
Y = []

#os.path.join('levels',sys.argv[1])
for lev in ['Tutor01.lev']:
    # reclink, int1, int2, int3, int4, levname, lgr, ground, sky, polys, objs
    reclink, int1, int2, int3, int4, levname, lgr, ground, sky, polys, objs = readlev.read(lev)
    Y.append( [polys, objs] )
    img_path = lev.replace('.lev', '.png')
    x = image.load_img(img_path, target_size=(100, 100))
    X.append( x )

#Y = np.array(Y)
#X = np.array(X)
print(X)
print(Y)

# samples should be same amount as y values; this is the dimensionality LSTM expects: https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/
#x = x.reshape((len(y), 1, 1)) # (samples, time_steps, features) #
#print(len(x), len(y))
#print(x, x.shape)

"""model = Sequential()
model.add(LSTM(
    1,
    input_shape=(1, 1), # (time_steps, features)
    #output_dim=1,
    #return_sequences=True
))
#model.add( Dense(1) )
model.add(Activation('softmax'))

start = time.time()
optimizer = RMSprop(lr=0.1)
model.compile(loss='msle', optimizer=optimizer) # loss='mse', optimizer='rmsprop'
#model.compile(loss='binary_crossentropy', optimizer='adam')
print('compilation time : ', time.time() - start)

model.fit(
    x,
    y,
    batch_size=5,
    epochs=2,
    validation_split=0.1)

# evaluate the model
#scores = model.evaluate(x, y)
#print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

#print( model.summary() )

values_to_predict = [400]
values_to_predict = np.array(values_to_predict)
values_to_predict = values_to_predict.reshape((len(values_to_predict), 1, 1)) # (samples, time_steps, features)
p = model.predict(values_to_predict)

import datetime
#unixtime = (p + 1) * y[0] # add one and multiply by first row to denormalize the y value
dt = datetime.datetime.fromtimestamp(p).strftime('%Y-%m-%d %H:%M:%S')
print(p, p*y[0], dt)"""

#import plot
#plot.plot(x, [i/3800000 for i in y], "WR Table #", "Elma Underground Time Units", fig="wr_tables.png", spline=True)
#sys.exit()


"""
model.add(Dropout(0.2))


model.add(LSTM(
    input_dim=1,
    output_dim=50,
    return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(
    100,
    return_sequences=False))
model.add(Dropout(0.2))

model.add(Dense(
    output_dim=1))
model.add(Activation('linear'))

start = time.time()
model.compile(loss='mse', optimizer='rmsprop')
print('compilation time : ', time.time() - start)

model.fit(
    X_train,
    y_train,
    batch_size=512,
    nb_epoch=1,
    validation_split=0.05)
    
predictions = lstm.predict_sequences_multiple(model, X_test, 50, 50)
#lstm.plot_results_multiple(predictions, y_test, 50)
"""
