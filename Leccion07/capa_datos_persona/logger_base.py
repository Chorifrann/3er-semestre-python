import logging as log

# Lllamamos una configuracion basica
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('mensaje nivel debug')
    log.info('mensaje a nivel info')
    log.warning('mensaje a nivel warning')
    log.error('mensaje a nivel error')
    log.critical('Mensaje a nivel critical')
