import pandas as pd
data = {
    'Ad_Name': ['Ad_01', 'Ad_02', 'Ad_03', 'Ad_04', 'Ad_05'],
    'Spend_INR': [500, 1200, 300, 2500, 100],
    'Revenue_INR': [1500, 2000, 0, 8000, 50],
    'Clicks': [150, 400, 50, 900, 10]
}
df = pd.DataFrame(data)
df['ROAS'] = df['Revenue_INR'] / df['Spend_INR']
wasting_money = df[df['ROAS'] < 1]
winners = df[df['ROAS'] >= 3]
winners.to_excel('winning_ads_report.xlsx', index=False)
print("--- ALL ADS ---")
print(df)
print("\n--- WINNING ADS (To scale up) ---")
print(winners)
print("\nSuccess! Report 'winning_ads_report.xlsx' created.")