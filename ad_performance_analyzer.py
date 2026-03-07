import pandas as pd

# 1. Let's create some "Fake" messy marketing data
data = {
    'Ad_Name': ['Ad_01', 'Ad_02', 'Ad_03', 'Ad_04', 'Ad_05'],
    'Spend_INR': [500, 1200, 300, 2500, 100],
    'Revenue_INR': [1500, 2000, 0, 8000, 50],
    'Clicks': [150, 400, 50, 900, 10]
}

# 2. Load it into a "DataFrame" (Think of this as an Excel sheet inside Python)
df = pd.DataFrame(data)

# 3. CALCULATE: Let's find the ROAS (Revenue / Spend)
# This is a high-value marketing metric.
df['ROAS'] = df['Revenue_INR'] / df['Spend_INR']

# 4. FILTER: Show me only the ads that are "Wasting Money" (ROAS less than 1)
wasting_money = df[df['ROAS'] < 1]

# 5. FILTER: Show me the "Winning Ads" (ROAS more than 3)
winners = df[df['ROAS'] >= 3]

# 6. OUTPUT: Save the winners to a new Excel file for the client
winners.to_excel('winning_ads_report.xlsx', index=False)

print("--- ALL ADS ---")
print(df)
print("\n--- WINNING ADS (To scale up) ---")
print(winners)
print("\nSuccess! Report 'winning_ads_report.xlsx' created.")