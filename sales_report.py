from pathlib import Path
import webbrowser

sales = [
    {"product": "Notebook", "units": 120, "price": 3.50},
    {"product": "Backpack", "units": 45, "price": 39.99},
    {"product": "Water Bottle", "units": 80, "price": 14.25},
]

rows = ""
total = 0

for item in sales:
    revenue = item["units"] * item["price"]
    total += revenue
    rows += f"""
    <tr>
        <td>{item["product"]}</td>
        <td>{item["units"]}</td>
        <td>${revenue:,.2f}</td>
    </tr>"""

html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Sales Report</title>
</head>
<body>
    <h1>Sales Report</h1>
    <table border="1" cellpadding="8">
        <tr>
            <th>Product</th>
            <th>Units</th>
            <th>Revenue</th>
        </tr>{rows}
    </table>
    <p><strong>Total revenue: ${total:,.2f}</strong></p>
</body>
</html>
"""

page = Path("sales_report.html")
page.write_text(html, encoding="utf-8")

webbrowser.open(page.resolve().as_uri())
