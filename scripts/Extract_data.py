import pandas as pd
class extract_data:
    def __init__(self,df:pd.DataFrame):
        self.df =df
    
    def extract_SocialMedia(self):
        SocialMediaCol = [col for col in self.df.columns if 'Social Media' in col]
        return self.df[SocialMediaCol].sum(1)

    def extract_Google(self):
        GoogleCol = [col for col in self.df.columns if 'Google' in col]
        return self.df[GoogleCol].sum(1)

    def extract_Email(self):
        EmailCol = [col for col in self.df.columns if 'Email' in col]
        return self.df[EmailCol].sum(1)