import pandas as pd

# lobby = pd.read_csv("data/raw/LobbyAmounts.csv")
awards = pd.read_csv("data/raw/Transactions.csv")
print(awards['cfda_title'])

# merged = pd.merge(lobby,awards.rename(columns={"action_date_fiscal_year":"Year"}),on="Year", how="outer")
# merged = merged[['Year','Lobby Amount','federal_action_obligation','total_obligated_amount','total_outlayed_amount_for_overall_award','cfda_title']]
# merged = merged.loc[merged['Lobby Amount']>0]
# merged = merged.loc[merged['federal_action_obligation']>0]
# merged = merged.loc[merged['total_obligated_amount']>0]
# merged = merged.loc[merged['total_outlayed_amount_for_overall_award']>0]


# print(merged)