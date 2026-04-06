# IssueSense - AI Complaint System

IssueSense is a Flask app that classifies complaints, stores them in Supabase, and provides a dashboard for analytics and resolution tracking.

## Features
- Complaint classification with ML model
- Sentiment analysis and priority mapping
- Dashboard with charts and metrics
- Resolved complaints workflow

## Requirements
- Python 3.9+ recommended
- Supabase project and table

## Environment Variables
Create a `.env` file (or set these in your deployment environment):
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `SECRET_KEY`

## Supabase Table
Create a table named `complaints` with these fields (minimum):
- `id` (primary key)
- `complaint_text` (text)
- `predicted_category` (text)
- `sentiment` (text)
- `status` (text, optional; used for resolved status)
- `created_at` (timestamp, optional)

## Local Setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Deployment (GitHub -> Hosting)
This repo includes a `Procfile` for Gunicorn:
```
web: gunicorn app:app
```

Typical steps (Heroku/Render/Railway style):
1. Push this project to GitHub.
2. Create a new web service and connect the GitHub repo.
3. Set build command:
   ```
   pip install -r requirements.txt
   ```
4. Set start command:
   ```
   gunicorn app:app
   ```
5. Add environment variables (`SUPABASE_URL`, `SUPABASE_KEY`, `SECRET_KEY`).
6. Deploy.

## Notes
- If your host requires a Python version file, add `runtime.txt` with a supported version, e.g. `python-3.11.6`.
- The dashboard excludes resolved complaints from active totals.

## Routes
- `/` - Submit a complaint
- `/dashboard` - Analytics dashboard
- `/resolve` - Admin resolve workflow
