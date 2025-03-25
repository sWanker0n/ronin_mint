import random
import time
from config import wallets, SLEEP
from ronin import Ronin

def main():
    for wallet in wallets:
        Ronin(wallet).mint()
        time.sleep(random.randint(SLEEP[0], SLEEP[1]))
    


if __name__ == '__main__':
    main()


