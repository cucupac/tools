


from web3 import Web3
from aave_pool_abi import ABI as AAVE_POOL_ABI
from aave_oracle_abi import ABI as AAVE_ORACLE_ABI
from erc20_abi import ABI as ERC20_ABI


# Fill in your infura API key here
web3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/837e5a22f48a42a1be56cafa6aaacc5f"))

#address = "0x5bed0810073cc9f0DacF73C648202249E87eF6cB" # Goerli Aave Oracle Address
#address = "0x368EedF3f56ad10b9bC57eed4Dac65B26Bb667f6" # Goerli Aave Pool Address
address = "0xA2025B15a1757311bfD68cb14eaeFCc237AF5b43" # Goerli USDC

contract = web3.eth.contract(address=address, abi=ERC20_ABI)

#result = contract.functions.getUserAccountData("0x3f9E4A6120aB7868485602241AbE9D85d6F9E382").call()
#result = contract.functions.getReserveData("0xA2025B15a1757311bfD68cb14eaeFCc237AF5b43").call() #wBTC
#result = contract.functions.getConfiguration("0xA2025B15a1757311bfD68cb14eaeFCc237AF5b43").call()  #USDC
#result = contract.functions.getConfiguration("0x2e3A2fb8473316A02b8A297B982498E661E1f6f5").call()  #wETH
#result = contract.functions.balanceOf("0x3f9E4A6120aB7868485602241AbE9D85d6F9E382").call()
#result = contract.functions.getReservesList().call()

#result = contract.functions.balanceOf("0x71059a9f54B00e1933dc6e02239a1471f58518dD").call()
result = contract.functions.allowance("0x71059a9f54B00e1933dc6e02239a1471f58518dD", "0x270D6F7620C30F300af545798061a251fae09319").call()

print(result)

