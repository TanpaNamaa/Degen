import sys
from web3 import Web3
import time

def mintNFT(pkey, to, hex_data, web3):
    account = web3.eth.account.from_key(pkey)
    origin = account.address
    nonce = web3.eth.get_transaction_count(origin)

    balance = web3.eth.get_balance(origin)
    gas_limit = 104336  # Adjusted gas limit
    gas_price = 151000000  # Adjusted gas price in Wei (0.01 Gwei)

    if balance > gas_limit * gas_price:
        # build a transaction in a dictionary
        tx = {
            'chainId': 666666666,  # Updated chain ID for Degen L3
            'nonce': nonce,
            'to': to,
            'value': 0,
            'data': hex_data,
            'gas': gas_limit,
            'gasPrice': gas_price
        }

        signed_tx = account.sign_transaction(tx)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f'Transaction sent: {web3.to_hex(tx_hash)}')
    else:
        print('Low DEGEN balance in wallet')

def main():
    if len(sys.argv) < 5:
        raise ValueError('Please provide arguments')

    pkey_list = sys.argv[1]
    to_addy = sys.argv[2]
    hex_data = sys.argv[3]
    rpc_url = sys.argv[4]

    web3 = Web3(Web3.HTTPProvider(rpc_url))

    with open(pkey_list, 'r') as pkeys:
        for _ in range(100):  # Ganti 5 dengan jumlah transaksi yang Anda inginkan
            pkeys.seek(0)  # Kembali ke awal file setiap iterasi
            for pkey in pkeys:
                pkey = pkey.strip()
                mintNFT(pkey, to_addy, hex_data, web3)
                time.sleep(1)  # Tunda 1 detik antara setiap transaksi

if __name__ == "__main__":
    main()