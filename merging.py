import pandas as pd

lobby = pd.read_csv("data/raw/LobbyAmounts.csv")
awards = pd.read_csv("data/raw/Transactions.csv")

print(awards[['federal_action_obligation']])

merged = pd.merge(lobby,awards.rename(columns={"action_date_fiscal_year":"Year"}),on="Year", how="outer")
merged = merged[['Year','Lobby Amount','federal_action_obligation','total_obligated_amount','total_outlayed_amount_for_overall_award']]
merged = merged.iloc[merged['Lobby Amount'].isna==False]
print(merged)