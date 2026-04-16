import pandas as pd

lobby = pd.read_csv("LobbyingMon.csv")
awards = pd.read_csv("Transactions")

merged = pd.merge(lobby,awards.rename(columns={"action_date_fiscal_year":"Year"}),on="Year", how="outer")
merged = merged[['feder_action_obligation','total_obligated_amount','total_outlayed_amount_for_overall_award',]]