from src.functions import *
import warnings
warnings.filterwarnings('ignore')

path = '20190910.txt'

# Given a directory path with data, we load our function to create two dataframes so we can work easily
df_observation, df_predict = data_loading(path)

# As we have described in README, we set the variables we are going to use in or ad hoc function.
wind_mod = list(map(int, list(df_observation['wind_mod'])))
production = list(map(int, list(df_observation['production'])))
wind_mod_pred = list(map(int, list(df_predict['wind_mod'])))

L = float(max(wind_mod))
k = (np.arange(0.5,1.5,0.05)).tolist()
x0 = (np.linspace(start=0, stop=L, num=20)).tolist()    

# Now, with 'train' function, we iterate over variables in order to do not miss any and make the calculus we set.
# This function output are: parameters obtained and errors (MSE, MAE y RMSE)
params, mse_err, mae_err, rmse_err = to_train(wind_mod, wind_mod_pred, L, k, x0)

# With fit function, we finalize prediction process and print the output as demanded in README
wind_module = to_fit(wind_mod_pred, L, params, mse_err, mae_err, rmse_err)
df_predict["production"] = [ '%.2f' % elem for elem in wind_module ]
print(df_predict[["observaciones","production"]].to_string(index=False))
