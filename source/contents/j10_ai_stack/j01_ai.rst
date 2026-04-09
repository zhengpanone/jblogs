Spring AI / Spring AI Alibaba / LangChain4j 对比
=====================================================

.. list-table::
   :header-rows: 1
   :widths: 20 25 25 30

   * - 对比项
     - Spring AI
     - Spring AI Alibaba
     - LangChain4j
   * - 维护方
     - Spring 官方
     - 阿里云
     - 社区（LangChain4j）
   * - 设计理念
     - Spring 统一抽象
     - Spring AI + 企业增强
     - 类 LangChain 编排
   * - 学习成本
     - 低（Spring 风格）
     - 低（增强版）
     - 中（新 DSL）
   * - 模型支持
     - OpenAI / Azure / HuggingFace
     - 通义千问 / 百炼 / OpenAI
     - OpenAI / Ollama / 本地模型
   * - 本地模型支持
     - 一般（需适配）
     - 一般
     - 强（原生支持 Ollama）
   * - Agent 支持
     - 弱（基础能力）
     - 中（增强工具调用）
     - 强（完整 Agent）
   * - RAG 支持
     - 有（基础 VectorStore）
     - 强（企业级增强）
     - 强（成熟链式调用）
   * - Tool Calling
     - 支持
     - 强化支持
     - 强（函数式调用）
   * - 编排能力
     - 弱（偏简单调用）
     - 中
     - 强（Chain/Agent）
   * - Spring 集成
     - 深度集成
     - 深度集成
     - 一般（非原生 Spring）
   * - 适合场景
     - Spring 项目快速接入 AI
     - 国内企业级 AI 平台
     - AI Agent / 复杂工作流