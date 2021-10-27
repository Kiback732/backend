# python-sample-app

Sample Python application on Flask with PostgreSQL database

Deployment
---

* install Python 3.6
* install libs `pip install -r requirements.txt`
* set flask environment `export FLASK_APP=app.py`
* set DB environment `export POSTGRESQL_URL=postgresql://worker:worker@localhost/app`
* migrate database `flask db upgrade`
* start application `python3 app.py` (app listen on `0.0.0.0:5000`)

Requirements
---

* Python 3.6
* postgresql 12

Docs
---

see [swagger specs](openapi.yaml)

License
---

MIT / BSD

Author Information
---

This app was created in 2019 by [Maxim Baranov](https://github.com/mbaran0v).
