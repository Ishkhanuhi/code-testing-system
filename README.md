# Code Testing System

## [Table of Contents](#table-of-contents)

- [Code Testing System](#movie-labeling)
    - [Table of Contents](#table-of-contents)
    - [Installation](#installation)
    - [Database](#database)
    - [Scripts documentation](#scripts-documentation)

## Installation

- Run `conda env update -f environment.yaml` from the command line in the root directory to install all required
  dependencies.
- Create `.env` file in the root directory.  
  **Note:** See `.env.example` file for details.

## Database

- Create a database named `code-testing-system`(or whatever you want, update in `.env`) in PostgreSQL.
- Run `flask db migrate -m "Some message here""` to generate a new migration.
- Run `flask db upgrade` to apply migration changes to the database.
- Run `flask db downgrade` to perform undo operation on the previous upgrade.

## Scripts documentation

- ### **Web Application Script**

  Starts web application whose purpose is to provide UI for code uploading and executing process.  
  _**Running command**_:

  ```bash
  python start.py --config-name=start_web_app port=some_port host=some_host
  ```

    - Routes
        - Sign in ([URL](http://127.0.0.1:{port}/))
        - Sign up ([URL](http://127.0.0.1:{port}/sign-up/))
        - Dashboard([URL](http://127.0.0.1:{port}/dashboard/))

  _**Command Example**_:

  ```bash
  python start.py --config-name=start_web_app port=5000 host=0.0.0.0
  ```


