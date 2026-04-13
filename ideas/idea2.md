Analyze the correlation between political party in control of Congress and the presidency to the annual spending.

External data set: 
1. https://history.house.gov/Institution/Presidents-Coinciding/Party-Government/ has a csv file regarding the Congress number, Majority in both house and senate, presidency party/president and if the government was unified or divided.


Possible subsets: 
1. Cols of interest for All_Contracts_Prime...:
federal_action_obligation - amount of money for the transaction
total_dollars_obligated - total amount committed so far - correlates directly to total_obligated amount

award_id_piid correlates to award_id_fain

possibly product_or_service_code_description - useful to annalyze what the government directly bought.

2. Cols of interest for All_Assistance_Prime...:
federal_action_obligation - amount gov agreed to spend in this transaction
total_obligated_amount - cumulative cost
total_outlayed_amount_for_overall_award - Actual amount paid rather than promised

awarding_agency_name - Depatment that awarded the funds
awarding_sub_agency_name - specific sub agency that awarded

action_date/action_date_fiscal_year - both can group by year and by date for chronilogical order.
