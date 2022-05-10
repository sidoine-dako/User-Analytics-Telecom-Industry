import pandas as pd
import numpy as np
class clean_data:
    def __init__(self,df:pd.DataFrame):
        self.df = df

    def missing_values(self,verbose=True):
        """This function compute the number of missing values per column, in the total and the percentage 
        of missing values.
        Inputs:
        -------
            verbose (default=True): whether the statistics relative to missing values should be printed
        """
        # Count missing values per column
        missingCountCol = self.df.isna().sum().sort_values(ascending=False)
        # Count the total number of missing values
        missingCountTot = missingCountCol.sum()
        # Percentage of missing values
        missingPerc = np.round(missingCountTot*100/self.df.size,2)

        if verbose==True:
            print(f"The dataset contains {missingCountTot} missing values in total\nThe missing values represent {missingPerc}% of the values contained in the set")
            print("These values are distributed as follows:")
            print(missingCountCol)

        return missingCountCol, missingCountTot, missingPerc

    def remove_duplicate(self,col:list)->pd.DataFrame:
        """This function remove the duplicates based on the variables listed in 'list' """
        dfWithoutDuplicated = self.df.drop_duplicates(col)
        return dfWithoutDuplicated

    def detect_outliers(self,col:list):
        """This function returns the outliers in a data set"""
        Q1 = self.df[col].quantile(.25)
        Q3 = self.df[col].quantile(.75)
        IQR = Q3-Q1
        # Total number of outliers per column
        ColName = Q1.index
        outliersCount = ((self.df.loc[:,ColName] > Q3 + 1.5 * IQR) | (self.df.loc[:,ColName] < Q1 - 1.5 * IQR)).sum()
        # Index of outliers per column
        outliersCol = dict()
        for colname in ColName:
            outlierList = np.where((self.df.loc[:,colname] > Q3[colname] + 1.5 * IQR[colname]) | (self.df.loc[:,colname] < Q1[colname] - 1.5 * IQR[colname]))
            outlierList = list(outlierList[0])
            outliersCol[colname] = outlierList
        return outliersCount, outlierList

if __name__ == "__main__":
    df = pd.read_csv("..\data\Week1_challenge_data_source(CSV).csv")
    data = clean_data(df=df)
    data.missing_values()