# logger

Simple logger function with colored LogLevel for other scripts and designed to run inside Docker container 

Debug can be enabled by setting the environment variable 

*DEBUG_MODE = True*

## Usage example
```python
# Usage with os only necessary if environment variable has not been set before (e.g. outside Docker)
import os
os.environ['DEBUG_MODE'] = 'True'

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