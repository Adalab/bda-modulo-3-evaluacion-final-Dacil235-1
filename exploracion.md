Fase 1:

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

Fase 2:

Explorando las variables numéricas y los outliers:

1. Salario. La mayoria de los clientes ganan entre 50.000 y 100.000 al año, aunque observo muchos outliers en los que el cliente ganas mas de 100.000 al año, es un grupo pequeño pero no tanto como los que ganan menos de 50.000 al año.

2. CLV. En este boxplot se observa que la mitad de los clientes no aportan mucho valor a la empresa pero que un gran númro de outliers si lo hacen.

3. Flights Booked. Aquí vemos que la mayoría de los clientes reservan entre 0 y 8 vuelos, y que hay clientes que vuelan hasta 20 veces pero son menos frecuentes, hay un outliers que vuela mas de 20 veces.

4. flights_with_companions. Esta gráfica nos muestra que la mayoria de los clientes viajan solos, veo unos pocos outliers en los que viajes a compañados.

5. total_flights. Gráfica muy parecida a la de vuelos reservados, clientes que viajan entre 0 y 10 veces, aunque la mediada tira más hacia el 0 y outliers que viajan mas de 10 veces.

6. points_accumulated. Muy relacionado con el total de vuelos, la mayor parte de los clientes no acumulan muchos puntos porque viajan poco y los ouyliers tienen mas puntos debido a la frecuencia con la que viajan.

7. points_redeemed. La mayoría de los clientes no han canjeado sus puntos, solo unos pocos (outliers) si los canjean, supongo que es debido a que como viajan con mas frecuencia tienen suficientes puntos para canjear.

8. dollar_cost_points_redeemed. Misma interpretación que con la variable points_redeemed.


Análisis de correlación entre variables numéricas:

He echo un heatmap para identificar las variables que tiene mas correlación, vemos que hay una correlación positiva entre los vuelos reservados, el total de vuelos, la distancia y los puntos acumulados por el cliente.

Análisis variables categóricas:

1. province. Tu mercado principal es Ontario, seguido de lejos por British Columbia y Quebec. Si vas a lanzar una campaña, Ontario es donde está el volumen.

2. education. La gran mayoría tiene un nivel de Bachelor (Grado). Esto encaja con los sueldos que vimos: gente de clase media-alta.

3. marital_status y enrollment_type. Tienes una base de clientes mayoritariamente casada y que se inscribe de forma estándar (no por promociones puntuales). Esto indica que son clientes orgánicos y estables.

4. gender. Está perfectamente equilibrado. Tu producto interesa por igual a hombres y mujeres.

5. loyalty_card. La tarjeta Star es la más común, pero tienes un grupo sólido de Nova. La tarjeta Aurora es la más exclusiva (menos gente), lo cual tiene sentido.

