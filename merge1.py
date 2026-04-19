import pandas as pd

lobby1csv = pd.read_csv('data/raw/Top Contributors, 2015-2016.csv')[['Contributor','To Dems','To Repubs','Lean']]
lobby2csv = pd.read_csv('data/raw/Top Contributors, 2019-2020.csv')[['Contributor','To Dems','To Repubs','Lean']]
lobby3csv = pd.read_csv('data/raw/Top Contributors, 2023-2024.csv')[['Contributor','To Dems','To Repubs','Lean']]
grantcsv = pd.read_csv('data/raw/Transactions.csv')
maj = pd.read_csv('data/raw/HORMaj.csv')

matchedMajority = pd.merge(maj,grantcsv.rename(columns={"action_date_fiscal_year":"Year"}),on="Year", how="right")

matchedMajority = matchedMajority[['Year','Political Majority','recipient_name','total_obligated_amount']]

matchedMajority['loweredName'] = matchedMajority['recipient_name'].str.lower()
lobby1csv['loweredName'] = lobby1csv['Contributor'].str.lower
print(matchedMajority)

mergedTop = pd.merge(matchedMajority,lobby1csv,on="loweredName", how="inner")

print(mergedTop)



'''
merged = pd.merge(lobbycsv, grantcsv, left_on = 'Contributor', right_on = 'recipient_name', how = 'outer')
print(merged)
'''