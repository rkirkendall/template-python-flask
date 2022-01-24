# Python/Flask with MySQL template for Crafting Sandbox

This is a Python/[Flask](https://flask.palletsprojects.com/en/2.0.x/) with MySQL template, configured for quick development setup in [Crafting Sandbox](https://docs.sandboxes.cloud/docs).

## Specifications

This template defines a single `/ping` route.
```python
@app.route('/ping')
def ping():
    ping = request.args.get('ping')
    if ping == "":
        ping = 'To ping, or not to ping; that is the question.'
    return jsonify(
        ping=ping,
        received_at=datetime.utcnow(),
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

## App Definition

The following [App Definition](https://docs.sandboxes.cloud/docs/app-definition) was used to create this template:

```yaml
endpoints:
- name: api
  http:
    routes:
    - pathPrefix: "/"
      backend:
        target: python-flask
        port: api
    authProxy:
      disabled: true
workspaces:
- name: python-flask
  description: Template backend using Python/Flask
  ports:
  - name: api
    port: 3000
    protocol: HTTP/TCP
  checkouts:
  - path: backend
    repo:
      git: https://github.com/crafting-dev/template-python-flask
dependencies:
- name: mysql
  serviceType: mysql
  version: '8'
  properties:
    database: superhero
    password: batman
    username: brucewayne
```
