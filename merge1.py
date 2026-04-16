import pandas as pd

lobbycsv = pd.read_csv('data/raw/Top Contributors, 2015-2016.csv')
grantcsv = pd.read_csv('data/raw/Transactions.csv')

print(grantcsv['recipient_name'])



'''
merged = pd.merge(lobbycsv, grantcsv, left_on = 'Contributor', right_on = 'recipient_name', how = 'outer')
print(merged)
'''