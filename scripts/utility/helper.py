from brownie import accounts, config, network

LOCAL_ENVIRONMENTS = [
    "development",
    "mainnet-fork"
]


def get_account(index: int = None, id: str = None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_ENVIRONMENTS:
        return accounts[0]
    elif network.show_active() == "ganache-local":
        return accounts.add(config["wallets"]["local-ui"][0]["private_key"])

    return accounts.add(config["wallets"]["metamask"][0]["private_key"])
