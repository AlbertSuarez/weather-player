# App module

## Requirements
Python 3.5+

## Recommendations
Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage
To run the server, please execute the following from the root directory:

**1**. Setup virtual environment
    ```
    python3 -m venv env
    source env/bin/activate
    ```

**2**. Install dependencies
    ```
    pip3 install -r requirements.txt
    ```

**3**. Run Startup server as python module
    ```
    python3 -m src
    ```

**4**. Open your browser to here:
    ```
    http://localhost:8081/
    ```
