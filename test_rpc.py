import requests
import pytest

URL = "https://ethereum-sepolia-rpc.publicnode.com"

def call(method, params=None):
    body = {"jsonrpc": "2.0", "method": method,
            "params": params or [], "id": 1}
    resp = requests.post(URL, json=body, timeout=10)
    assert resp.status_code == 200
    return resp.json()

def test_block_number():
    data = call("eth_blockNumber")
    assert int(data["result"], 16) > 0

def test_unknown_method():
    data = call("eth_notExist")
    assert "error" in data

@pytest.mark.parametrize("addr", ["abc", "0x123", ""])
def test_bad_address(addr):
    data = call("eth_getBalance", [addr, "latest"])
    assert "error" in data
    
def test_chain_id():
    # Sepolia 的链 ID 是 11155111，十六进制是 0xaa36a7
    data = call("eth_chainId")
    assert data["result"] == "0xaa36a7"

def test_latest_block_has_hash():
    # 第二个参数 False 表示不需要区块里的完整交易内容
    data = call("eth_getBlockByNumber", ["latest", False])
    block = data["result"]
    assert block["hash"].startswith("0x")
    assert len(block["hash"]) == 66

def test_balance_of_valid_address():
    zero = "0x0000000000000000000000000000000000000000"
    data = call("eth_getBalance", [zero, "latest"])
    assert data["result"].startswith("0x")

@pytest.mark.parametrize("addr", [
    "0x" + "0" * 39,   # 太短（39位）
    "0x" + "0" * 41,   # 太长（41位）
    "0x" + "g" * 40,   # 长度对，但含非法字符
    "0" * 40,          # 缺少 0x 前缀
])
def test_bad_address_cases(addr):
    data = call("eth_getBalance", [addr, "latest"])
    assert "error" in data
# import requests

# URL = "https://ethereum-sepolia-rpc.publicnode.com"

# def test_block_number():
#     # 要发给节点的请求：问它"最新区块号是多少"
#     body = {"jsonrpc": "2.0", "method": "eth_blockNumber",
#             "params": [], "id": 1}
#     # 发出去，等它回答（最多等 10 秒）
#     resp = requests.post(URL, json=body, timeout=10)
#     data = resp.json()
#     print(data)
#     # 检查：返回的区块号（十六进制）转成数字后应该大于 0
#     assert int(data["result"], 16) > 0

# def test_unknown_method():
#     # 故意问一个不存在的方法
#     body = {"jsonrpc": "2.0", "method": "eth_notExist",
#             "params": [], "id": 1}
#     data = requests.post(URL, json=body, timeout=10).json()
#     print(data)
#     assert "error" in data

# def test_bad_address():
#     # 故意传一个格式错误的地址
#     body = {"jsonrpc": "2.0", "method": "eth_getBalance",
#             "params": ["abc", "latest"], "id": 1}
#     data = requests.post(URL, json=body, timeout=10).json()
#     print(data)
#     assert "error" in data