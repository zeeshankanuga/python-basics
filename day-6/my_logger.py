import logging
logging.basicConfig(filename='my_server_logs.log', datefmt= '%d-%m-%y %H:%M:%S', format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
logging = logging.getLogger()
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message") 