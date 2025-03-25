import json

with open('data/wallets', 'r') as file:
    wallets = [row.strip() for row in file]

with open('data/abi/opensea_abi.json', 'r') as file:
    OPENSEA_ABI = json.load(file)

OPENSEA_CONTRACT = '0x00005ea00ac477b1030ce78506496e8c2de24bf5'

ERC_20_ABI = ''

Jin = '0xc2F09694fcc9C9dDcbe54a72b1a3b14658d2f755'
Ronke = '0x2fb6FEB663c481E9854a251002C772FEad3974d6'

stable = '0x0000a26b00c1F0DF003000390027140000fAa719'

RPC = 'https://ronin.drpc.org'
EXPLORER = "https://app.roninchain.com/tx"