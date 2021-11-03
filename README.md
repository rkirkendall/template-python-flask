# Python/Flask with MySQL template for Crafting Sandbox

This is a Python/[Flask](https://flask.palletsprojects.com/en/2.0.x/) with MySQL template, configured for quick development setup in [Crafting Sandbox](https://crafting.readme.io/docs).

## Specifications

This template defines a single `/ping` route.
```python
@app.route('/ping')
def ping():
    return jsonify(
        ping=request.args.get('ping'),
        received_at=datetime.now(),
    )
```

It accepts a ping query string, and responds with the query string and current time. For example:
```bash
$ curl --request GET 'localhost:3000/ping?ping=hello'
{"ping":"hello","received_at":"XXX, XX XXX XXXX XX:XX:XX GMT"}
```

[`.sandbox/manifest.yaml`](.sandbox/manifest.yaml) sets up sandbox in development mode (Debug Mode):
```yaml
- FLASK_APP=flaskr
- FLASK_ENV=development
```

These environment variables can also be set manually:
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
```

Host is modified to `--host=0.0.0.0` to make the server publicly available. Port is also modified to `--port=3000`, which is the port defined in App configuration for the app.

[`config.py`](config.py) contains the mysql connection configuration. See the [flask mysql](https://flask-mysql.readthedocs.io/en/latest/#configuration) docs for more.

You can launch the app by running:
```bash
python3 -m flask run
```

## App configuration

The following [App configuration](https://crafting.readme.io/docs/app-spec) was used to create this template:

```yaml
endpoints:
- http:
    routes:
    - backend:
        port: http
        target: python-flask
      path_prefix: /
  name: app
services:
- description: Python/Flask template
  name: python-flask
  workspace:
    checkouts:
    - path: src/template-python-flask
      repo:
        git: https://github.com/crafting-dev/template-python-flask.git
    ports:
    - name: http
      port: 3000
      protocol: HTTP/TCP
- managed_service:
    properties:
      database: superhero
      password: batman
      username: brucewayne
    service_type: mysql
    version: "8"
  name: mysql
```
