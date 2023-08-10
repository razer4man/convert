"""GEt user's input and convert it to float amount."""

# User's prompted input
user_input: str = input("Enter your payment, BYN: ")

# Float amount
amount: float = float(user_input.replace(" ", "").replace(",", "."))
