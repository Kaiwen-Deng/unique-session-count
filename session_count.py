import os
import json
import glob
import time
import sys
import pandas as pd
import numpy as np

from datetime import datetime, timedelta

t0 = time.time()

input = sys.argv[1]

path_to_json = 'data/'

gap_duration = 1800  # seconds

dfs = []

json_pattern = os.path.join(path_to_json, '*.json')
file_list = glob.glob(json_pattern)

for file in file_list:
    data = pd.read_json(file, orient="records", lines=True)
    dfs.append(data)

df = pd.concat(dfs, ignore_index=True)  # combine all dataframes as one dataframe

def session_count(input):

    # modify timestamp when it is in microseconds
    df.loc[df.device_sent_timestamp > 10 ** 11, 'device_sent_timestamp'] = df[['device_sent_timestamp']] / 1000

    # drop the empty id
    df['anonymous_id'].replace('', np.nan, inplace=True)
    df.dropna(subset=['anonymous_id'], inplace=True)

    df_clean = df.sort_values(by=['anonymous_id', 'device_sent_timestamp'])
    df_clean[['diff_gap']] = df_clean[['device_sent_timestamp']] - df_clean[['device_sent_timestamp']].shift()
    diff_gap = df_clean.device_sent_timestamp.diff() > gap_duration
    diff_user = df_clean.anonymous_id != df_clean.anonymous_id.shift()
    session_id = (diff_user | diff_gap).cumsum()
    df_clean['session_id'] = session_id

    return print(df_clean.groupby(input).session_id.nunique().to_dict())

if __name__ == '__main__':
    session_count(input)
    t1 = time.time()
    print('Ran script in ' + str(timedelta(seconds=(t1 - t0))))
