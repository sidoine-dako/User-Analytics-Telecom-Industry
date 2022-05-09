from heapq import merge
import pandas as pd
import functools as ft
class extract_data:
    def __init__(self,df:pd.DataFrame):
        self.df = df
    
    def extract_SocialMedia(self,identifier:str):
        SocialMediaCol = [col for col in self.df.columns if 'Social Media' in col]
        SocialMediaData = pd.Series(self.df[SocialMediaCol].groupby(identifier).sum().sum(1),name='Social Media')
        return SocialMediaData

    def extract_Google(self,identifier:str):
        GoogleCol = [col for col in self.df.columns if 'Google' in col]
        GoogleData = pd.Series(self.df[GoogleCol].groupby(identifier).sum().sum(1),name="Google")
        return GoogleData

    def extract_Email(self,identifier:str):
        EmailCol = [col for col in self.df.columns if 'Email' in col]
        EmailData = pd.Series(self.df[EmailCol].groupby(identifier).sum().sum(1),name="Email")
        return EmailData

    def extract_Youtube(self,identifier:str):
        YoutubeCol = [col for col in self.df.columns if 'Youtube' in col]
        YoutubeData = pd.Series(self.df[YoutubeCol].groupby(identifier).sum().sum(1),name="Youtube")
        return YoutubeData

    def extract_Gaming(self,identifier:str):
        GamingCol = [col for col in self.df.columns if 'Gaming' in col]
        GamingData = pd.Series(self.df[GamingCol].groupby(identifier).sum().sum(1),name="Gaming")
        return GamingData

    def extract_Other(self,identifier:str):
        OtherCol = [col for col in self.df.columns if 'Youtube' in col]
        OtherData = pd.Series(self.df[OtherCol].groupby(identifier).sum().sum(1),name="Other")
        return OtherData

    def merge_data(self,identifier:str):
        SocialMediaData = self.extract_SocialMedia(identifier)
        GoogleData = self.extract_Google(identifier)
        EmailData = self.extract_Email(identifier)
        YoutubeData = self.extract_Youtube(identifier)
        GamingData = self.extract_Gaming(identifier)
        OtherData = self.extract_Other(identifier)
        Data = [SocialMediaData,GoogleData,EmailData,YoutubeData,GamingData,OtherData]
        df_final = ft.reduce(lambda left,right: pd.merge(left,right,left_index=True,right_index=True,
        validate="one_to_one"),Data)
        return df_final
