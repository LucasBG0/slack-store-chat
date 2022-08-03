# slack-store-chat

## Run project

```sh
$ docker build . -t slackstorechat
$ docker run --name slackstorechat -d -p 5000:5000 -e "SLACK_BOT_TOKEN=<add your token here>" -v $(pwd):/app slackstorechat
```

## Install a package

1. First add the package in `requirements.txt`.
2. Run the bellow command to install directly in container:

```sh
$ docker exec slackstorechat pip install --no-cache-dir --upgrade -r requirements.txt
```
