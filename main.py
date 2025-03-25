from config import wallets
from ronin import Ronin

def main():
    for wallet in wallets:
        Ronin(wallet).mint()


if __name__ == '__main__':
    main()


