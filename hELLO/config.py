import os

with open('.env') as f:
    for line in f:
        if line.strip() and not line.startswith('#'):
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

SDK = os.environ['SDK']
URL_DB = os.environ['URL_DB']