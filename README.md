# Python and HTML: From Web Pages to Simple Apps

**BAIM 3220: Introduction to Python**

In this module, you'll build a basic web page, use Python to create and display HTML, and make an interactive app with Streamlit. You'll finish by building a number-guessing game.

## Learning Goals

By the end of this module, you will be able to:

- Explain what HTML does and identify common tags
- Write and open a simple HTML page
- Use Python to generate an HTML page from data
- Build a simple user interface with Streamlit
- Use `st.session_state` to remember values in a Streamlit app

## Before You Start

You'll need a code editor such as VS Code, a web browser, and Conda. Conda keeps this module's Python and packages in their own **environment**, separate from everything else on your computer.

### Step 1: Install Miniconda

Miniconda is a small installer for Conda. If you already have Anaconda or Miniconda, skip to Step 2.

Download the graphical installer for your computer from the [Miniconda install page](https://www.anaconda.com/docs/getting-started/miniconda/install), then run it and accept the default settings.

- **Mac:** Choose **Apple Silicon** for an M-series Mac or **Intel** for an older one. To check, open the Apple menu and select **About This Mac**.
- **Windows:** Choose the 64-bit installer.

### Step 2: Open a Terminal

- **Mac:** Open **Terminal**. If it was already open during the install, close it and open a new one.
- **Windows:** Open **Anaconda Prompt** from the Start menu. Use this instead of Command Prompt, which may not recognize `conda`.

Check that Conda works:

```bash
conda --version
```

### Step 3: Get the Module Files

The files for this module are in the [intro-html repository](https://github.com/iportilla/intro-html). Use either option to put them in a folder named `intro-html` in your Downloads folder.

**Option A: Download a ZIP**

1. Open the repository, select **Code**, then select **Download ZIP**.
2. Unzip the file in your Downloads folder.
3. Rename the unzipped folder from `intro-html-main` to `intro-html`.

**Option B: Clone with Git**

If you have Git installed, run these commands.

Mac:

```bash
cd ~/Downloads
git clone https://github.com/iportilla/intro-html.git
```

Windows:

```bat
cd %USERPROFILE%\Downloads
git clone https://github.com/iportilla/intro-html.git
```

Now move into the folder.

Mac:

```bash
cd ~/Downloads/intro-html
```

Windows:

```bat
cd %USERPROFILE%\Downloads\intro-html
```

> The folder already includes the example files. When a section below says to create a file, you can open the existing one instead. `guess_number.py` contains the starter code for the exercise.

### Step 4: Create and Activate the Environment

These commands are the same on Mac and Windows:

```bash
conda create -n baim3220-web python=3.12 -y
conda activate baim3220-web
```

Your prompt should now start with `(baim3220-web)`.

### Step 5: Install the Packages

Install Streamlit, plus Jupyter for the notebook version of this module:

```bash
python -m pip install streamlit notebook
```

Check that Streamlit installed:

```bash
python -m streamlit --version
```

### Each Time You Come Back

The environment stays on your computer, so you only create it once. For each new work session, open your terminal, go to your `intro-html` folder as in Step 3, and activate it:

```bash
conda activate baim3220-web
```

To open the notebook, run `jupyter notebook`. When you're done, stop any running app with `Ctrl+C`, then run `conda deactivate`.

> **VS Code:** Open the Command Palette (`Cmd+Shift+P` on Mac, `Ctrl+Shift+P` on Windows), select **Python: Select Interpreter**, and choose `baim3220-web`.

### Troubleshooting

| Problem | Fix |
| --- | --- |
| `conda` isn't recognized | Mac: open a new Terminal window. Windows: use Anaconda Prompt. |
| Conda asks you to accept its Terms of Service | Enter `a` at the prompt, or run `conda tos accept`, then run the command again. |
| `No module named streamlit` | Run `conda activate baim3220-web`, then try again. |
| Your prompt doesn't show `(baim3220-web)` | Run `conda activate baim3220-web`. |
| Port 8501 is already in use | Stop the other app with `Ctrl+C`. Streamlit may also pick the next open port, so check the terminal for the address. |

### Module Files

Your `intro-html` folder contains these files. The two marked files appear after you run the scripts or the notebook.

```text
intro-html/
├── .gitignore
├── LICENSE
├── README.md
├── app.py
├── click_counter.py
├── guess_number.py
├── hello.html
├── html_with_python.ipynb
├── python_page.html       (created by render_page.py)
├── render_page.py
├── sales_report.html      (created by sales_report.py)
└── sales_report.py
```

---

## Part 1: Simple HTML Pages

**HTML (HyperText Markup Language)** describes the structure of a web page. It uses **tags** to label each piece of content. Most tags come in pairs, with content between them:

```html
<p>This is a paragraph.</p>
```

### Common Tags

| Tag | Purpose |
| --- | --- |
| `<h1>` to `<h6>` | Headings, from largest to smallest |
| `<p>` | Paragraph |
| `<a href="...">` | Link |
| `<ul>` and `<li>` | Bulleted list and list item |
| `<table>`, `<tr>`, `<th>`, `<td>` | Table, row, header cell, and data cell |
| `<img src="..." alt="...">` | Image (this tag has no closing tag) |

### Example: `hello.html`

Create a file named `hello.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Page</title>
</head>
<body>
    <h1>Hello, Buffs!</h1>
    <p>This is my first web page.</p>

    <h2>Things I'm learning</h2>
    <ul>
        <li>Python</li>
        <li>HTML</li>
        <li>Streamlit</li>
    </ul>

    <p>Learn more at <a href="https://www.python.org">python.org</a>.</p>
</body>
</html>
```

Double-click the file to open it in your browser.

The `<head>` holds information about the page, such as the title on the browser tab. The `<body>` holds what visitors see.

### Try It

1. Change the heading to include your name.
2. Add a fourth item to the list.
3. Add a new paragraph about your major.
4. Save the file and refresh your browser.

---

## Part 2: Rendering HTML with Python

An HTML page is just text, so Python can create one like any other string. Your browser then **renders** that text, turning the tags into a formatted page.

### Example 1: Write and Open a Page

Create `render_page.py`:

```python
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
```

Run it:

```bash
python render_page.py
```

The script saves `python_page.html` and opens it in your default browser.

### Example 2: Build a Page from Data

Python becomes especially useful when the page depends on data. This script uses a loop to build one table row per product.

Create `sales_report.py`:

```python
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
```

Notice how the code combines three familiar ideas:

- A **list of dictionaries** stores the data.
- A **`for` loop** creates each table row.
- An **f-string** inserts the values into the HTML.

### Example 3: Render HTML in a Jupyter Notebook

If you're working in Jupyter or Google Colab, you can show HTML directly in the notebook:

```python
from IPython.display import HTML, display

display(HTML("<h2>Hello from a notebook!</h2><p>No browser tab needed.</p>"))
```

### Try It

1. Add two more products to `sales`.
2. Add a **Price** column to the table.
3. Add a line that shows the best-selling product by revenue.

---

## Part 3: Introduction to UI with Streamlit

A **user interface (UI)** is the part of a program that people see and interact with. Our HTML pages so far only display information. **Streamlit** lets you build interactive web apps in Python, without writing HTML yourself.

### Example: `app.py`

Create `app.py`:

```python
import streamlit as st

st.title("Tip Calculator")
st.write("Enter your bill to see the tip and total.")

name = st.text_input("Your name")
bill = st.number_input("Bill amount ($)", min_value=0.0, value=25.0, step=1.0)
tip_percent = st.slider("Tip (%)", min_value=0, max_value=30, value=20)

tip = bill * tip_percent / 100
total = bill + tip

st.write(f"Tip: ${tip:.2f}")
st.write(f"Total: ${total:.2f}")

if st.button("Say thanks"):
    if name:
        st.success(f"Thanks, {name}!")
    else:
        st.warning("Enter your name first.")
```

Run it from your terminal:

```bash
python -m streamlit run app.py
```

Streamlit opens the app in your browser, usually at `http://localhost:8501`. Press `Ctrl+C` in the terminal to stop it.

> Use `streamlit run`, not `python app.py`, to start a Streamlit app.

### Common Streamlit Elements

| Code | What it shows |
| --- | --- |
| `st.title("Text")` | Large page title |
| `st.write(value)` | Text, numbers, tables, and more |
| `st.text_input("Label")` | Text box |
| `st.number_input("Label")` | Number box |
| `st.slider("Label", 0, 10)` | Slider |
| `st.button("Label")` | Button that returns `True` when clicked |
| `st.success("Text")` | Green message |
| `st.warning("Text")` | Yellow message |
| `st.error("Text")` | Red message |

### How Streamlit Runs Your Code

**Every time a user interacts with the app, Streamlit reruns your script from top to bottom.**

That means regular variables start over on every click. To keep a value between reruns, store it in `st.session_state`, which works much like a dictionary:

```python
import streamlit as st

if "clicks" not in st.session_state:
    st.session_state.clicks = 0

if st.button("Click me"):
    st.session_state.clicks += 1

st.write(f"Clicks: {st.session_state.clicks}")
```

You'll need this idea for the exercise below.

### Try It

1. Add a number input for how many people are splitting the bill.
2. Display the amount each person owes.
3. Show a warning if the tip is below 10%.

---

## Part 4: Exercise: Guess the Number

Build a Streamlit game in which the app picks a secret whole number less than 10, and the user tries to guess it.

### Requirements

Your app must:

1. Pick a random whole number from 1 to 9.
2. Keep the same secret number until the user starts a new game.
3. Let the user enter a guess from 1 to 9.
4. Tell the user whether the guess is too low, too high, or correct.
5. Count the number of guesses.
6. Include a **New game** button that picks a new number and resets the count.

### Starter Code

Create `guess_number.py`:

```python
import random
import streamlit as st

st.title("Guess the Number")
st.write("I'm thinking of a whole number from 1 to 9.")

# TODO 1: If "secret" isn't in st.session_state yet,
# store a random number and set "attempts" to 0.

guess = st.number_input("Your guess", min_value=1, max_value=9, step=1)

if st.button("Guess"):
    # TODO 2: Add 1 to the number of attempts.

    # TODO 3: Compare guess to the secret number.
    # Show "Too low", "Too high", or a success message.
    pass

# TODO 4: Display the number of attempts.

if st.button("New game"):
    # TODO 5: Pick a new secret number and reset attempts to 0.
    # Then call st.rerun() to refresh the page.
    pass
```

Run it:

```bash
python -m streamlit run guess_number.py
```

### Hints

- Use `random.randint(1, 9)`. It includes both 1 and 9.
- Look back at the `clicks` example for the `st.session_state` pattern.
- Use `if`, `elif`, and `else` to compare the guess to the secret number.
- If the secret number changes after each guess, it probably isn't being stored in `st.session_state`.

### Bonus Challenges

- Limit the player to 4 guesses.
- Add an easy mode (1 to 9) and a hard mode (1 to 99).
- Celebrate a correct guess with `st.balloons()`.
- Show a list of the player's previous guesses.

### Submit

Turn in `guess_number.py` and a screenshot of your app after a correct guess.
