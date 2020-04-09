FROM gitpod/workspace-full

USER root
# Setup Heroku CLI
RUN curl https://cli-assets.heroku.com/install.sh | sh

# Setup MongoDB
RUN apt-get update -y
RUN apt-get -y install libmemcached-dev

USER gitpod
# Local environment variables
# C9USER is temporary to allow the MySQL Gist to run
ENV C9_USER="gitpod"
ENV PORT="8080"
ENV IP="0.0.0.0"
ENV C9_HOSTNAME="localhost"

USER root
# Switch back to root to allow IDE to load