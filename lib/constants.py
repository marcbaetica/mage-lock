from pathlib import Path


CREDS_DB_FILE = 'mock_db.json'
CREDS_DB_PATH = Path(Path(__file__).parent.parent, CREDS_DB_FILE)
CREDS_SEEDS_FILE = 'data_start.csv'
CREDS_SEEDS_FILE_PATH = Path(Path(__file__).parent.parent, 'seeds', CREDS_SEEDS_FILE)

