def analizar_dataframe(df):
    """
    Realiza un análisis básico de cada columna de un DataFrame.
    """
    print(f"ANÁLISIS DEL DATAFRAME ({len(df)} filas, {len(df.columns)} columnas)\n")
    
    for columna in df.columns:
        
        tipo_dato = df[columna].dtype
        nulos = df[columna].isnull().sum()
        porcentaje_nulos = round(df[columna].isnull().mean() * 100, 2)
        unicos = df[columna].unique()
        n_unicos = df[columna].nunique()
        
        # Impresión de resultados
        print(f"Columna: {columna}")
        print(f"  - Tipo de dato: {tipo_dato}")
        print(f"  - Nulos: {nulos} ({porcentaje_nulos}%)")
        print(f"  - Valores únicos: {unicos}")
        print(f"  - Número de valores únicos: {n_unicos}")