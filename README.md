## Setup via docker-compose

1. Clone the repository:
    ```sh
    $ git@github.com:Vlad0n20/MD-Digital-test-task.git
    ```
2. Populate env.example and end.db.example files and rename it on .env  and .env.db
3. Build and run containers with command:
    ```sh
    $ make build_containers
    ```
4. Populate the database with command if you want to generate new data:
    ```sh
    $ make populate_db_in_container
    ```
   if you want to use existing data:
    ```sh
    $ make load_data_in_container
    ```
5. Create superuser with command if you use docker-compose:
    ```sh
    $ make create_admin_in_container
    ```
## Setup locally
1. Clone the repository:
    ```sh
    $ git@github.com:Vlad0n20/MD-Digital-test-task.git
    ```
2. Populate env.example and end.db.example files and rename it on .env  and .env.db
3. If you don't have installed poetry, you can find how to do it here https://python-poetry.org/docs/
4. Install dependencies with command:
    ```sh
    $ poetry install
    ```
5. Activate virtual environment with command:
    ```sh
    $ poetry shell
    ```
6. Run project with command:
    ```sh
    $ /bin/bash start
    ```
7. Populate the database with command if you want to generate new data:
    ```sh
    $ python manage.py populate_db
    ```
    if you want to use existing data:
     ```sh
        $ python manage.py loaddata fixtures/user.json
        $ python manage.py loaddata fixtures/group.json
     ```
8. Create superuser with command:
    ```sh
    $ python manage.py createsuperuser
    ```

Now you can use the application. 

By http://0.0.0.0:8000/swagger/ - there is a swagger documentation for app.
