# Django Prack

## Deploying to Vercel

Vercel detects `manage.py` and uses the project's build command to run migrations.

Set `DJANGO_SECRET_KEY` in the Vercel project environment variables before deploying.
You may also set `DJANGO_ALLOWED_HOSTS` and `DJANGO_CSRF_TRUSTED_ORIGINS` as
comma-separated lists to add permitted hosts and trusted origins.

SQLite storage is ephemeral on Vercel. For reliable login, sessions, admin, and
book creation, use managed PostgreSQL and configure the application with its
`DATABASE_URL`.
