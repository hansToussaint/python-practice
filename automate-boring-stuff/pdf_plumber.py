import os, pdfplumber, sys, re, openpyxl

desktop = os.path.join(os.path.expanduser("~"), 'Desktop')

#2 - open and read pdf
with pdfplumber.open(os.path.join(desktop, 'Air Canada - Détail de la réservation.pdf')) as pdf:
    print(f"number of pages: {len(pdf.pages)}")

    page = pdf.pages[0]
    text = page.extract_text()
    print(text)

# Read all
with pdfplumber.open('document.pdf') as pdf:
    text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    print(text)

#4 - encodage
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text)

#5 - tables
with pdfplumber.open('document.pdf') as pdf:
    page = pdf.pages[0]

    tables = page.extract_tables()

    for table in tables:
        for row in table:
            print(row)

#7 - exo
#7.1
def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = len(pdf.pages)
        text = '\n'.join(page.extract_text() or "" for page in pdf.pages)

    return text, pages

def save_text(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

def main():
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        print("Enter please the path of the pdf")
        sys.exit()

    os.chdir(desktop)

    text, pages = extract_text(pdf_path)
    
    name = os.path.splitext(os.path.basename(pdf_path))[0]
    save_text(text, name + ".txt")

    print("Pages:", pages)
    print("Caractères:", len(text))
    
# main()

#7.2
def pdf_invoice_reader(pdf_path):
    #Open and extract pdf
    with pdfplumber.open(pdf_path) as pdf:
        invoice = '\n'.join(page.extract_text() or "" for page in pdf.pages)

    # regex invoice - (see practice regex.py exercise 8.1)
    invoice_number = re.search(r"FAC-\d{4}-\d{4}", invoice).group()
    date = re.search(r"\d{1,2}\s+\w+\s+\d{4}", invoice).group()
    client = re.search(r"Client:\s*(.+)", invoice).group(1)
    postal_code = re.search(r"[A-Z]\d[A-Z]\s*\d[A-Z]\d", invoice).group()
    total = re.search(r"TOTAL:\s*(\d+\.\d+)", invoice).group(1)
    analysis = re.findall(r"Analyse\s+([\w\.]+)", invoice)
    line_totals = re.findall(r"\d+\.\d+\$\s+(\d+\.\d+)\$", invoice)

    #   Pour ne pas planter, normalement il faut faire
    #match = re.search(r"FAC-\d{4}-\d{4}", invoice)
    #invoice_number = match.group() if match else None

    # return a dict with the data
    data = {
        "Invoice Number": invoice_number,
        "Date": date,
        "Client": client,
        "Postal code": postal_code,
        "Total": total,
        "Analysis": analysis,
        "Total of lines": line_totals
    }

    return data

#7.3 - pdf to excel
def pdf_extractor(pdf_path):
    # Extract
    with pdfplumber.open(pdf_path) as pdf:
        # number of pages
        pages = len(pdf.pages)

        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""

        # number of words
        words = len(text.split())

        return pages, words

def main_func(folder_path):
    wb = openpyxl.Workbook()
    sheet = wb.active

    sheet["A1"] = "Fichier"
    sheet["B1"] = "Pages"
    sheet["C1"] = "Mots"

    row = 2
    
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, file)

            pages, words = pdf_extractor(pdf_path)

            sheet.cell(row=row, column=1, value=file)
            sheet.cell(row=row, column=2, value=pages)
            sheet.cell(row=row, column=3, value=words)

            row += 1

    wb.save("resume_pdfs.xlsx")
