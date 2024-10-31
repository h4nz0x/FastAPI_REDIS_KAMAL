# FastAPI Redis Docker Application

This application is a FastAPI-based web service that integrates with Redis for data caching and storage. It's designed to demonstrate a simple yet powerful setup using Docker for containerization and Kamal for deployment.
This a setup that deploys a fastapi application using docker and redis using kamal accessories all deployed on hetzner server(s).

## Application Overview

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Redis**: An in-memory data structure store, used as a database, cache, and message broker.
- **Docker**: Used for containerizing the application and its dependencies.
- **Kamal**: A deployment tool that simplifies the process of shipping web apps.

## Features

- FastAPI web server with example endpoints
- Redis integration for data storage and retrieval
- Docker containerization for easy setup and deployment
- Kamal configuration for streamlined deployment process
- Hetzner Cloud for hosting

## Prerequisites

- Docker
- Kamal (for deployment)

## Running the Application Locally

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Build the Docker image:
   ```
   docker build -t fastapi-redis-app .
   ```

3. Run the Docker container:
   ```
   docker run -p 8000:8000 -e REDIS_HOST=<redis-host> -e REDIS_PORT=<redis-port> fastapi-redis-app
   ```
   Replace `<redis-host>` and `<redis-port>` with your Redis server details.

4. Access the application at `http://localhost:8000`

5. Test the Redis connection at `http://localhost:8000/redis`

6. Check the application health at `http://localhost:8000/up`

## Deployment with Kamal

This project uses Kamal for deployment. Kamal simplifies the process of deploying Docker containers to remote servers.

1. Ensure you have Kamal installed:
   ```
   gem install kamal
   ```

2. Configure your deployment settings in `config/deploy.yml`

3. Set up your environment variables:
   - For CI/CD, ensure these variables are set in your pipeline (e.g., GitHub Actions secrets)

4. Deploy your application:
   ```
   kamal setup
   kamal deploy
   ```

## Project Structure

- `main.py`: The main FastAPI application file
- `Dockerfile`: Defines the Docker image for the application
- `config/deploy.yml`: Kamal deployment configuration
- `requirements.txt`: Python dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)


