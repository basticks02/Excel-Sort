import pandas as pd
df = pd.read_excel('calls_export_09-03-2024_3-53-15_pm.xlsx', header=1)

def find_unanswered_phone_calls(df):
    unanswered_calls = []
    inbound_calls = df[df['Type'] == 'inbound']
    grouped = inbound_calls.groupby('Calling Number')

    for calling_number, group in grouped:
        if (group['Duration (min)'] == '0s').all():
            unanswered_calls.append(calling_number)

    return unanswered_calls

unanswerd_in_calls = find_unanswered_phone_calls(df)
print(unanswerd_in_calls)

# print(df.columns)


