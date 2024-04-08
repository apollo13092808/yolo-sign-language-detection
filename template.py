import logging
import os
from pathlib import Path

logging.basicConfig(format='[%(asctime)s]: %(message)s', level=logging.INFO)

project_name = 'signlang'

list_of_files = [
    'data/.gitkeep',
    f'{project_name}/__init__.py',
    f'{project_name}/components/__init__.py',
    f'{project_name}/components/data_ingestor.py',
    f'{project_name}/components/data_validator.py',
    f'{project_name}/components/model_trainer.py',
    f'{project_name}/components/model_pusher.py',
    f'{project_name}/configurations/__init__.py',
    f'{project_name}/configurations/s3_operations.py',
    f'{project_name}/constants/__init__.py',
    f'{project_name}/constants/constant.py',
    f'{project_name}/entities/__init__.py',
    f'{project_name}/entities/artifacts.py',
    f'{project_name}/entities/configs.py',
    f'{project_name}/exception/__init__.py',
    f'{project_name}/logger/__init__.py',
    f'{project_name}/pipline/__init__.py',
    f'{project_name}/pipline/training.py',
    f'{project_name}/utils/__init__.py',
    f'{project_name}/utils/extras.py',
    'templates/index.html',
    '.dockerignore',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file \'{filename}\'')

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file \'{filename}\'')
    else:
        logging.info(f'{filename} already exists')
