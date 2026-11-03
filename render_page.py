from pathlib import Path
import webbrowser

html = """<!DOCTYPE html>
<html>
<head>
    <title>Made with Python</title>
</head>
<body>
    <h1>This page was created by Python</h1>
    <p>Python wrote this HTML to a file.</p>
</body>
</html>
"""

page = Path("python_page.html")
page.write_text(html, encoding="utf-8")

webbrowser.open(page.resolve().as_uri())
