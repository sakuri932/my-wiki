# Stanford CS336: 从头开始做一个 GPT

## 课程简介

- 所属大学：Stanford University
- 先修要求：熟练掌握 Python 和 PyTorch，具备深度学习基础知识（了解 Transformer 架构为佳）
- 编程语言：Python (with PyTorch)
- 课程难度：🌟🌟🌟🌟🌟
- 预计学时：100小时

CS336 是斯坦福大学开设的一门硬核语言模型课程，由 Percy Liang 和 Tatsunori Hashimoto 主讲。课程的核心理念只有一句话：**从零开始，亲手搭建一个大语言模型**。

不同于大多数课程停留在"调用 API"或"微调预训练模型"的层面，CS336 要求学生从最底层做起——自己实现 Transformer、自己处理训练数据、自己写 BPE 分词器、自己搞定分布式训练、自己研究 scaling law……一路走下来，你对 GPT 类模型的理解会从"知道它能干什么"升级到"知道它的每一行代码是怎么来的"。

课程涵盖的主要内容包括：

- **Transformer 架构**：从 attention 机制到完整的 decoder-only 模型，逐模块手工实现
- **数据处理**：Common Crawl 数据清洗、BPE 分词器实现、数据配比策略
- **训练基础设施**：混合精度训练、梯度检查点、Flash Attention、分布式训练（DDP/FSDP）
- **Scaling Laws**：Chinchilla 最优计算分配，如何在有限算力下做出最好的模型
- **对齐与安全**：RLHF、DPO 等后训练技术

五个大作业贯穿始终，每一个都要求写大量从零开始的代码，没有捷径。

## 课程资源

- 课程网站：[https://cs336.stanford.edu/](https://cs336.stanford.edu/)
- 课程视频：参见课程网站
- 课程教材：无固定教材，配套讲义和阅读材料均发布于课程网站
- 课程作业：五个作业，涵盖 Transformer 实现、数据处理、训练基础设施、模型对齐等，具体参见课程网站



## 笔者注

建议先把李宏毅机器学习2022or2023版学到至少VAE位置再开始这门课程。这门课几乎所有代码都要手搓，难度曲线比较大。
