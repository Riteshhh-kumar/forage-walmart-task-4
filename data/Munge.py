import sqlite3
import pandas as pd

sheet0 = pd.read_csv('C:\\Users\\rites\\OneDrive\\Documents\GitHub\\forage-walmart-task-4\\data\\shipping_data_0.csv') 
sheet1 = pd.read_csv('C:\\Users\\rites\\OneDrive\\Documents\GitHub\\forage-walmart-task-4\\data\\shipping_data_1.csv') 
sheet2 = pd.read_csv('C:\\Users\\rites\\OneDrive\\Documents\GitHub\\forage-walmart-task-4\\data\\shipping_data_2.csv') 

Connection = sqlite3.connect("shipment_database.db")
cur=Connection.cursor()
sheet0.to_sql('product',Connection,if_exists='replace',index=False)
sheet1.to_sql('shipment',Connection,if_exists='replace',index=False)
sheet2.to_sql('shipment',Connection,if_exists='replace',index=False)
