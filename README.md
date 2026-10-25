# blockchain-rpc-api-test

使用 Python + pytest + requests，对以太坊 Sepolia 测试网的公开 JSON-RPC 接口做自动化测试。

## 测试内容

- 正常用例：查询最新区块号、链 ID、最新区块哈希、合法地址余额
- 异常用例：调用不存在的方法、传入格式错误的地址（使用参数化，共 3 组数据）

共 8 条用例。

## 运行方法

    pip install pytest requests pytest-html
    pytest -v
    pytest --html=report.html --self-contained-html

## 说明

测试使用公开节点，可能受到限流或网络波动影响。
