# Tiktokenizer

[在线直达 → tiktokenizer.vercel.app](https://tiktokenizer.vercel.app/)

## 简介

Tiktokenizer 是一个运行在浏览器里的 Token 可视化工具，底层基于 OpenAI 的 [tiktoken](https://github.com/openai/tiktoken) 库构建。输入任意一段文字，它会实时高亮显示文本被切分成了哪些 Token，以及总共消耗了多少个。

## 能做什么

- **Token 计数**：精确告诉你这段文字会占用多少 Token
- **分词可视化**：用不同颜色高亮每一个 Token，直观看到 LLM"眼里"的文本长度
- **API 费用估算**：根据 Token 数量自动计算各模型的调用成本
- **多模型支持**：覆盖 GPT-4o、Claude、Llama、DeepSeek、Qwen 等 60+ 主流模型

## 为什么有用

写 Prompt 时，一个常见困惑是：**"这段文字到底占了多少上下文窗口？"** Tiktokenizer 让你不用跑任何代码就能立刻得到答案。

典型使用场景：

- 精简 System Prompt，把 Token 砍到预算以内
- 对比不同模型的分词策略，理解为什么同一句话在不同模型里长度不一样
- 快速估算一批文档喂给 LLM 的总成本
- 直观理解中文、代码、特殊符号的 Token 效率（剧透：中文比英文贵）
