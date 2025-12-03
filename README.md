This is a Flask WorkBuddy application. It supports user registration and login, and stores tasks per user in a SQLite database.

Quick start

1. Create and activate a virtual environment (Windows PowerShell):
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the app:
```
python run.py
```

Database

The app uses SQLite stored at `instance/todo.db`. To reset the DB during development remove that file and restart the app.

Deploy to GitHub (summary)

- Initialize git, commit files, create a remote on GitHub, and push. See the `Deploy` section below for commands.

Deploy (commands)

PowerShell commands to initialize and push the repo:

```
cd "C:\Users\91908\Documents\Python\PROJECTS\TODO_APP"
git init
git add .
git commit -m "Initial commit"
# create a repo on GitHub via the CLI (optional):
# gh repo create <OWNER>/<repo-name> --public --source=. --remote=origin --push
# OR create the repo on github.com and then:
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

Optional: Add GitHub Actions workflows if you want CI.
