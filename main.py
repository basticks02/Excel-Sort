import pandas as pd
df = pd.read_excel('calls_export_09-03-2024_3-53-15_pm.xlsx')


selected_columns = df['Date']
print(selected_columns)

