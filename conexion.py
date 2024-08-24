import pymysql
import yaml

# Load database configuration from YAML file
def load_db_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config['mysql']

# Function to connect to the MySQL database
def get_db_connection():
    db_config = load_db_config()
    conn = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    return conn