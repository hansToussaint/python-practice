#! python3
# blank_row_inserter.py - Takes 2 integers and an excel file name (put in command line)
# If N M and example.xlsx, the program put from N'th line M blank rows

import os, sys, openpyxl

desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
os.chdir(desktop)

def blank_row_inserter(N, M, doc):
    # Reading the content of the excel document
    wb = openpyxl.load_workbook(doc)
    sheet = wb.active

    # Writing the spreasheet
    new_wb = openpyxl.Workbook()
    new_sheet = new_wb.active
    
    for row in range(1, sheet.max_row + 1):
        if row < N:
            new_row = row
        else:
            new_row = row + M

        # Copy each cell
        for col in range(1, sheet.max_column + 1):
            new_sheet.cell(row=new_row, column=col, value=sheet.cell(row=row, column=col).value)

    new_wb.save(f'{doc}_blank_row.xlsx')
    print('Done')

if len(sys.argv) > 3:
    from_line = int(sys.argv[1])
    blank_rows = int(sys.argv[2])
    document = sys.argv[3]
else:
    print("""In the command Line you have to write:\n
            blank_row_inserter N M example.xlsx\n
            N -int, from the line to start\n
            M - int, number of rows\n
            example.xlsx - excel document
            """)
    sys.exit()

blank_row_inserter(from_line, blank_rows, document)
