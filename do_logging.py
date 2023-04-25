import logging

logging.basicConfig(filename= "module.log", level= logging.DEBUG, format= "%(asctime)s %(levelname)s %(message)s")

def log(string,result):
    logging.info(string,result)

def log_error(string):
    logging.error(string)

def log_exception(string,result):
    logging.exception(string,result)

