## Meteo data exploration
On this repository I aimed to explore and develop a basic electric power predictor for a wind farm power plant based on
meteorological data. The data given only provide production and wind module measures.

### What's the goal?
Main task aims to develop a basic predictor system that use wind module - production generated relation. From this point,
we expect to automatize the prediction process and discover the insigth for each wind farm installation (as the
prediction and the system used may vary from one power plant to other).

**Methodology**
Let's develop this logistic function:
`function = L / 1 - (e - k(x-x0 ))`
This function has a number of parameters: L, k and x 0 that we will adjust to each park. To do this
we will perform an optimization procedure to minimize the error we make in the prediction of the park.
In order to optimize these parameters, we are going to use a very simple procedure which will consist of testing a sufficient number of values for the parameters of the function.
- **L** this parameter will correspond to the installed power of the park, since we do not have the installed power data, we will use the maximum value of the production data.  **k** and **x0** for these two parameters we will divide the search space as follows:
    - **x0** will be between 0 and the maximum value of the wind module present in the data and divide this interval into 20 pieces.
    - **k** use the interval [ 12 , 2 3 ] and test each separate value 0,05.

Knowing the intervals at which we are going to test values for our parameters, the process of optimization consists in calculating the mean quadratic error (RMSE) for each of the combinations of the parameters **k** and **x0** (**L** is calculated at the beginning and is already fixed). And we will keep the combination of parameters with the smallest mean quadratic error.

### Folders
- **src** - Where the main code and functions are stored
- **notebooks** Where a jupyter notebook was used for the first exploratory exercise
