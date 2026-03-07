import pandas as pd
data = {
    'Ad_Name': ['Ad_01', 'Ad_02', 'Ad_03', 'Ad_04', 'Ad_05', 'Ad_06'],
    'Spend_INR': [500, 1200, 300, 2500, 100, 1500],
    'Revenue_INR': [1500, 2000, 0, 8000, 50, 4500],
    'Clicks': [150, 400, 50, 900, 10, 120]
}
df = pd.DataFrame(data)
df['ROAS'] = df['Revenue_INR'] / df['Spend_INR']
df['CPC'] = df['Spend_INR'] / df['Clicks']
high_performing_ads = df[(df['Clicks'] > 100) & (df['ROAS'] > 2)]
high_performing_ads.to_excel('final_marketing_report.xlsx', index=False)
print("--- FULL PROCESSED DATA ---")
print(df)
print("\n--- HIGH PERFORMING ADS (CLICK > 100 & ROAS > 2) ---")
print(high_performing_ads)