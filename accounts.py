import requests

# 你的Etherscan API密钥
ETHERSCAN_API_KEY = 'ENFN8359TIRMPPGKRX3F4U6AB3PVCTBYMD'
YourApiKeyToken = ETHERSCAN_API_KEY
# 要查询的账户地址
account_address = '0x07D71D4378dc004e59BD2Fd481898A3De676Fbb8'


def getMaticBalance(address):
    url = f"""https://api.polygonscan.com/api?module=account&action=balance&address={address}&apikey={YourApiKeyToken}"""
    print(f'url: {url}')
    # 发送请求
    response = requests.get(url)
    data = response.json()
    print(f'data: {data}')
    if data['status'] == '1':
        return data['result']
    else:
        pass

# # 构建请求URL
# url = f"https://api.polygonscan.com/api?module=stats&action=tokensupply&contractaddress=0x7ceb23fd6bc0add59e62ac25578270cff1b9f619&apikey={ETHERSCAN_API_KEY}"

# print(f'url: {url}')
# # 发送请求
# response = requests.get(url)
# data = response.json()
# print(f'data: {data}')

# # 检查请求是否成功
# if data['status'] == '1':
#     transactions = data['result']
#     for tx in transactions:
#         print(f"Hash: {tx['hash']}, From: {tx['from']}, To: {tx['to']}, Value: {tx['value']} Wei, TimeStamp: {tx['timeStamp']}")
# else:
#     print("Error fetching transaction history or no transactions found.")

def main():
    # 这里是你的代码
    print("Hello, world!")
    getMaticBalance('0x5A534988535cf27a70e74dFfe299D06486f185B7')

if __name__ == "__main__":
    main()
