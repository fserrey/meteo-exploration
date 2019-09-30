#include "ema.h"

#include <math.h>

double ema(double *observaciones, double *predicciones,
		size_t numero_observaciones_y_predicciones) {
	double error_acumulado = 0.;
	double observacion_total = 0.;

	double *observaciones_fin = observaciones
			+ numero_observaciones_y_predicciones;
	for (; observaciones != observaciones_fin;
			++observaciones, ++predicciones) {
		error_acumulado += fabs(*observaciones - *predicciones);
		observacion_total += *observaciones;
	}

	if (observacion_total < 1e-7) {
		return 0.;
	}

	return (error_acumulado / observacion_total) * 100.;
}

