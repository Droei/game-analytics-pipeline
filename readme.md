# Readme.md still WIP

Python - FastApi - Clickhouse
- Python is great for data analysis and applying Ai algorithms to finding connections between form data and game data
- FastApi, personal preference from previous experience, LIGHT WEIGHT BABYYYYY, easy to pick up and amazing documentation
- Clickhouse, golden standard for anyting analysis based. Works column based rather than row based, meaning its way more efficient with processing analythical requests but falls flat when working with complex databases

Setup:
- Install docker
- Install Python
- Clone repo: git clone https://github.com/Droei/game-analytics-pipeline.git
- Set up .venv for installs: python -m venv .venv
- Activate env (always before running py commands): .\.venv\Scripts\activate
- Make sure pip is up to date: pip install --upgrade pip
- Install dependencies: pip install -r requirements.txt
- Enable the docker-compose to create a clickhouse container (make sure docker is open and leave the .venv): docker compose -f infra\docker-compose.yml up -d
- Run the project with: uvicorn ingestion.app.main:app --reload

Everything should be ready to go

