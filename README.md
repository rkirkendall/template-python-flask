# Python Flask template for Cloud Sandbox

This is a Python [Flask]() template, for quick development setup in Cloud Sandbox.

## Specifications

The following `App configuration` was used to create this template:

```yaml
endpoints:
- http:
    routes:
    - backend:
        port: http
        target: py-flask
      path_prefix: /
  name: app
services:
- description: A python/flask template
  name: py-flask
  workspace:
    checkouts:
    - path: template-python-flask
      repo:
        git: https://github.com/crafting-dev/template-python-flask.git
    ports:
    - name: http
      port: 3000
      protocol: HTTP/TCP
```

To run the app:
```bash
$ export FLASK_APP=flaskr
$ python3 -m flask run
```