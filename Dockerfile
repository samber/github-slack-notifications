#
# docker build -t samber/github-slack-notifications .
# docker run --rm -it -e GITHUB_OAUTH_TOKEN=****** -e SLACK_WEBHOOK=****** samber/github-slack-notifications
#

FROM python:3

MAINTAINER Samuel BERTHE <contact@samuel-berthe.fr>

CMD ["python", "/usr/src/app/app.py"]

RUN pip install requests

RUN mkdir /usr/src/app
COPY . /usr/src/app
