# A minimal Flask example about using this SDK

1. Make sure you have installed all dependencies under
`requirements.txt` by using

    ```bash
    pip install -r requirements.txt
    ```
   **It is recommended to use a Python virtualenv (venv) to manage
    your things under this project.**


2. Please go to `__init__.py` file to set up the global
variables for your own application.


3. Run the app  

    Commands to run Flask under Linux/Unix:
    
    ```bash
    $ export FLASK_APP=flask_example  
    $ export FLASK_ENV=development  
    $ flask run
    ```
    
    Commands to run Flask under Windows:
    
    ```bash
    > set FLASK_APP=flask_example  
    > set FLASK_ENV=development  
    > flask run
    ```
For other questions, please refer to
[Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/)