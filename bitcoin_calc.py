import pandas as pd

from coindesk import btc_interval


def bpi_df(start, end):
    btc = btc_interval(start, end)
    btc = btc['bpi']
    df = pd.DataFrame(list(btc.items()), columns=['Date', 'USD'])
    return df


def percent_change(df):
    return df['USD'].pct_change()


def merger(df, df2):
    merge_df = df.merge(df2.to_frame(), left_index=True, right_index=True)
    merge_df.columns = ['USD', 'Date', 'percent_change']
    return merge_df


def high_percents(merge_df):
    date_inc = merge_df[merge_df['percent_change'] > 0.09]
    return date_inc['Date']


def low_percents(merge_df):
    date_dec = merge_df[merge_df['percent_change'] < -0.09]
    return date_dec['Date']
