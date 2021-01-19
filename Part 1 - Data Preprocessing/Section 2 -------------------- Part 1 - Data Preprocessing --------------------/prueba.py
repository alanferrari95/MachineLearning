# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 03:54:49 2020

@author: Alan
"""

#planilla de pre procesado
#como importar las librerias
#numpy: tiene herramientas matematicas
import numpy as np
#representacion grafica
import matplotlib.pyplot as plt
import pandas as pd


#importar el data set
dataset=pd.read_csv("Data.csv")
#variable X. Localizo a la X para todas las filas y todas las columnas salvo la ultima
X=dataset.iloc[:,:-1].values
#aca elegis todas las filas y solo la tercer columna
y=dataset.iloc[:,3].values

#Tratamineto de NaN
from sklearn.impute import SimpleImputer
#reemplazamos los NaN por la meadia = "mean" de la columna. 
#Columna(axis=0) y fila(axis=1)
imputer=SimpleImputer(missing_values=np.nan, strategy="mean", verbose=0)
#Arreglamos los nan.
imputer=imputer.fit(X[:,1:3])
#"transform" sustituye los valores
X[:,1:3]=imputer.transform(X[:,1:3])

#Codificar datos categoricos
#Transformar datos "categoricos" (los paises) a numeros
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#crear un codificador de datos
labelencoder_X=LabelEncoder()
#Agarra una variable y la transforma. En este caso transforma la columna 0 (paises)
X[:,0]=labelencoder_X.fit_transform(X[:,0])
#Codificacion de variables categoricas
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()

labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)

#Dividir el data set en conjunto de entrenamiento y conjunto de testing
#Libreria que ayuda a separar entre entrenamiento y conjunto
from sklearn.model_selection import train_test_split
#Creamos las variables de entrenamiento y de test tanto para X como para y
#Test_size = porcentaje que se va a utilizar como "test", en este caso 20%
#random_state es para que devuelva siempre el mismo valor
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=0)
#"over setting" es cuando un modelo de entrenamiento se aprende de memoria los reusltados
#por ende a la hora de testear, es mas probable que falle

#Problemas que se pueden presentar: distancia euclidean (distancia entre 2 puntos x,y)
#Distancia entre p1 y p2= raiz cuadrada de ((x2-x1)^2+(y2-y1)^2).
#Como la edad varia entre 27 y 50 y el salario entre 48000 y 83000, la variable X pasaria
#a ser casi inadvertida. Para eso se "escalan" los datos, por ejemplo datos entre 1 y -1.
#Esto es para evitar que unas variables pesen mas que lo otro
#Tenemos que diferenciar entre Estandarizacion y Normalizacion
#Estandarizacion: A un numero X le resto la media de toda la columna X y lo divido 
#por la desviacion estandar
#Ventajas: cuando hay numeros muy cercanos

#Normalizacion: Al numero X le resto el numero minimo de X y lo divido por la diferencia
#entre la X maxima y la X minima. El numero mas grande es 1 y el mas chico es 0.

#Escalado de variables
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
#Escala X_test con los mismos datos (o forma) que el X_train
X_test=sc_X.transform(X_test)


















