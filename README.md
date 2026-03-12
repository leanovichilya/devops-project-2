# DevOps Project 2

## Description
Simple Flask application that returns JSON response.
Deployed to AWS EC2 with automated CI/CD pipeline.

## Technologies
- Python / Flask
- Docker / Docker Compose
- PostgreSQL
- GitHub Actions (CI/CD)
- AWS EC2

## How to run locally
1. Clone the repository
2. Create `.env` file:
```
   POSTGRES_PASSWORD=pass
   POSTGRES_USER=user
   POSTGRES_DB=mydb
```
3. Run with Docker Compose:
```bash
   docker compose up --build
```
4. Open http://localhost:5000/home

## CI/CD
On every push to `main`:
- Runs tests
- Builds Docker image
- Deploys to AWS EC2 automatically
