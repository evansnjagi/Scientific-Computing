# Import
import re

invoice = """
INVOICE NO: 10045
Date: 15/08/2024
Items:
  - Web Design     KES 35000
  - Hosting        KES 1200
  - Domain         KES 850
Total Due: KES 37050
"""

# 1. Extract the invoice number
match_invoiceNumber = re.search(r"\d{5}", invoice)

# 2. Extract all individual dates
match_dates = re.findall(r"\d{2}/\d{2}/\d{4}", invoice)

# 3. Extract all amounts as a whole unit
match_amounts = re.findall(r"KES\s\d+", invoice)

# Print the results
if match_invoiceNumber:
    invoice_number = match_invoiceNumber.group()
    print(f"Invoice Number: {invoice_number}")

if match_dates:
    print("Invoice Date: ", match_dates[0])
    
if match_amounts:
    print("Amounts: ", match_amounts)