# Tweet-Automator
A Python script to automate the process of posting tweets

## How to run the script
 - Install dependencies
    ```angular2html
    pip install -r requirements.txt
    ```
 - Add a ```credentials.py``` in the following format
    ```
    ACCESS_TOKEN = "####"
    ACCESS_TOKEN_SECRET = "####"
    CONSUMER_KEY = "####"
    CONSUMER_SECRET = "####"
    ```
 - Adjust the ```NUM_OF_TWEETS``` and ```WAIT_TIME``` parameter in ```script.py```. Make sure to not have a very small ```WAIT_TIME```.
 - Run the script
    ```angular2html
    python script.py
    ```

## To do
 - Add a config.yaml file
