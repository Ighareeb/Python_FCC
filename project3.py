# Budget App
class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list()

    # UTILS
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    # DEPOSIT / WITHDRAW / TRANSFER
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.category}"):
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    # Format response string
    def __str__(self):
        output = self.category.center(30, "*") + "\n"
        for item in self.ledger:
            output += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        output += f"Total: {self.get_balance()}"
        return output


# Non-class function that takes a list of categories as an argument. It should return a string that is a bar chart.
def create_spend_chart(categories):
    # calculate total withdrawn for each category
    total_withdrawl = sum(
        sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        for category in categories
    )

    # Calculate % of total withdrawl for each category
    percentages = [
        (
            category.category,
            sum(item["amount"] for item in category.ledger if item["amount"] < 0)
            / total_withdrawl
            * 100,
        )
        for category in categories
    ]

    # Create bar chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for _, percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1)

    # Format category names
    names = [name for name, _ in percentages]
    max_length = max(len(name) for name in names)
    for i in range(max_length):
        chart += "\n     "
        for name in names:
            chart += name[i] + "  " if i < len(name) else "   "

    return chart
