import pandas as pd
import functools as ft
class extract_data:
    def __init__(self,df:pd.DataFrame):
        self.df = df
    
    def extract_SocialMedia(self,identifier:str):
        SocialMediaCol = [col for col in self.df.columns if 'Social Media' in col]
        return self.df[SocialMediaCol].groupby(identifier).sum().sum(1)

    def extract_Google(self,identifier:str):
        GoogleCol = [col for col in self.df.columns if 'Google' in col]
        return self.df[GoogleCol].groupby(identifier).sum().sum(1)

    def extract_Email(self,identifier:str):
        EmailCol = [col for col in self.df.columns if 'Email' in col]
        return self.df[EmailCol].groupby(identifier).sum().sum(1)

    def extract_Youtube(self,identifier:str):
        YoutubeCol = [col for col in self.df.columns if 'Youtube' in col]
        return self.df[YoutubeCol].groupby(identifier).sum().sum(1)

    def extract_Gaming(self,identifier:str):
        GamingCol = [col for col in self.df.columns if 'Gaming' in col]
        return self.df[GamingCol].groupby(identifier).sum().sum(1)

    def extract_Other(self,identifier:str):
        OtherCol = [col for col in self.df.columns if 'Youtube' in col]
        return self.df[OtherCol].groupby(identifier).sum().sum(1)