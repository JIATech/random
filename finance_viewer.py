import pickle
import tkinter as tk
import json

# Load transactions from pickle file
with open('transactions.pickle', 'rb') as file:
    transactions = pickle.load(file)

# Filter transactions based on a condition
filtered_transactions = [transaction for transaction in transactions if transaction['amount'] > 0]

# Create a GUI window
window = tk.Tk()

# Create a text widget to display the filtered transactions
text_widget = tk.Text(window)
text_widget.pack()

# Display the filtered transactions in the text widget
for transaction in filtered_transactions:
    text_widget.insert(tk.END, str(transaction) + '\n')
    
# for transaction in filtered_transactions: sums up by category
category_totals = {}
for transaction in filtered_transactions:
    category = transaction['category']
    amount = transaction['amount']
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount
    
# Create a label for each category total
for category, total in category_totals.items():
    label = tk.Label(window, text=f"{category}: {total}")
    label.pack()
    
# Create a button to export the filtered transactions to a json file
def export_transactions():
    with open('filtered_transactions.json', 'w') as file:
        json.dump(category_totals, file)
        
export_button = tk.Button(window, text="Export Transactions", command=export_transactions)
export_button.pack()

# Start the GUI event loop
window.mainloop()
