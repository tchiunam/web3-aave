from brownie import config, interface, network

from scripts.utility.helper import get_account


def get_weth():
    account = get_account()
    weth = interface.IWeth(
        config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    tx.wait(1)
    print("Received 0.1 WETH")


def main():
    get_weth()
