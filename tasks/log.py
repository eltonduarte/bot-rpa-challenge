from datetime import datetime

def log_to_file(msg, file): 

    with open(file, 'a') as arquivo:
        arquivo.write(f"{datetime.now()} | INFO | {msg}")
        arquivo.write('\n')
    