from heapq import merge
import pandas as pd
import functools as ft
class extract_data:
    def __init__(self,df:pd.DataFrame):
        self.df = df
    
    def extract_Session(self,identifier:str,session='Bearer Id'):
        NSession = self.df[[identifier,session]].groupby(identifier).count()
        NSession = NSession.rename(columns={session:'Number of session'})
        return NSession

    def sum_duration(self,identifier:str,durationCol='Dur. (s)'):
        sumDuration = self.df[[identifier,durationCol]].groupby(identifier).sum()
        return sumDuration

    def extract_SocialMedia(self,identifier:str):
        SocialMediaCol = [col for col in self.df.columns if 'Social Media' in col]
        SocialMediaCol.append(identifier)
        SocialMediaData = pd.Series(self.df[SocialMediaCol].groupby(identifier).sum().sum(1),name='Social Media')
        return SocialMediaData

    def extract_Google(self,identifier:str):
        GoogleCol = [col for col in self.df.columns if 'Google' in col]
        GoogleCol.append(identifier)
        GoogleData = pd.Series(self.df[GoogleCol].groupby(identifier).sum().sum(1),name="Google")
        return GoogleData

    def extract_Email(self,identifier:str):
        EmailCol = [col for col in self.df.columns if 'Email' in col]
        EmailCol.append(identifier)
        EmailData = pd.Series(self.df[EmailCol].groupby(identifier).sum().sum(1),name="Email")
        return EmailData

    def extract_Youtube(self,identifier:str):
        YoutubeCol = [col for col in self.df.columns if 'Youtube' in col]
        YoutubeCol.append(identifier)
        YoutubeData = pd.Series(self.df[YoutubeCol].groupby(identifier).sum().sum(1),name="Youtube")
        return YoutubeData

    def extract_Gaming(self,identifier:str):
        GamingCol = [col for col in self.df.columns if 'Gaming' in col]
        GamingCol.append(identifier)
        GamingData = pd.Series(self.df[GamingCol].groupby(identifier).sum().sum(1),name="Gaming")
        return GamingData

    def extract_Other(self,identifier:str):
        OtherCol = [col for col in self.df.columns if 'Other' in col]
        OtherCol.append(identifier)
        OtherData = pd.Series(self.df[OtherCol].groupby(identifier).sum().sum(1),name="Other")
        return OtherData

    def extract_Total(self,identifier:str):
        TotalCol = [col for col in self.df.columns if 'Total' in col]
        TotalCol.append(identifier)
        TotalData = pd.Series(self.df[TotalCol].groupby(identifier).sum().sum(1),name="Total")
        return TotalData

    def extract_TotalUL(self,identifier:str,totalULCol='Total UL (Bytes)'):
        TotalUL = self.df[[identifier,totalULCol]].groupby(identifier).sum()
        return TotalUL

    def extract_TotalDL(self,identifier:str,totalDLCol='Total DL (Bytes)'):
        TotalDL = self.df[[identifier,totalDLCol]].groupby(identifier).sum()
        return TotalDL
    
    def merge_data(self,identifier:str):
        NSession = self.extract_Session(identifier)
        sumDuration = self.sum_duration(identifier)
        SocialMediaData = self.extract_SocialMedia(identifier)
        GoogleData = self.extract_Google(identifier)
        EmailData = self.extract_Email(identifier)
        YoutubeData = self.extract_Youtube(identifier)
        GamingData = self.extract_Gaming(identifier)
        OtherData = self.extract_Other(identifier)
        TotalUL = self.extract_TotalUL(identifier)
        TotalDL = self.extract_TotalDL(identifier)
        TotalData = self.extract_Total(identifier)
        try:
            Data = [NSession,sumDuration,SocialMediaData,GoogleData,EmailData,YoutubeData,GamingData,OtherData,TotalUL,TotalDL,TotalData]
            df_final = ft.reduce(lambda left,right: pd.merge(left,right,left_index=True,right_index=True,
        validate="one_to_one"),Data)
        except KeyError:
            print("Please check for the name of your features")
            df_final = None
        return df_final
