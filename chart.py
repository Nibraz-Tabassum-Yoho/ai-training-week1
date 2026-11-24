import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 100, 180, 220]

plt.figure(figsize=(8, 5))

plt.bar(months, sales, color="steelblue")

plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
