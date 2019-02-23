Downloads historical candles from [oanda.com](https://www.oanda.com/) in a nice csv file.

Usage:
- Install necessary modules:
```
pip3 install -r requirements.txt
```
- Make changes in `config.py`.
- Run without parameters (it will look for a config in a current directory) or with a single parameter - path to a config file:
```
./downloader

or

./downloader -c /path/to/config.py
