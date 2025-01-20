import os
import time
from web3 import Web3
from solcx import install_solc, set_solc_version, compile_source
from colorama import init, Fore, Style
import emoji
from dotenv import load_dotenv

load_dotenv()

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    print(Fore.YELLOW + "========================================")
    print(Fore.CYAN + emoji.emojize(":rocket:") + " AUTHOR : ANAM BACTIAR")
    print(Fore.MAGENTA + emoji.emojize(":star:") + " THANKS TO : ANAM BACTIAR!")
    print(Fore.BLUE + emoji.emojize(":globe_with_meridians:") + " GITHUB: https://github.com/bactiar291")
    print(Fore.GREEN + emoji.emojize(":coffee:") + " BUY COFFEE FOR ME: 0x648dce97a403468dfc02c793c2b441193fccf77b ")
    print(Fore.YELLOW + "========================================\n")

display_banner()

install_solc('0.8.0')
set_solc_version('0.8.0')

reddio_rpc_url = "https://reddio-dev.reddio.com"
chain_id = 50341
web3 = Web3(Web3.HTTPProvider(reddio_rpc_url))

account_address = os.getenv('ACCOUNT_ADDRESS')
private_key = os.getenv('PRIVATE_KEY')

contract_source_code = '''
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 storedData;

    constructor() {
        storedData = 100;
    }

    function set(uint256 x) public {
        storedData = x;
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
'''

def deploy_contract():
    try:
        compiled_sol = compile_source(contract_source_code)
        contract_interface = compiled_sol['<stdin>:SimpleStorage']
        abi = contract_interface['abi']
        bytecode = contract_interface['bin']

        SimpleStorage = web3.eth.contract(abi=abi, bytecode=bytecode)

        gas_estimate = SimpleStorage.constructor().estimate_gas()
        transaction = SimpleStorage.constructor().build_transaction({
            'from': account_address,
            'nonce': web3.eth.get_transaction_count(account_address),
            'gas': gas_estimate,
            'gasPrice': web3.eth.gas_price,
            'chainId': chain_id
        })

        signed_tx = web3.eth.account.sign_transaction(transaction, private_key)

        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        contract_address = tx_receipt.contractAddress

        print(Fore.GREEN + emoji.emojize(":check_mark_button:") + f' Kontrak berhasil di-deploy di alamat: {contract_address}')
    except Exception as e:
        print(Fore.RED + emoji.emojize(":cross_mark:") + f' Gagal deploy kontrak: {str(e)}')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    if web3.is_connected():
        print(Fore.BLUE + "Memulai proses deploy...")
        deploy_contract()
    else:
        print(Fore.RED + emoji.emojize(":cross_mark:") + " Tidak dapat terhubung ke node Reddio Testnet")
    for i in range(10, 0, -1):
        print(Fore.MAGENTA + f"Menunggu {i} detik untuk mencoba kembali...", end='\r')
        time.sleep(0.2)
    print("\n" + Fore.GREEN + "Memulai kembali proses...\n")
