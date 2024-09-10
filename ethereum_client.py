from web3 import Web3
import config

def create_web3_instance():
    web3 = Web3(Web3.HTTPProvider(config.ALCHEMY_URL))
    if not web3.is_connected():
        raise ConnectionError("Failed to connect to Ethereum network.")
    return web3
