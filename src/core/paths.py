from pathlib import Path

# Path to the root of the project
ROOT = Path(__file__).parent.parent.parent
SRC = ROOT / 'src'

# Path to the data directory
APP_DATA_DIR = ROOT / 'AppData'
LOG_DIR = APP_DATA_DIR / 'log'

# Path to the file
DATABASE_META_FILE = ROOT / 'database_meta.json'
DATABASE_FILE = ROOT / 'database.db'
LOG_FILE = LOG_DIR / 'log.log'
CONFIG_FILE = ROOT / 'settings.json'

# All directories in the project
ALL_DIRS: list[Path] = [APP_DATA_DIR, LOG_DIR]
