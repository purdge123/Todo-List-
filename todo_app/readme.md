# Todo List API

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. **Build and Start Containers**

   Run the following command to build the Docker images and start the containers:

   ```bash
   docker-compose up --build

## Run Migrations

Run the migrations to set up the database schema:

bash
Copy code
docker-compose run web python manage.py migrate

## Create Superuser

Create a superuser for accessing the Django admin interface:

bash
Copy code
docker-compose run web python manage.py createsuperuser

## Import Postman Collection

To test and explore the API, import the Postman collection:

1. Open Postman.
2. Click on the "Import" button.
3. Select "File" and choose the `api_spec.json` file from the project directory.
4. Click "Import."
