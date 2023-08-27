import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# from sys import stdout

# # Define logger
# logger = logging.getLogger('mylogger')

# logger.setLevel(logging.DEBUG) # set logger level
# logFormatter = logging.Formatter\
# ("%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S")
# consoleHandler = logging.StreamHandler(stdout) #set streamhandler to stdout
# consoleHandler.setFormatter(logFormatter)
# logger.addHandler(consoleHandler)