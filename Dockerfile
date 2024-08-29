FROM python:3.8

# update and upgrade apt
RUN apt-get update && \
    apt-get upgrade --yes

# create non-root user
RUN useradd demo

# set workdir as
WORKDIR /home/demo

# create virtualenv in docker
ENV VIRTUALENV=/home/demo/venv
RUN python -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

# copy requirements
COPY --chown=demo requirements/base.txt ./base.txt
COPY --chown=demo requirements/prod.txt ./prod.txt

# install dependencies
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r prod.txt

# copy project files config folder and app folders
COPY --chown=demo myapp ./myapp
COPY --chown=demo setup ./setup
COPY --chown=demo manage.py ./manage.py
COPY entrypoints/prod-start.sh ./

# env settings
RUN mkdir .env
COPY .env/env.prod  ./.env/env.prod

# copy start app script and set to entrypoint
RUN chmod +x ./prod-start.sh

#ENTRYPOINT ["/home/demo/prod-start.sh"]