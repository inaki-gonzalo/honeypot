# Basic Honey Pot
Intercepts requests to a dummy HTTP server and logs them in Splunk.

# Prerequisites
* python3
* docker
* docker-compose.
* Splunk server with HTTP collector setup.

# Setup
Create .env file with Splunk configs.

`SPLUNK_URL=1.2.3.4 # Update with your url.`

`SPLUNK_TOKEN=xxxx-xxx-xxxxx-xxxx # Update with your HTTP collector token.`

# Run
Execute:
`docker-compose up -d`

# Stop
Execute:
`docker-compose down -v --rmi local`
