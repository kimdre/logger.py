# logger

Simple logger function with colored Loglevel for other scripts

## Usage example
```python
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
[Fri, 06 Aug 2021 13:20:41] INFO [test.py.main:6] This is a Info Message
[Fri, 06 Aug 2021 13:20:41] WARNING [test.py.main:7] This is a Warning Message
[Fri, 06 Aug 2021 13:20:41] ERROR [test.py.main:8] This is a Error Message
[Fri, 06 Aug 2021 13:20:41] CRITICAL [test.py.main:9] This is a Critical Message
```