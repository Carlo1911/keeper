# Technical Test

## Beginning 🚀
_This instructions let you deploy the project on your machine._

### Requirements 📋

-   Docker 19.03^
-   Docker Compose 1.25^
***

## Installation 🔧

1. Clone the repository
    ```
    git clone ...
    ```

2. Create a copy of .env.example in .env and modify it
    ```
    cp .env.example .env
    ```

3. Build the docker image
    ```
    make build
    ```
4. Run the docker image
    ```
    make up
    ```
5. Apply migrations
    ```
    make migrate
    ```
6. Create a superuser
    ```
    make superuser
    ```
***

## Testing 🔬
To run the tests you need to run the following command:
```
make test
```
***

## Utils 💻
- API docs available in: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
***
⌨️ with ❤️ by Carlo1911

---