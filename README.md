# anagha_ops_backend

FastAPI backend for Anagha Ops, using SQLAlchemy models and startup migrations.

## Requirements

- Python 3.x
- `pip`

## Install

```bash
pip install -r requirements.txt
```

## Database configuration

Set `DATABASE_URL` before starting the app.

Example:

```bash
set DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@db.ncqspuxvxkqvuhbdazba.supabase.co:5432/postgres
```

If `DATABASE_URL` is not set, the app falls back to the Supabase connection string placeholder in `database.py`.

## Run locally

```bash
uvicorn main:app --reload
```

The API starts on `http://127.0.0.1:8000/` by default.

## Available route groups

- `/shops`
- `/dispatch`
- `/payments`
- `/admin`
- `/routes`
- `/auth`
- `/dashboard`

## Notes

- The app creates and updates the database schema on startup.
- Local export artifacts are intentionally not tracked in git:
  - `datastore/`
  - `export_datastore_csvs.py`
