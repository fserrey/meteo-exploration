import numpy as np
import pandas as pd
import math
from src.functions import *
import warnings
warnings.filterwarnings('ignore')


path = '20190910.txt'

# Cargo elarchivo de datos y lo transformo en dos dataframe para trabajar
df_observation, df_predict = data_loading(path)

# Una vez definidos los errores, paso a definir las variables que usaremos inicialmente
wind_mod = list(map(int, list(df_observation['wind_mod'])))
production = list(map(int, list(df_observation['production'])))
wind_mod_pred = list(map(int, list(df_predict['wind_mod'])))

L = float(max(wind_mod))
k = (np.arange(0.5,1.5,0.05)).tolist()
x0 = (np.linspace(start=0, stop=L, num=20)).tolist()    

# Preparo la función 'train' para que recorra las variables y ejecute los cálculos previstos en esta prueba

#Esta función me devuelve los parámetros y los errores MSE, MAE y RMSE
parameters, mse_err, mae_err, rmse_err = to_train(wind_mod, L, k, x0)  
params = parameters

# En esta otra función, preparamos el fit. Imprimimos ya varios de los valores que necesitamos en el output
wind_module = to_fit(wind_mod_pred, params, mse_err, mae_err, rmse_err)

# Aquí preparo el output
df_predict["production"] = [ '%.2f' % elem for elem in wind_module ]
print(df_predict[["observaciones","production"]].to_string(index=False))