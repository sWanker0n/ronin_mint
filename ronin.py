from account import Account
from loguru import logger as ll
import json
from config import OPENSEA_ABI, OPENSEA_CONTRACT, Ronke, Jin, stable

class Ronin(Account):
    def __init__(self, pk):
        super().__init__(pk=pk)

    def mint(self):
        try:
            if self.check_balance() / 10 ** 18 >= 0.01:
                tx_data = self.get_tx_data()
                transaction = self.get_contract(OPENSEA_CONTRACT, OPENSEA_ABI).functions.mintPublic(Ronke, stable, self.address, 1).build_transaction(tx_data)
                signed_txn = self.sign(transaction)
                txn_hash = f"0x{self.send_raw_transaction(signed_txn).hex()}"
                ll.success(f"[register_domain] | {self.address} | https://app.roninchain.com/tx{txn_hash}")
            else:
                ll.warning(f"{self.address} dont enough RONIN balance")
        except Exception as err:
            ll.error(err)
