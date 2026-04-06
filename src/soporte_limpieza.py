def limpiar_columnas(df):
    """
    Transforma los nombres de las columnas a minúsculas 
    y reemplaza espacios por guiones bajos.
    """
    df.columns = (df.columns.str.strip().str.lower().str.replace(' ', '_'))
    return df
