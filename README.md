# gae-webapp-base

A minimal base for GAE webapp for basic JSON API action. Includes the following libraries:

1. flask (https://palletsprojects.com/p/flask/)
1. requests (https://2.python-requests.org/en/master/)
1. requests-toolbelt (https://github.com/requests/toolbelt)

### Dev setup

1. Install Python 2.7.x
    1. Its probably preferable to run it with `pyenv` (https://github.com/pyenv/pyenv)
1. Run `python get_requirements.py` which will download the requirements into the `libs` folder
1. Download the latest GAE SDK (https://console.cloud.google.com/storage/browser/appengine-sdks/featured?prefix=google_appengine)
1. Unpack the SDK to somewhere accessible
1. Run `python $PATH_TO_SDK/google_appengine/dev_appserver.py ./app.yaml`

### Pushing into GAE servers

1. Run `python ../google_appengine/appcfg.py update ./ --noauth_local_webserver`
1. Open the link to go through the Google authorization process
1. Get the token and paste on terminal
1. Wait for update to be pushed to GAE servers
