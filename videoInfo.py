import pandas as pd
from datetime import datetime

class VideoInfo:
    def __init__(self, post_url, account, views, likes, saved, caption, hashtags, date_posted):
        self.PostURL = post_url
        self.Account = account
        self.Views = views
        self.Likes = likes
        self.Saved = saved
        self.Caption = caption
        self.Hashtags = hashtags
        self.Dateposted = date_posted
        self.Datecollected = datetime.now().strftime("%m/%d/%Y")  # Current date and time

    def to_dataframe_row(self):
        row = {
            'PostURL': self.PostURL,
            'Account': self.Account,
            'Views': self.Views,
            'Likes': self.Likes,
            'Saved': self.Saved,
            'Caption': self.Caption,
            'Hashtags': self.Hashtags,
            'Dateposted': self.Dateposted,
            'Datecollected': self.Datecollected
        }
        return row

    def write_to_dataframe(self, dataframe):
        row = self.to_dataframe_row()
        dataframe = pd.concat([dataframe, pd.DataFrame([row])], ignore_index=True)
        return dataframe