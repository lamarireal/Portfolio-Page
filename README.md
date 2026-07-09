# Artem Pysmak Portfolio

A multilingual Django portfolio website for presenting personal information, skills, projects, social/contact links, and a development chronology. The site is designed as a polished frontend portfolio with animated atmospheric backgrounds, responsive sections, project detail pages, and admin-managed content.

## Overview

This project is a Django-based personal portfolio site. It combines static portfolio sections with dynamic content managed through the Django admin panel.

Main features:

- Multilingual interface: English, Spanish, and Ukrainian (`en`, `es`, `ua`).
- Localized database content for projects and chronology entries.
- Animated portfolio landing page with a layered visual background.
- Timeline/chronology section with collapsible extra entries.
- Skills gallery with uploaded logos.
- Project cards and project detail pages.
- Contact modal and social links.
- Production-ready Django settings using environment variables.
- WhiteNoise static file handling for deployment.
- Optional PostgreSQL configuration through `DATABASE_URL`.

## Tech Stack

- Python 3.14
- Django 6.0.6
- SQLite for local development
- PostgreSQL-ready production configuration
- WhiteNoise for static files
- Pillow for image fields
- python-dotenv for local environment variables
- HTML, CSS, and vanilla JavaScript

## Project Structure

```text
prtf_site/
|-- README.md
|-- requirements.txt
|-- .gitignore
`-- django_project/
    |-- manage.py
    |-- .env.example
    |-- db.sqlite3
    |-- locale/
    |   |-- es/LC_MESSAGES/
    |   `-- ua/LC_MESSAGES/
    |-- chronology_images/
    |-- project_images/
    |-- skill_logos/
    |-- mainapp/
    |   |-- admin.py
    |   |-- models.py
    |   |-- urls.py
    |   |-- views.py
    |   |-- migrations/
    |   |-- static/
    |   |   |-- js/
    |   |   `-- mainapp/
    |   `-- templates/mainapp/
    `-- mysite/
        |-- settings.py
        |-- urls.py
        |-- asgi.py
        `-- wsgi.py
```

## Main App Models

### `Project`

Stores portfolio projects.

Important fields:

- `title`, `description`, `tags`: English source content.
- `title_es`, `description_es`, `tags_es`: Spanish content.
- `title_ua`, `description_ua`, `tags_ua`: Ukrainian content.
- `image`: project image.
- `link`: external project link.
- `pub_date`: publication date.

The site automatically falls back to the English fields when a translation is empty.

### `ChronologyEntry`

Stores timeline entries for the chronology section.

Important fields:

- `title`, `description`: English source content.
- `title_es`, `description_es`: Spanish content.
- `title_ua`, `description_ua`: Ukrainian content.
- `date_label`: timeline date.
- `image`, `video_url`, `link`: optional media/link fields.
- `side`: left/right timeline layout side.

The chronology section shows the first two entries by default. Extra entries can be expanded with a wide animated toggle panel.

### `Skill`

Stores skills shown in the skills gallery.

Important fields:

- `name`
- `logo`
- `order`

## Multilingual Support

The project uses Django internationalization for static interface text and model helper methods for database content.

Supported languages:

- `en`: English
- `es`: Spanish
- `ua`: Ukrainian

Static translations live in:

```text
django_project/locale/es/LC_MESSAGES/django.po
django_project/locale/ua/LC_MESSAGES/django.po
```

Compiled translation files:

```text
django_project/locale/es/LC_MESSAGES/django.mo
django_project/locale/ua/LC_MESSAGES/django.mo
```

Language URLs:

```text
/       English
/es/    Spanish
/ua/    Ukrainian
```

Database content translation is handled through translated model fields. For example, if the current language is Spanish, `Project.localized_title()` uses `title_es` when it exists. If `title_es` is empty, it falls back to `title`.

## Local Development

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create local environment file

Copy:

```text
django_project/.env.example
```

to:

```text
django_project/.env
```

For local development, useful values are:

```env
DJANGO_SECRET_KEY=replace-this-with-a-local-secret-key
DJANGO_DEBUG=true
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000
DJANGO_SECURE_SSL_REDIRECT=false
DJANGO_SESSION_COOKIE_SECURE=false
DJANGO_CSRF_COOKIE_SECURE=false
DJANGO_SECURE_HSTS_SECONDS=0
DJANGO_SERVE_MEDIA=1
```

### 4. Apply migrations

```bash
python django_project/manage.py migrate
```

### 5. Create an admin user

```bash
python django_project/manage.py createsuperuser
```

### 6. Run the development server

```bash
python django_project/manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

## Managing Content

Most visible dynamic content is managed from the Django admin panel.

Admin models:

- Projects
- Chronology entries
- Skills

For projects and chronology entries, fill the English fields first. Spanish and Ukrainian fields are optional. If a translated field is empty, the site will display the English version.

Recommended content workflow:

1. Add or edit the English content.
2. Add Spanish translations where available.
3. Add Ukrainian translations where available.
4. Upload images through the admin panel.
5. Check each language route: `/`, `/es/`, `/ua/`.

## Static and Media Files

Static files:

- Source CSS/JS lives in `django_project/mainapp/static/`.
- Collected static files are written to `django_project/staticfiles/`.
- WhiteNoise serves collected static files in production.

Media files:

- Project images: `django_project/project_images/`
- Chronology images: `django_project/chronology_images/`
- Skill logos: `django_project/skill_logos/`

For simple deployments, media can be served by the web server. For larger deployments, use external object storage or a dedicated media server.

## Translation Workflow

When changing static text in templates:

1. Wrap text with Django translation tags:

```django
{% trans 'Projects' %}
```

2. Update `.po` files in `locale/es` and `locale/ua`.

3. Compile messages:

```bash
python django_project/manage.py compilemessages
```

If GNU gettext is not installed locally, `.po` files can still be edited manually, but `.mo` files must be compiled before deployment.

## Production Configuration

Production settings are controlled through environment variables.

Required variables:

```env
DJANGO_SECRET_KEY=your-real-production-secret-key
DJANGO_DEBUG=false
DJANGO_ALLOWED_HOSTS=example.com,www.example.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://example.com,https://www.example.com
```

Recommended HTTPS/security variables:

```env
DJANGO_SECURE_SSL_REDIRECT=true
DJANGO_SESSION_COOKIE_SECURE=true
DJANGO_CSRF_COOKIE_SECURE=true
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=true
DJANGO_SECURE_HSTS_PRELOAD=true
DJANGO_SECURE_REFERRER_POLICY=same-origin
DJANGO_X_FRAME_OPTIONS=DENY
```

Optional database variable:

```env
DATABASE_URL=postgres://USER:PASSWORD@HOST:5432/DB_NAME
```

If `DATABASE_URL` is not set, Django uses local SQLite:

```text
django_project/db.sqlite3
```

## Deployment Checklist

Before deployment:

```bash
python django_project/manage.py check --deploy
python django_project/manage.py makemigrations --check --dry-run
python django_project/manage.py migrate
python django_project/manage.py collectstatic --noinput
```

Production checklist:

- Set `DJANGO_DEBUG=false`.
- Set a strong `DJANGO_SECRET_KEY`.
- Set correct `DJANGO_ALLOWED_HOSTS`.
- Set correct `DJANGO_CSRF_TRUSTED_ORIGINS`.
- Configure HTTPS.
- Configure static file serving through WhiteNoise or the platform.
- Configure media file storage/serving.
- Run migrations.
- Run `collectstatic`.
- Create a superuser if needed.
- Verify `/`, `/es/`, `/ua/`, `/admin/`.

## Useful Commands

Run development server:

```bash
python django_project/manage.py runserver
```

Run Django checks:

```bash
python django_project/manage.py check
```

Run deployment checks:

```bash
python django_project/manage.py check --deploy
```

Create migrations:

```bash
python django_project/manage.py makemigrations
```

Apply migrations:

```bash
python django_project/manage.py migrate
```

Collect static files:

```bash
python django_project/manage.py collectstatic --noinput
```

Create superuser:

```bash
python django_project/manage.py createsuperuser
```

## Notes

- The project is configured to keep secrets in environment variables.
- `.env`, local SQLite databases, and collected static files should not be committed.
- `django_extensions` is loaded only in debug mode.
- The production settings are intentionally platform-neutral. Final deployment steps may change depending on the hosting provider.
