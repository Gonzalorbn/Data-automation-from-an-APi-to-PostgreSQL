import logging as log

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('Python\Extraer_api_ML_SQL\capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')