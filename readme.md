# Readme.md still WIP

Setup:
- Install docker
- Install Python
- Clone repo: git clone https://github.com/Droei/game-analytics-pipeline.git
- Set up env: python -m venv .venv
- Activate env (always before running py commands): .\.venv\Scripts\activate
- Make sure pip is up to date: pip install --upgrade pip
- Install dependencies: pip install -r requirements.txt
- Enable the docker-compose to create a clickhouse container (make sure docker is open and leave the .venv): docker compose -f infra\docker-compose.yml up -d

Everything should be ready to go

