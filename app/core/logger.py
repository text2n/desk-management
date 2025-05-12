import logging

logging.getLogger('watchfiles.main').setLevel(logging.ERROR)
logging.basicConfig(filename='storage/app.log',level=logging.INFO , format='%(asctime)s %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)