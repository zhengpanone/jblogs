=============
Agent
=============

Agent 是智能体的抽象，它是智能体的核心，是智能体的接口。

Agent 通常有这几个部件：

1. LLM(大脑)：负责推理、生成行动指令
2. Tools(手脚)：HTTP请求、数据库、搜索、代码执行、链上RPC、发邮件
3. Memory(记忆)：存储历史信息、状态、上下文
4. Loop(循环)：处理输入、推理、生成、输出
5. Safety & Guardrails(护栏)：避免无限循环、越权调用、危险操作

最小可用版本（MVP）
======================

Minimum Viable Product，最小可行产品

- 输入一个目标：比如“查一下我项目的错误日志并总结原因，给出修复建议”
- Agent 自动拆解：需要查询日志 → 提取关键错误 → 归类 → 给建议
- 每次行动都是调用一个 tool，然后把结果喂回 LLM 继续下一步





参考文档
==============

- `用 Rust 开发一个可落地的 AI Agent`_

.. _`用 Rust 开发一个可落地的 AI Agent`: https://mp.weixin.qq.com/s/sDboXOlQ7rVhWnkmrtxRTQ



