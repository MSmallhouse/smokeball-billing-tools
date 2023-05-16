# INSTRUCTIONS:
# 1. On Smokeball Billing in Chrome, navigate to a matter
# 2. Click the "CSV" button to download a file with this matter's billing history
# 3. The lines containing empty_bill_field may be commented out to ignore entries not already associated to a bill
# 4. Enter the filename of the downloaded csv when prompted
# 5. Enter the number of the invoice with time entries to combine
# 6. Make sure to check resulting output csv for errors (Excel is okay for this)
# 
# This will add new time entries for all of the rows in the csv, which can then be manually added to a bill

import pandas as pd

def add_to_end(date, subject, hours, description):
    result.loc[len(result.index)] = [date, subject, hours, description]
    return result

# to store the combined data that I want
result = pd.DataFrame(columns=['Date', 'Subject', 'Hours', 'Description']) 

filename = input("Enter filename: ")
invoice_number = input("Enter desired invoice number: ")
if '#' not in invoice_number:
    invoice_number = '#' + invoice_number

df = pd.read_csv(filename, skiprows=5)

empty_bill_field = df[df['Billed'].isna()]
df = df.loc[(df['Billed'] == invoice_number)]
df = pd.concat([df, empty_bill_field], sort=True)
df = df.drop(columns=['Staff', 'Matter', 'Activity', 'Rate', 'Amount', 'Billable?'])

prev_date = ""
subject = ""
description = ""
hours = 0
for index, row in df.iterrows():
    if index == 0:
        prev_date = row['Date']
        description = f'* {row["Subject"]}'
        hours = row['Hours']
        subject = f"Services provided on {row['Date']}:"
        continue

    if row['Date'] == prev_date: # still on same date
        description = f'{description}\n* {row["Subject"]}'
        hours += row['Hours']

    else: # moved on to new date 
        add_to_end(prev_date, subject, hours, description)
        hours = row['Hours']
        prev_date = row['Date']
        description = f'* {row["Subject"]}'
        subject = f"Services provided on {row['Date']}:"

add_to_end(prev_date, subject, hours, description)

result.to_csv('combined-bill.csv', index=False)