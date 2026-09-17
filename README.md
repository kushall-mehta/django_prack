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

## Creating users

Local development can use SQLite:

```powershell
$env:DEBUG = "True"
python manage.py migrate
python manage.py createsuperuser
```

The same user must be created separately in the remote PostgreSQL database.
To create the first remote admin during the Vercel build, add these Production
environment variables and redeploy:

```text
DJANGO_ADMIN_USERNAME
DJANGO_ADMIN_EMAIL
DJANGO_ADMIN_PASSWORD
```

The deployment build runs migrations and creates this admin only if it does not
already exist. It never overwrites an existing user's password. After login,
use `/admin/` to manage additional users.
