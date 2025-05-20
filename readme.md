# Fender Engineering Challenge - Auth API

## Overview :earth_americas:

Hello! :wave:

My name is [David Jiménez Rodríguez](https://linkedin.com/in/david-jr1792) and this is the code repository for the technical assessment given as part of the recruitment process for the **Software Engineer** position at Fender :guitar:

## Solution :bulb:
The solution is made using the **Python** :snake: language, since it is the language that I am most familiar with and the one that was asked for in the assessment. I decided to use **FastAPI** as my web framework, with **Pydantic** to build my data models. 

The solution uses **Amazon DynamoDB**, a **NoSQL** key-value database in a single-table design pattern, to store the objects. A local version of DynamoDB is created and all operations happen inside a table called `fender`.

Once deployed, the API exposes the following endpoints:
- `GET /health`
- `POST /api/login`
- `POST /api/logout`
- `POST /api/users/register`
- `GET /api/users/me`
- `PATCH /api/users/me`
- `DELETE /api/users/me`

Aside from exposing the API, the project also has a [web UI](http://localhost:8001) for monitoring the database and a Swagger API [documentation page](http://localhost:8080/docs), accessible **once deployed**. These can be used to get more information on the exposed endpoints and the actual data being created.

### Assumptions
Here are some of the assumptions made on the assigment, from which a lot of the data handling and validation is based off:

- The `email` field on a User must be unique, and a valid email address
- The `password` field on a User must have between 4 and 128 characters
- The `POST /api/register` endpoint returns a `204` status code, leading to a user login
- The endpoint to update user data uses a `PATCH` operation instead of `PUT` to be able to handle partial updates (makes sense imagining a UI on top the API)
- The access tokens (JWT's) must be stored in the database in order for the `/api/logout` endpoint to revoke these tokens (not a very usual pattern with token-based auth)
- If the user attempts to log in with invalid credentials or tries to use an invalid token, a `401` status code is expected

## Testing and deployment :computer:
### Environment setup :gear:

These are the prerequisites for running the app and its dependencies:

- **Docker** and **Docker Compose** installed
- Ports `8000`, `8001` and `8080` **available**

A `.env` file has been left out of .gitignore on purpose so that you don't need to create it by hand. This would contain the specific configuration and sensitive data in a real deployment.

All of the commands used to deploy, test and clean up the project must be ran in the root directory.

### Deployment :rocket:

To run the app, run the following command:

```bash
scripts/deploy.sh
```

This will run the app and expose it on port `8080` of the local machine.

The **API docs** are now accesible at http://localhost:8080/docs

### Testing :mag:
To run the unit/integration code tests, run the following command:

```bash
scripts/test.sh
```

This will run `pytest` inside of the Docker container and give a report of the results.

### Cleanup :broom:

To clean up all of the resources created by the app, run the following command:

```bash
scripts/cleanup.sh
```

This will remove all of the containers, images and volumes related to the Compose stack.

## Future improvements :soon:
Here are some of the thing I would improve, if I had more time and knowledge about the use case:

- Evaluate the **persistence** of the access tokens and the `/api/logout` endpoint. Token-based authentication using JWT does **not** usually persist tokens.
- Write an **async** wrapper over the DynamoDB operations to utilize FastAPI to its best potential performance-wise
- Write more detailed **tests** to handle edge cases and exceptions
- Improve the **exception handling** logic to give more complete responses
- Verify the password requirements and add **regex** matching
- Add functionality to handle **refresh tokens** and **password recovery**
- Implement a much more complete **logging** implementation
- Add more **fields** to the User model

## Resources used :page_facing_up:
- [FastAPI docs](https://fastapi.tiangolo.com/)
- [Pydantic docs](https://docs.pydantic.dev/latest/)
- [PynamoDB docs](https://pynamodb.readthedocs.io/en/stable/)
- [uv docs](https://docs.astral.sh/uv/)
- [pytest docs](https://docs.pytest.org/en/stable/)