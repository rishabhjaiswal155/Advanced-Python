#Problems with root logger
'''1. once we set the basic configuration then that configuration is final and we cannot change.
2.It will always works with only one handler either console handler or file handler,but not with both simultaneously.
3.It is not possible to configure logger with different configuration at different levels.
4. No way to specify multiple log files for multiple  modules/classes/function.'''

import logging
import Student
logging.basicConfig(filename='log1.txt',level=logging.CRITICAL)
logging.debug("some DEBUG message")
logging.info("some INFO message from RootLoggerProblem module")
logging.warning("some WARNING message")
logging.error("some ERROR message")
logging.critical("some CRITICAL message from RootLoggerProblem module")

 