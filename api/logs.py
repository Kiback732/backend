import logging

class Logger:

    config = {
        'level': 'DEBUG',
        'stdout': True
    }

    def __init__(self, name='logger', config=config):
        self.logger = logging.getLogger(name)

        level = logging.getLevelName(config.get('level', 'DEBUG'))
        self.logger.setLevel(level)

        default_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s   %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
        sh = logging.StreamHandler()
        sh.setFormatter(default_formatter)

        if 'handlers' in config:
            handlers = config['handlers']
            if handlers.get('stdout', True):
                self.logger.addHandler(sh)
            if handlers.get('file', False):
                fh = logging.FileHandler(handlers['file'], 'a')
                fh.setFormatter(default_formatter)
                self.logger.addHandler(fh)
        else:
            self.logger.addHandler(sh)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

if __name__ == '__main__':
    log = Logger()
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
