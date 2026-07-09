# VPS Deployment Notes

These files are examples for a classic VPS deployment using:

- Gunicorn as the Django application server.
- systemd to keep Gunicorn running.
- nginx as the public reverse proxy and static/media file server.

The intended isolated deployment path is:

```text
/srv/artem-portfolio/
|-- current/
|-- venv/
`-- media/
```

Do not overwrite existing nginx sites or systemd services on a shared VPS. First inspect the server and choose a unique service name, socket path, domain, and project directory.

Typical deployment flow:

```bash
sudo mkdir -p /srv/artem-portfolio
sudo chown -R "$USER":"$USER" /srv/artem-portfolio
git clone <repo-url> /srv/artem-portfolio/current
python3 -m venv /srv/artem-portfolio/venv
/srv/artem-portfolio/venv/bin/pip install -r /srv/artem-portfolio/current/requirements.txt
cp /srv/artem-portfolio/current/django_project/.env.example /srv/artem-portfolio/current/django_project/.env
nano /srv/artem-portfolio/current/django_project/.env
/srv/artem-portfolio/venv/bin/python /srv/artem-portfolio/current/django_project/manage.py migrate
/srv/artem-portfolio/venv/bin/python /srv/artem-portfolio/current/django_project/manage.py collectstatic --noinput
```

After that, install the systemd and nginx configs with real paths/domains, then restart services.
