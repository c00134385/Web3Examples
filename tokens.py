import requests

# ���Etherscan API��Կ
ETHERSCAN_API_KEY = 'ENFN8359TIRMPPGKRX3F4U6AB3PVCTBYMD'

# Ҫ��ѯ���˻���ַ
account_address = '0x07D71D4378dc004e59BD2Fd481898A3De676Fbb8'

# ��������URL
url = f"https://api.polygonscan.com/api?module=stats&action=tokensupply&contractaddress=0x7ceb23fd6bc0add59e62ac25578270cff1b9f619&apikey={ETHERSCAN_API_KEY}"

print(f'url: {url}')
# ��������
response = requests.get(url)
data = response.json()
print(f'data: {data}')

# # ��������Ƿ�ɹ�
# if data['status'] == '1':
#     transactions = data['result']
#     for tx in transactions:
#         print(f"Hash: {tx['hash']}, From: {tx['from']}, To: {tx['to']}, Value: {tx['value']} Wei, TimeStamp: {tx['timeStamp']}")
# else:
#     print("Error fetching transaction history or no transactions found.")
