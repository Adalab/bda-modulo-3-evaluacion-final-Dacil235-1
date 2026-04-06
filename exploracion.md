Resumen de los cambios en los datos
1. Limpieza de nombres

He pasado todos los nombres de las columnas a minúsculas y con guiones bajos (ej. nombre_columna). Es mucho más cómodo para trabajar y evita errores con las mayúsculas.

2. Eliminación de datos que no sirven

Columna Country: La he borrado porque todos los datos eran iguales y no aportaba nada al análisis.

Duplicados: En el archivo de vuelos había 1.864 filas repetidas con valores en cero. Como parecían errores de carga, las he eliminado.

3. Creación de la columna "Status"

Me di cuenta de que los huecos en Cancellation Year significaban que el cliente no había cancelado. He creado una columna nueva llamada status: si el año está vacío es "active" y si tiene año es "inactive".

4. Arreglo de los Salarios

Negativos: Había sueldos negativos, que claramente eran un error al escribir el signo. Los he pasado todos a positivo.

Nulos: Faltaba el 25% de los sueldos, sobre todo en el nivel "College". Para rellenarlos, he usado la media entre el nivel educativo anterior y el siguiente, que es más preciso que usar una media general.

5. Los decimales en los Puntos

Aunque la mayoría son números enteros, hay algunos con decimales (como .25 o .45). He decidido dejarlos como están porque en medidas de distancia es normal tener esa precisión.

