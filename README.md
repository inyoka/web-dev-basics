# web-dev-basics

A beginner-friendly Flask web app for AQA and OCR A-Level Computer Science students. It demonstrates the fundamental aspects of web development using very simple, readable code.

The project is a **Study Tracker**: a student fills in a short form (their name, favourite subject, and hours studied), Flask processes the data, and a personalised result page is returned.

---

## 1. Folder structure

```
web-dev-basics/
├── app.py               # The Flask application — routes and logic
├── requirements.txt     # Python packages needed to run the project
├── templates/
│   ├── index.html       # The home page (the form)
│   └── result.html      # The result page (shows processed data)
└── static/
    ├── css/
    │   └── style.css    # Custom CSS styling
    └── js/
        └── script.js    # JavaScript for a small interactive feature
```

---

## 2. What each file does

### `app.py`
The main Python file. It creates the Flask app and defines two **routes** (URL addresses):

- The `/` route serves the home page with the form (**GET** request).
- The `/result` route receives the submitted form data (**POST** request), processes it, and returns the result page.

### `templates/index.html`
The home page. Contains an HTML form where the student enters their name, subject, and hours studied. Uses:

- **Bootstrap** (from a CDN) for a clean, responsive layout.
- **Font Awesome** (from a CDN) for small icons.
- **Google Fonts** (from a CDN) for the Nunito web font.
- Jinja's `url_for()` to link to the project's own CSS and JS files.

### `templates/result.html`
The result page. Uses **Jinja template variables** (`{{ student_name }}`, `{{ subject }}`, `{{ hours }}`) to display personalised content, and a Jinja `{% if %}/{% elif %}/{% else %}` block to show a different message depending on how many hours were studied.

### `static/css/style.css`
A small CSS file that adds custom styles on top of Bootstrap — for example, the page background colour, rounded card corners, and the Nunito web font.

### `static/js/script.js`
A small JavaScript file that adds a **live character counter** to the name input field. This is a simple example of how JavaScript can make a page interactive without sending anything to the server.

---

## 3. How to run the project locally

### Step 1 — Check Python is installed
Open a terminal and run:
```
python --version
```
You need Python 3.7 or later.

### Step 2 — Install Flask
```
pip install -r requirements.txt
```

### Step 3 — Run the app
```
python app.py
```

### Step 4 — Open the app in a browser
Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

Fill in the form and submit it to see the personalised result page.

---

## 4. Industry-standard habits

Even in this small project, several good habits are used that professional developers follow:

| Habit | Why it matters |
|---|---|
| Python, HTML, CSS, and JS are in separate files | Keeps code organised and easier to read, debug, and maintain |
| HTML lives in `templates/`, not inside Python strings | Separates presentation from logic (the MVC principle) |
| CSS and JS live in `static/` | Flask knows these are files to serve directly to the browser |
| Bootstrap and Font Awesome are loaded from a CDN | No need to download or host the files — the browser loads them automatically |
| `url_for()` builds paths to static files | Links still work correctly even if the app is hosted at a different URL path |
| `debug=True` is only used when running locally | Debug mode shows detailed error pages — this must never be switched on in production as it can expose sensitive information |
| `requirements.txt` lists dependencies | Makes it easy for anyone else to install exactly the right packages |

---

## 5. Possible next steps

Once you are comfortable with this project, here are some things you could try:

- **Add more form fields** — ask for the student's year group and show a more tailored message.
- **Add a third route** — create a simple `/about` page to practise defining new routes.
- **Add client-side validation** — use JavaScript to check the name field is not empty before the form is submitted.
- **Keep a running total** — store each session in a Python list so the page can show a summary of all sessions (without a database).
- **Improve the CSS** — try changing the colour scheme, adding hover effects, or adding a CSS animation.
- **Try `redirect` and `url_for`** — instead of rendering a template directly after a POST, redirect to another route (the Post/Redirect/Get pattern).
- **Connect a SQLite database** — once you are ready, this is the natural next step to make data persist between visits.
