#Logging in Python

import logging
logging.basicConfig(filename="log.txt",level=logging.WARNING)
logging.debug("some debug message")
logging.info("some information")
logging.warning("some warning")
logging.error("some Error")
logging.critical("some critical message")
