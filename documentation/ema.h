#ifndef EMA_H_
#define EMA_H_

#include <stddef.h>

/**
 * Calcula el error medio absoluto en porcentaje entre una colección de observaciones y de predicciones.
 *
 * @return 0 si las observaciones suman 0. El error medio absoluto en porcentaje en caso contrario.
 */
double ema(double *observaciones, double *predicciones,
		size_t numero_observaciones_y_predicciones);

#endif /* EMA_H_ */
