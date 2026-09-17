# Django Prack

## Deploying to Vercel

Vercel detects `manage.py` and uses the project's build command to run migrations.

Set `DJANGO_SECRET_KEY` and `DATABASE_URL` in the Vercel project environment
variables before deploying. Both are mandatory: the application will not start
without them.
You may also set `DJANGO_ALLOWED_HOSTS` and `DJANGO_CSRF_TRUSTED_ORIGINS` as
comma-separated lists to add permitted hosts and trusted origins.

SQLite storage is not used and would be ephemeral on Vercel. Use a managed
PostgreSQL database and its `DATABASE_URL` for reliable login, sessions, admin,
and book creation.
