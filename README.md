# Blog App API

Django REST Framework API that allows admins to create and manage BlogPosts (including image upload), Tags, Categories and Users through the Django Admin interface and provides JSON REST API for retrieving lists and instance details.
Dockerized with Nginx, PostgreSQL and GUnicorn for Django, to be production-ready.

## Prerequisites 
To use these files, you must first have the following installed:
-   [Docker](https://docs.docker.com/engine/installation/)
-   [docker-compose](https://docs.docker.com/compose/install/)

## Usage
The following steps will run a local instance using the default configuration file (`docker-compose.yml`):

1.  Clone this repository.
2.  Change directory into the root of the project.
3.  Run the `docker-compose up` command.

```
git clone https://github.com/Thewest123/blog-app-api.git
cd blog-app-api
docker-compose up
```    

## Endpoints
 - /admin - Django Administration
 - /api/blog - Blog API Root
 - /api/token - Obtain JWT Token Pair
 - /docs - Simple SwaggerUI API documentation
