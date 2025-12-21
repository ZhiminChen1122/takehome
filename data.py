# %%
import os 
import pandas as pd
os.chdir('/Users/zhiminchen/Downloads')

df = pd.read_csv('2PL_Item_Parameters.csv')

df.info()
df.describe()

# second degree users 


def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    df1 = follow.groupby('followee').agg(
        num_followees = ('follower', 'count')
        ).reset_index()
    
    df2 = follow.groupby('follower').agg(
        num_followers = ('followee', 'count')
    ).reset_index()

    df = df1.merge(df2, left_on = 'followee', right_on = 'follower', how = 'left')

    df = df[ (df.num_followees > 0) & (df.num_followers >0)]

    df = df[['followee', 'num_followers']].rename(
        columns = {'num_followers' : 'num'
                   , 'followee': 'follower'}
    ).sort_values('follower', ascending = True) 

    return df