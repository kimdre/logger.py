# logger.py

[![Build Status](https://drone.pyas.de/api/badges/Kim/logger.py/status.svg)](https://drone.pyas.de/Kim/logger.py)

Simple logger function with colored LogLevel designed to run inside Docker container 

## Possible values
Values can be set case insensitive (DEBUG, debug, Debug).
- debug
- info (default value)
- warn
- warning
- crit
- critical

## Requirements 
- Python 3.10 or higher

## Usage example

> Use the environment variable `LOG_LEVEL` to set the log level.
> 
> **LOG_LEVEL** = *debug*

```python
# Setting LOG_LEVEL with `os.environ` is only necessary if environment variable has not been set before (e.g. outside Docker)
import os
os.environ['LOG_LEVEL'] = 'DEBUG'

from loghandler import logger

def main():
    logger.debug("This is a Debug Message")
    logger.info("This is a Info Message")
    logger.warning("This is a Warning Message")
    logger.error("This is a Error Message")
    logger.critical("This is a Critical Message")

main()
```

```
[Fri, 06 Aug 2021 13:36:09] DEBUG [test.py.main:7] This is a Debug Message
[Fri, 06 Aug 2021 13:36:09] INFO [test.py.main:8] This is a Info Message
[Fri, 06 Aug 2021 13:36:09] WARNING [test.py.main:9] This is a Warning Message
[Fri, 06 Aug 2021 13:36:09] ERROR [test.py.main:10] This is a Error Message
[Fri, 06 Aug 2021 13:36:09] CRITICAL [test.py.main:11] This is a Critical Message
```

## Credits
Repo Icon made by [Smartline](https://www.flaticon.com/authors/smartline "Smartline") from [www.flaticon.com](https://www.flaticon.com/ "Flaticon")