import tabulate

def calculate_remaining_debt(total_debt, payments_made):
    remaining_debt = total_debt - sum(payments_made)
    return remaining_debt

def display_progress(total_debt, payments_made):
    table = []
    remaining_debt = total_debt

    for payment in payments_made:
        remaining_debt = calculate_remaining_debt(total_debt, payments_made)
        table.append([payment, remaining_debt])

    headers = ["Payment Made", "Remaining Debt"]
    print(tabulate.tabulate(table, headers, tablefmt="grid"))

# Example usage
total_debt = 1000
payments_made = [100, 200, 300, 150]

display_progress(total_debt, payments_made)
