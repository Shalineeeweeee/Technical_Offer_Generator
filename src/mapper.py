def map_columns(dataframe, mapping):

    dataframe = dataframe.rename(columns=mapping)

    return dataframe