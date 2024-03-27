def log(msg): 
    with open(r'C:\Users\elton.duarte\Downloads\python-rpa\rpa-challange\logs/log.csv', 'a') as arquivo:
        arquivo.write(f"INFO; {msg}")
        arquivo.write('\n')
    