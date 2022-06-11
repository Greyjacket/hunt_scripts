import xlrd
import pandas as pd

file_errors_location = 'c2c.xlsx'
df = pd.read_excel(file_errors_location)

for row in df.iterrows():
    #print(row)
    pass

test = df.columns

with open('excel_rows.txt', 'a') as f:
    for col in df.columns:
        #print((col))
        f.write(col)



# Give the location of the file
# loc = ("c2c.xlsx")
 
# # To open Workbook
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
 
# # For row 0 and column 0
# print(sheet.cell_value(0, 0))
