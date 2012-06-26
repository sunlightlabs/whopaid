import logging
import logging.handlers
import os.path

def set_up_logger(importer_name, log_path):
    # create logger
    log = logging.getLogger(importer_name)
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
    
    # create console handler and set level to debug
    ch = logging.FileHandler(os.path.join(log_path, importer_name + '.log'))
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    log.addHandler(ch)

    # create email handler and set level to warn
#    if LOGGING_EMAIL:
#        eh = logging.handlers.SMTPHandler(
#            (LOGGING_EMAIL['host'], LOGGING_EMAIL['port']), # host
#            LOGGING_EMAIL['username'], # from address
#            email_recipients,
#            email_subject,
#            (LOGGING_EMAIL['username'], LOGGING_EMAIL['password']) # credentials tuple
#        )
#        eh.setLevel(logging.WARN)
#        eh.setFormatter(formatter)
#        log.addHandler(eh)
#
    return log
#
