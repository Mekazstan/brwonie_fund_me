from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

#Create forked account with forked eth for gas fee and not deploy MOCK
#See notes for creating mainnet forked accounts
FORKED_LOCAL_ENVIRONMENTS = ["mainnet_fork", "mainnet_fork_dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache_local']

DECIMALS = 8
STARTING_PRICE = 200000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mock():
    print(f"The active network is {network.show_active}")
    print("Deploying Mocks....")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
    print("Mock Deployed")