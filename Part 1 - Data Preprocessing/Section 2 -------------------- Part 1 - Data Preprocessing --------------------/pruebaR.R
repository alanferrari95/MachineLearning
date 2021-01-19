#Plantilla para el pre procesado de datos
#Importar el dataset
dataset=read.csv("Data.csv")

#Tratamiento de los valores NA
#Ave hace un subconjunto promedio
#Si se encuentra con un NA lo remplaza por la media de todas las edades
dataset$Age=ifelse(is.na(dataset$Age),
                   ave(dataset$Age, FUN=function(x) mean(x, na.rm=TRUE)),
                   dataset$Age)

dataset$Salary=ifelse(is.na(dataset$Salary),
                   ave(dataset$Salary, FUN=function(x) mean(x, na.rm=TRUE)),
                   dataset$Salary)

#Codificar las variables categoricas
#Convierte una columna en factores
dataset$Country=factor(dataset$Country,
                       levels=c("France","Spain","Germany"),
                       labels=c(1,2,3))

dataset$Purchased=factor(dataset$Purchased,
                       levels=c("No","Yes"),
                       labels=c(0,1))

#Dividir los datos en conjunto de entrenamiento y conjunto de test
#instalar paquete catool
#install.packages("caTools")
library(caTools)
#dividir entre entrenamiento y test. Funcion de la libreria caTools
#semilla aleatorea para darle un valor
set.seed(123)
split=sample.split(dataset$Purchased, SplitRatio=0.8)
#Dividimos el dataset
#Dataset de training donde el split sea TRUE
training_set=subset(dataset, split==TRUE)
#Dataset de testing donde el split sea FALSE
testing_set=subset(dataset, split==FALSE)

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

#Escalado de valores.
#No escalo los valores de la columna 1 y 2 porque son de tipo "Factor" y los numeros que 
#aparecen estan entre "comillas", dando una suerte de strings
training_set[,2:3]=scale(training_set[,2:3])
testing_set[,2:3]=scale(testing_set[,2:3])