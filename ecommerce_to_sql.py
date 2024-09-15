import pandas as pd
import sqlite3
conn = sqlite3.connect('comm.db')
df = pd.read_csv('ecommerce.csv')
df.to_sql('ecommerce', conn, if_exists ="replace", index=False)