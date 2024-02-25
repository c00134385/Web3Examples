from web3 import Web3

# 使用 Infura 的 URL
infura_url = "https://polygon-mainnet.infura.io/v3/079b909eeafc461383987e1e56a6755a"
web3 = Web3(Web3.HTTPProvider(infura_url))

# 检查连接是否成功
print(web3.is_connected())

if(web3.is_connected()):
    latest_block = web3.eth.block_number
    print(latest_block)
else:
    print("Failed to connect to Ethereum network")
    exit(-1)

# 获取当前链ID
chain_id = web3.eth.chain_id

print(f'Current connected chain ID: {chain_id}')

# 根据链ID判断网络
if chain_id == 1:
    print("This is the Ethereum Mainnet.")
elif chain_id == 3:
    print("This is the Ropsten Testnet.")
elif chain_id == 4:
    print("This is the Rinkeby Testnet.")
elif chain_id == 5:
    print("This is the Goerli Testnet.")
elif chain_id == 42:
    print("This is the Kovan Testnet.")
else:
    print(f"This is an unknown or private network with chain ID: {chain_id}")


# ERC-20代币合约地址（这是一个示例地址，请替换为你想查询的代币合约地址）
token_contract_address = '0x2C89bbc92BD86F8075d1DEcc58C7F4E0107f286b'

# ERC-20代币合约的ABI（这只是`balanceOf`方法的部分ABI）
token_abi = '''
[
    {
        "constant":true,
        "inputs":[{"name":"_owner","type":"address"}],
        "name":"balanceOf",
        "outputs":[{"name":"balance","type":"uint256"}],
        "type":"function"
    }
]
'''

print(f'token_abi: {token_abi}')

# 创建代币合约对象
token_contract = web3.eth.contract(address=token_contract_address, abi=token_abi)

# 账户地址（替换为你想查询的账户地址）
account_address = '0x07D71D4378dc004e59BD2Fd481898A3De676Fbb8'

# 查询余额
balance = token_contract.functions.balanceOf(account_address).call()

# 将余额从Wei转换为更易读的单位（如果代币使用的不是18位小数，请相应调整）
readable_balance = balance / 10**18

print(f'Balance: {readable_balance} tokens')

# 设置账户地址和私钥
account = "0x07D71D4378dc004e59BD2Fd481898A3De676Fbb8"
private_key = "你的私钥"


# 查询余额
balance = web3.eth.get_balance(account_address)

# 将余额从wei转换为Matic（Polygon使用和以太坊相同的18位小数）
matic_balance = web3.from_wei(balance, 'ether')

print(f"Account balance: {matic_balance} Matic")



# 构建交易
# nonce = web3.eth.get_transaction_count(account)
# print(nonce)
# balance = web3.eth.get_balance(account=account)
# print(balance)

# tx = {
#     'nonce': nonce,
#     'to': contract_address,
#     'value': web3.toWei(0, 'ether'),
#     'gas': 2000000,
#     'gasPrice': web3.toWei('50', 'gwei'),
#     'data': contract.encodeABI(fn_name='yourFunction', args=['参数']),
# }