


from web3 import Web3
from scripts.aave_pool_abi import ABI as AAVE_ABI
from erc20_abi import ABI as ERC20_ABI

# Fill in your infura API key here
web3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/837e5a22f48a42a1be56cafa6aaacc5f"))

address = "0x368EedF3f56ad10b9bC57eed4Dac65B26Bb667f6"
#address = "0x480B8b39d1465b8049fbf03b8E0a072Ab7C9A422"

contract = web3.eth.contract(address=address, abi=AAVE_ABI)

user_account_data = contract.functions.getUserAccountData("0x3f9E4A6120aB7868485602241AbE9D85d6F9E382").call()
#user_account_data = contract.functions.balanceOf("0x3f9E4A6120aB7868485602241AbE9D85d6F9E382").call()
# user_account_data = contract.functions.getReservesList().call()

print(user_account_data)

