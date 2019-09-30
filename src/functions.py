import numpy as np
import pandas as pd
import math
import warnings
warnings.filterwarnings('ignore')


def data_loading(path):
    data = pd.read_fwf(path, parse_dates=['observaciones'])
    split = data.loc[data['observaciones'] == 'predicciones'].index.values.astype(int)[0]
    df_observation = data[:split]
    df_prediction = data[split+1:]

    df_observation[['production','wind_mod']] = df_observation['Unnamed: 1'].str.split(" ",expand=True)
    df_observation = df_observation[[x for x in df_observation.columns if x != 'Unnamed: 1']]
    df_predict = df_prediction.rename(columns={'Unnamed: 1': 'wind_mod'})

    df_observation['observaciones'] = pd.to_datetime(df_observation['observaciones'], errors='coerce', format='%Y-%m-%d %H:%M')
    df_predict['observaciones'] = pd.to_datetime(df_predict['observaciones'], errors='coerce', format='%Y-%m-%d %H:%M')

    df_observation['wind_mod'] = df_observation.wind_mod.astype(int)
    df_observation['production'] = df_observation.production.astype(int)
    df_predict['wind_mod'] = df_predict.wind_mod.astype(int)

    return df_observation, df_predict


def _error(actual: np.ndarray, predicted: np.ndarray):
    """ Simple error """
    return actual - predicted

def mse(actual: np.ndarray, predicted: np.ndarray):
    """ Mean Squared Error """
    return np.mean(np.square(_error(actual, predicted)))

def rmse(actual: np.ndarray, predicted: np.ndarray):
    """ Root Mean Squared Error """
    return np.sqrt(mse(actual, predicted))

def mae(actual: np.ndarray, predicted: np.ndarray):
    """ Mean Absolute Error """
    return np.mean(np.abs(_error(actual, predicted)))


def to_train(wind_mod, wind_mod_pred, L, k, x0):
    result = []
    params = []
    mse_err = []
    mae_err = []
    rmse_err = []
    for x in wind_mod:
        for i in k:
            for s in x0:

                try:
                    func = L/(1-math.exp(-(i)*((x)-(s))))
                    params_ = [i, s]

                    if func > 0: # He puesto esta condición porque previamente me salían valores negativos
                        result.append(func)
                        params.append(params_)

                        # Defino dos arrays para cálculo de errores
                        actual_array = np.asarray(func, dtype=np.float32)
                        predicted_array = np.asarray(wind_mod_pred, dtype=np.float32)

                        mse_err.append(mse(actual_array, predicted_array))
                        mae_err.append(mae(actual_array, predicted_array))
                        rmse_err.append(rmse(actual_array, predicted_array))

                except ZeroDivisionError:
                    continue
    return params, mse_err, mae_err, rmse_err

def to_fit(wind_mod_pred, L, params, mse_err, mae_err, rmse_err):
    print(rmse_err)
    print(params)
    print(int(np.argmin(rmse_err)))
    print(params[int(np.argmin(rmse_err))])
    print(params[0])

    print(params[int(np.argmin(rmse_err))][0])
    rmse_best_k = params[int(np.argmin(rmse_err))][0]
    rmse_best_x0 = params[(int(np.argmin(rmse_err)))][1]

    mse_best_k = params[(int(np.argmin(mse_err)))][0]
    mse_best_x0 = params[(int(np.argmin(mse_err)))][1]

    mae_best_k = params[(int(np.argmin(mae_err)))][0]
    mae_best_x0 = params[(int(np.argmin(mae_err)))][1]

    rmse_output = (int(np.amin(rmse_err)))/100
    mse_output = (int(np.amin(mse_err)))/100
    mae_output = (int(np.amin(mae_err)))/100
    
    wind_mod_pred_rmse = []
    wind_mod_pred_mse = []
    wind_mod_pred_mae = []


    for x in wind_mod_pred:
        funcion_params_rmse = L/(1-math.exp(-(rmse_best_k)*((x)-rmse_best_x0)))
        funcion_params_mse = L/(1-math.exp(-(mse_best_k)*((x)-mse_best_x0)))
        funcion_params_mae = L/(1-math.exp(-(mae_best_k)*((x)-mae_best_x0)))

        wind_mod_pred_rmse.append(funcion_params_rmse)
        wind_mod_pred_mse.append(funcion_params_mse)
        wind_mod_pred_mae.append(funcion_params_mae)    

    print(L , rmse_best_k, rmse_best_x0)
    print(mae_output, rmse_output)
    return wind_mod_pred_rmse

