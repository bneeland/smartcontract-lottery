from brownie import Lottery, accounts, config, network
from scripts.deploy_lottery import deploy_lottery
from web3 import Web3

def test_get_entrance_fee():
    # Arrange
    lottery = deploy_lottery()
    # Act
    # 2,000 ETH / USD
    # USD entry fee = 50 USD
    # => 2,000 = 50 / x => x = 0.025
    expected_entrance_fee = Web3.toWei(0.025, "ether")
    entrance_fee = lottery.getEntranceFee()
    # Assert
    assert expected_entrance_fee == entrance_fee
