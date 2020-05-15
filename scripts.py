import Utilities.general_logs as logs

log = logs.setup_general_logger(__file__)


if __name__ == '__main__':
    log.debug('test')
    log.error('error message')