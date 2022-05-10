from xmlrpc.client import Boolean
import pandas as pd
import numpy as np
class clean_data:
    def __init__(self,df:pd.DataFrame):
        self.df = df

    def right_type(self,objType:list):
        self.df[objType] = self.df[objType].astype(str).replace('nan',np.nan)

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

    def fillMissing(self,func=None):
        """This function fill the NA with either the mean or the median.
        It uses the mean if the distribution of the column is symmetric and the median otherwise."""
        numCols = self.df.select_dtypes([np.number]).columns
        if func == "mean":
            for col in numCols:
                valToFill = self.df[col].mean()
                self.df[col] = self.df[col].fillna(valToFill)
        elif func =="median":
            for col in numCols:
                valToFill = self.df[col].median()
                self.df[col] = self.df[col].fillna(valToFill)
        else:
            skewList = self.df[numCols].skew()
            for col in skewList.index:
                if abs(skewList[col])>1:
                    valToFill = self.df[col].median()
                    self.df[col] = self.df[col].fillna(valToFill)
                else:
                    valToFill = self.df[col].mean()
                    self.df[col] = self.df[col].fillna(valToFill)

    def remove_duplicate(self,col:list)->pd.DataFrame:
        """This function remove the duplicates based on the variables listed in 'list' """
        dfWithoutDuplicated = self.df.drop_duplicates(col)
        return dfWithoutDuplicated

    def detect_outliers(self):
        """This function returns the outliers in a data set"""
        col = self.df.select_dtypes([np.number]).columns
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
        return outliersCount, outlierList, outliersCol

if __name__ == "__main__":
    df = pd.read_csv("..\data\Week1_challenge_data_source(CSV).csv")
    data = clean_data(df=df)
    data.missing_values()