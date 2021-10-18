from sqlalchemy import types
import math
import numpy as np

def sqlcol(dfparam, fraction_size=1, varchar_multiplier=1):
    ''' Determines the sentence to create a table with using T-SQL syntax
        Verifies the name of the columns, column type and max longitud or precision.
        Parameters:
        ---------------
            dfparam = dataframe
            fraction_size = random sample size to analyze column type and longitud / precision
            varchar_multiplier = multiplier to augment proportionally the max longitud on each varchar column.
        Required modules:
        ---------------
            sqlalchemy.types
            numpy
            math
    '''

    dtypedict = {}

    for i in range(0, dfparam.shape[1]-1):
        col = dfparam.iloc[:, i].dropna()

        try:

            if col.empty:
                dtypedict.update({
                    col.name: types.VARCHAR(length=100)
                })
            elif str(col.dtype) == 'object':
                dtypedict.update({
                    col.name: types.VARCHAR(length=math.ceil(
                        col.astype(str).map(len).max() * varchar_multiplier
                    ))
                })
            elif 'datetime' in str(col.dtype):
                dtypedict.update({
                    col.name: types.DateTime()
                })
            elif 'float' in str(col.dtype):
                dtypedict.update({
                    col.name: types.Float(precision=np.modf(
                        col[0] * 100).astype(str).map(len).max(), asdecimal=True)
                })
            elif 'int' in str(col.dtype):
                dtypedict.update({
                    col.name: types.INT()
                })
        except:
            dtypedict.update({
                    col.name: types.VARCHAR(length=100)
                })
    return dtypedict