import pandas as pd
import numpy as np


def read_csv():
    df=pd.read_csv('./recurring_transactions_case.csv')
    return df
    

def get_unique_customers():
    return set(df['client_hash'])
    
    

def omit_same_day_transaction():
    df1=pd.DataFrame()
    cust_set=get_unique_customers()#getting all the customers
    for cust in cust_set:
        temp=df.loc[df['client_hash']==cust]
        merch_set=set(temp['merchant_name'])#getting unique merchant_name for each customer
        for merch in merch_set:
            temp1=temp.loc[temp['merchant_name']==merch]#creating sub frame of a customer for a unique merchant
            temp2=temp1.drop_duplicates(subset=['date'])#Dropping recurrent transaction happend same day to a merchant
            df1=df1.append(temp2)
    return df1

    
def split_time_date(temp_df):#function to split time and date
    time=list()
    date=list()
    for i in temp_df:
        temp=i.split(' ')
        #print(i)
        #print(temp)
        date.append(temp[0])
        time.append(temp[1])
    #print(time)
    return date,time
    
    
df=read_csv()#Readinf data
date,time=split_time_date(df['emitted_at'])#Splitting the value in emitted_at column
df['time']=time#making new column for sake of ease
df['date']=date
df1=omit_same_day_transaction()#Removing recurrent transactions
df1.to_csv('r.csv')#saving cleansed dataset in csv file
df2=df1.loc[df['client_hash']=='ad83f05b4eb6221d99e6f0dd0dfbcd7c']
df2.to_csv('r1.csv')#saving results for a single user
print('Count of transaction for specific user before cleansing the data:'+str(np.sum(df['client_hash']=='ad83f05b4eb6221d99e6f0dd0dfbcd7c')))
print('Count of transaction for specific user after cleansing the data:'+str(np.sum(df1['client_hash']=='ad83f05b4eb6221d99e6f0dd0dfbcd7c')))
print('Length of dataset:'+str(len(df)))
print('Lenght of cleansed dataset:'+str(len(df1)))
#print(df.head())