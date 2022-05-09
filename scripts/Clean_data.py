import pandas as pd
import numpy as np
class clean_data:
    def __init__(self,df:pd.DataFrame):
        self.df = df

    def missing_values(self,verbose=True):
        # Count missing values per column
        missingCountCol = self.df.isna().sum()

        # Count the total number of missing values
        missingCountTot = missingCountCol.sum()

        # Percentage of missing values
        missingPerc = np.round(missingCountTot*100/self.df.size,2)
