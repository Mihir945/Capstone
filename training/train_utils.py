import os

DATA_DIR = 'Data'
DATA_FILE = 'car-details.csv'
DATA_FILE_PATH = os.path.join(DATA_DIR, DATA_FILE)

APP_DIR = 'app'
MODEL_DIR_NAME = 'model'
MODEL_NAME = 'model.joblib'
MODEL_DIR = os.path.join(APP_DIR, MODEL_DIR_NAME)
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)