# UC Berkeley CS61C: Great Ideas in Computer Architecture

## 课程简介

- 所属大学：UC Berkeley
- 先修要求：CS61A, CS61B
- 编程语言：C
- 课程难度：🌟🌟🌟🌟
- 预计学时：100 小时

伯克利 CS61 系列的最后一门课程，深入计算机的硬件细节，带领学生逐步理解 C 语言是如何一步步转化为 RISC-V 汇编并在 CPU 上执行的。和 [Nand2Tetris](https://csdiy.wiki/体系结构/N2T/) 不同，这门课 在难度和深度上都会提高很多，具体会涉及到流水线、Cache、虚存以及并发相关的内容。

这门课的 Project 也非常新颖有趣。Project1 会让你用 C 语言写一个小程序，20 年秋季学期是著名的游戏 *Game of Life*。Project2 会让你用 RISC-V 汇编编写一个神经网络，用来 识别 MNIST 手写数字，非常锻炼你对汇编代码的理解和运用。Project3 中你会用 Logisim 这个数字电路模拟软件搭建出一个二级流水线的 CPU，并在上面运行 RISC-V 汇编代码。Project4 会让你使用 OpenMP, SIMD 等方法并行优化矩阵运算，实现一个简易的 Numpy。

总而言之，这是个人上过的最好的计算机体系结构的课程。

## 课程资源

- 课程网站：[https://cs61c.org/sp26/](https://cs61c.org/sp26/)
- 课程视频：Bilibili 和 YouTube 上均有历年录像（推荐 Summer 2020 / Fall 2020 版本）
- 课程教材：无固定教材，配套讲义发布于课程网站
- 课程作业：四个 Project + 若干 Lab/HW，具体要求见课程网站



## 笔者注

学完 Nand2Tetris 之后的自然延伸。Nand2Tetris 砍掉了许多现代计算机特性来降低入门门槛，而 CS61C 补上了这一切，流水线、Cache、虚拟内存、分支预测、乱序执行、并发等这些现代计算机最关键的部分。两门课加在一起，基本就能建立起对一台真实计算机从门电路到操作系统接口的完整认知。

这门课难度相当高，因此最好学过有关RISCV架构的相关课程，另外，如果你没有伯克利的学生邮箱，那么历年课程你是进不去的，只能进最新一学期课程，而且课程结束后也会随之关闭。因此最好还是参考CSDIY中给出的资讯。
