from scripts.helpful_scripts import get_account, get_contract, fund_with_link
from brownie import Lottery, network, config
import time

def deploy_lottery():
    account = get_account()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed lottery")
    return lottery

def start_lottery():
    account = get_account()
    lottery = Lottery[-1]
    starting_tx = lottery.startLottery({"from": account})
    starting_tx.wait(1)
    print("Started lottery")

def enter_lottery():
    account = get_account()
    lottery = Lottery[-1]
    value = lottery.getEntranceFee() + 100_000_000 # Tack on a little bit of Wei to make sure it's over the minimum amount
    tx = lottery.enter({"from": account, "value": value})
    tx.wait(1)
    print("Entered lottery")

def end_lottery():
    account = get_account()
    lottery = Lottery[-1]
    # Fund the contract, then end the lottery
    tx = fund_with_link(lottery.address)
    tx.wait(1)
    ending_transaction = lottery.endLottery({"from": account})
    ending_transaction.wait(1)
    print("Waiting (sleep)...")
    time.sleep(300)
    print(f"{lottery.recentWinner()} is the new winner.")

def main():
    deploy_lottery()
    start_lottery()
    enter_lottery()
    end_lottery()
