#Steps for Customized Logger
import logging
#step 1: creating a logger object and setting the level

logger=logging.getLogger('DemoLogger')
logger.setLevel(logging.DEBUG)

#step 2: creating handler object and setting the level

consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.WARNING)

fileHandler=logging.FileHandler('logFile.txt')
fileHandler.setLevel(logging.DEBUG)

#step 3: Creating formatter object
formatter1=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
formatter2=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')

#step 4: adding the formatter to handler
consoleHandler.setFormatter(formatter1)
fileHandler.setFormatter(formatter2)

#step 5: adding the handler to Logger
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

#step 6: writting the messages to Logger
logger.debug("some DEBUG message")
logger.info("some INFO message")
logger.warning("some WARNING message")
logger.error("some ERROR message")
logger.critical("some CRITICAL message")