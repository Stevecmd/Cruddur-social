FROM newrelic/infrastructure:latest

# Install Tini
RUN apk add --no-cache tini

# Set Tini as the entry point
ENTRYPOINT ["/sbin/tini", "--"]

# Copy your configuration or application files
ADD newrelic-infra.yml /etc/newrelic-infra.yml
