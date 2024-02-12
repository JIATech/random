import tkinter as tk
import pickle
import json

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.load_transactions()

    def add_transaction(self, amount, category):
        transaction = {'amount': amount, 'category': category}
        self.transactions.append(transaction)
        self.save_transactions()

    def get_total_balance(self):
        total_balance = 0
        for transaction in self.transactions:
            total_balance += transaction['amount']
        return total_balance

    def get_historical_transactions(self):
        return self.transactions

    def create_gui(self):
        root = tk.Tk()

        amount_label = tk.Label(root, text="Cantidad:")
        amount_label.pack()
        amount_entry = tk.Entry(root)
        amount_entry.pack()

        category_label = tk.Label(root, text="Categoría:")
        category_label.pack()
        category_entry = tk.Entry(root)
        category_entry.pack()

        def add_transaction():
            amount = float(amount_entry.get())
            category = category_entry.get()
            self.add_transaction(amount, category)
            amount_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
            update_total_balance()

        add_button = tk.Button(root, text="Añadir Transacción", command=add_transaction)
        add_button.pack()

        total_balance_label = tk.Label(root, text="Balance:")
        total_balance_label.pack()
        total_balance_value = tk.Label(root, text="0")
        total_balance_value.pack()

        def update_total_balance():
            total_balance = self.get_total_balance()
            total_balance_value.config(text=str(total_balance))

        update_button = tk.Button(root, text="Actualizar Balance", command=update_total_balance)
        update_button.pack()

        transactions_label = tk.Label(root, text="Historial de Transacciones:")
        transactions_label.pack()
        transactions_text = tk.Text(root, height=10, width=50)
        transactions_text.pack()

        def update_historical_transactions():
            transactions = self.get_historical_transactions()
            transactions_text.delete(1.0, tk.END)
            for transaction in transactions:
                transactions_text.insert(tk.END, f"Cantidad: {transaction['amount']}, Categoría: {transaction['category']}\n")

        update_transactions_button = tk.Button(root, text="Actualizar Transacciones", command=update_historical_transactions)
        update_transactions_button.pack()

        def clear_transactions():
            self.transactions = []
            self.save_transactions()
            update_historical_transactions()

        clear_transactions_button = tk.Button(root, text="Limpiar Transacciones", command=clear_transactions)
        clear_transactions_button.pack()
        
        def export_transactions():
            with open('transactions.json', 'w') as file:
                json.dump(self.transactions, file)
        
        export_transactions_button = tk.Button(root, text="Exportar Transacciones", command=export_transactions)
        export_transactions_button.pack()

        root.mainloop()

    def save_transactions(self):
        with open('transactions.pickle', 'wb') as file:
            pickle.dump(self.transactions, file)

    def load_transactions(self):
        try:
            with open('transactions.pickle', 'rb') as file:
                self.transactions = pickle.load(file)
        except FileNotFoundError:
            self.transactions = []

tracker = FinanceTracker()
tracker.create_gui()
# START: be15d9bcejpp

print("Total balance:", tracker.get_total_balance())
print("Historical transactions:", tracker.get_historical_transactions())
