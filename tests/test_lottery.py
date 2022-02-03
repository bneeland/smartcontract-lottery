from brownie import Lottery, accounts, config, network
from web3 import Web3

def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    # assert lottery.getEntranceFee() > Web3.toWei(0.017, "ether") # 50 USD / 2721.41 ETH = 0.0184
    # assert lottery.getEntranceFee() < Web3.toWei(0.021, "ether") # 50 USD / 2721.41 ETH = 0.0184
