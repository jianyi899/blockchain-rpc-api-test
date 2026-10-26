# blockchain-rpc-api-test

使用 Python + pytest + requests，对以太坊 Sepolia 测试网的公开 JSON-RPC 接口做自动化测试。

## 测试内容

- 正常用例（4 条）：查询最新区块号、链 ID、最新区块哈希、合法地址余额
- 异常用例（8 条）：
  - 调用不存在的方法
  - 传入格式错误的地址（参数化，3 组数据）
  - 地址边界值与非法字符（参数化，4 组数据：长度过短、长度过长、含非法字符、缺少 0x 前缀）

共 12 条用例。
## 运行方法

    pip install pytest requests pytest-html
    pytest -v
    pytest --html=report.html --self-contained-html

## 说明

测试使用公开节点，可能受到限流或网络波动影响。



测试报告可用 pytest-html 生成。