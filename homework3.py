#!/home/fei/anaconda3/bin/python

import os 
import sys
import pandas as pd
import sqlite3
from urllib.request import pathname2url


# Do not show traceback statements
sys.tracebacklimit=0

def create_dataframe(inputDb):

    if(os.path.exists(inputDb) != True):
        raise ValueError("Invalid path to a database.")
    else:
        sql = """
        select video_id, category_id, 'us' as language from USvideos
        union all 
        select video_id, category_id, 'gb' as language from GBvideos 
        union all 
        select video_id, category_id, 'fr' as language from FRvideos
        union all 
        select video_id, category_id, 'de' as language from DEvideos
        union all 
        select video_id, category_id, 'ca' as language from CAvideos
        """
        conn = sqlite3.connect(inputDb)
        df = pd.read_sql_query(sql, conn)
    return(df)
