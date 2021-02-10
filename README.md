# Requirements
1. IVAO account
2. Python3 (Available [here](https://python.org))
    - If you're on Linux/Mac, ensure you have python3-pip.
4. BeautifulSoup and selenium (`pip3 install bs4 selenium --user`)

# How to use
1. Copy the `config.example.json` file to a file named `config.json`
2. Edit the fields with relevent info (change region to two letter code, ex. `"region": "xa"`). For now please make sure it is lowercase
3. Edit `webdriver.Firefox(firefox_binary=...)` to use Chrome/Firefox, whichever browser you have, and change the `firefox_binary` to the path to your browser executable. 
    - If you don't know that path, replace that line with `webdriver.Firefox()` or `webdriver.Chrome()` and pray it works. 
    - Note, you will need geckodriver/chromedriver in your PATH. This will require some googling if you are not familiar with the process. 
4. Run `python3 main.py` and let it finish
5. Run `python3 clean.py` to format the data. Change up that file if you know Python and want to format differently
6. Run `python3 search.py` to perform the example search. Change it up to search for different stuff

All the data is now in `cleaned_data.json` if you want to do anything else with it. 


# I AM NOT RESPONSIBLE FOR WHAT YOU DO WITH ANYTHING IN THIS REPO. USE AT YOUR OWN RISK
