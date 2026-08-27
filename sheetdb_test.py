import requests

# ✅ Your SheetDB API endpoint
url = "https://sheetdb.io/api/v1/08qhlpoo74lfz"
response = requests.get(url)
data = response.json()

# Helper function to clean and convert values
def to_float(value):
    try:
        return float(str(value).replace("$", "").replace("₱", "").replace(",", "").strip())
    except:
        return 0.0

# 1. Print products neatly
print("=== PRODUCTS ===")
for product in data:
    if isinstance(product, dict):
        name = product.get('Name', '')
        category = product.get('Category', '')
        cost = product.get('Cost', '')
        selling = product.get('SellingPrice', '')
        profit = product.get('Profit', '')
        local_selling = product.get('Local_SellingPrice', '')
        local_profit = product.get('Local_Profit', '')

        print(f"{name} ({category})")
        print(f"Cost: {cost} | Selling: {selling} | Profit: {profit}")
        print(f"Local Selling: {local_selling} | Local Profit: {local_profit}")
        print("---")

# 2. Calculate totals
total_usd = sum(to_float(p.get('Profit', 0)) for p in data if isinstance(p, dict))
total_php = sum(to_float(p.get('Local_Profit', 0)) for p in data if isinstance(p, dict))

print("\n=== SUMMARY ===")
print("Total Profit (USD):", round(total_usd, 2))
print("Total Profit (PHP):", round(total_php, 2))

# 3. Top 5 products by Local Profit
sorted_products = sorted(
    [p for p in data if isinstance(p, dict)],
    key=lambda x: to_float(x.get('Local_Profit', 0)),
    reverse=True
)

print("\n=== TOP 5 PRODUCTS BY LOCAL PROFIT ===")
for product in sorted_products[:5]:
    print(product.get('Name', ''), "-", round(to_float(product.get('Local_Profit', 0)), 2))

with open("result.txt", "w", encoding="utf-8") as f:
    f.write("=== SUMMARY ===\n")
    f.write(f"Total Profit (USD): {round(total_usd, 2)}\n")
    f.write(f"Total Profit (PHP): {round(total_php, 2)}\n\n")
    f.write("=== TOP 5 PRODUCTS BY LOCAL PROFIT ===\n")
    for product in sorted_products[:5]:
        f.write(f"{product.get('Name', '')} - {round(to_float(product.get('Local_Profit', 0)), 2)}\n")

