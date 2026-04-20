# LaTeX安装与使用教程

$\LaTeX$是一款常用于科研与教育的文本语言，因为它支持强大且严格的文本格式以及数学、科学公式编写。我们研究室使用的ppt（日本叫slide）模版也是由LaTeX的beam模版改写而来。

相比所见即所得的word，LaTeX是所想即所得的，因此使用起来相比word会稍难一点。下面的教程会先教你如何打开和编译tex文件，然后简要地讲解最核心的latex语句教程。更详细的教程，以现在AI的实力，相信能解决你遇到的其它大部分问题，你永远可以相信AI（而且作为一个深度学习实验室，学会如何用AI是基本功了！）

## 什么是TeX？TeX历史简单介绍

在撰写学术论文时，我们常常需要面对复杂的排版和海量的数学公式。为了优雅地解决这个问题，**TeX** 应运而生。

**TeX的发明与演变**

TeX 是由著名计算机科学家、图灵奖得主高德纳（Donald Knuth）在20世纪70年代末发明的排版系统。

![Donald_Ervin_Knuth_(cropped)](./latex.assets/Donald_Ervin_Knuth_(cropped).jpg){ style="zoom:25%;" }

当时，高德纳在校对他的巨著《计算机程序设计艺术》（*The Art of Computer Programming*)时，对出版社糟糕的排版质量感到极为失望，尤其是数学公式的排版。于是，他决定自己动手，开发一套能够生成高质量印刷品的排版语言，这就是 TeX。

然而，原生的 TeX 语法非常底层且复杂，普通用户学习成本极高。到了20世纪80年代，计算机科学家莱斯利·兰伯特（Leslie Lamport）在 TeX 的基础上开发了一套宏包集合，这就是我们现在熟知的 **LaTeX**。LaTeX 极大地简化了 TeX 的使用，让作者可以将主要精力集中在文章的**内容**上，而不是排版的**细节**上。

**LaTeX 的核心功能与优势**

今天，LaTeX 已经成为理工科领域的学术排版标准。它支持极其强大的功能：

- **无与伦比的数学公式排版**：无论是简单的微积分还是复杂的矩阵，LaTeX 都能渲染得非常漂亮。
- **自动化管理**：自动生成目录、交叉引用以及参考文献。
- **分离内容与格式**：通过更换模板（Class），你可以一键将文章从"会议格式"切换为"期刊格式"，无需重新调整字体和段落。



## 使用Overleaf进行编译

对于刚接触 LaTeX 的新人来说，配置本地环境可能会遇到各种报错。**Overleaf** 是一个在线的、基于云端的 LaTeX 编辑器，它能让你像使用 Google Docs 或腾讯文档一样，打开浏览器就能写论文。

**1. 注册与登录**

访问 Overleaf 官网，你可以使用邮箱或关联相关学术账号直接注册登录。无需安装任何软件。

![image-20260411114845613](./latex.assets/image-20260411114845613.png){ style="zoom:50%;" }

**2. 创建你的第一个项目**

登录后，点击左上角的"New Project"（新建项目）。你可以选择创建一个"Blank Project"（空白项目），也可以直接从海量的"Templates"（模板）中寻找适合的学术期刊或会议模板。由于研究室已经有对应模板，因此我们选择上传文档。

![image-20260411104728186](./latex.assets/image-20260411104728186.png){ style="zoom:33%;" }

**3. 认识操作界面**

打开项目后，你会看到一个经典的三栏/两栏布局：

- **左侧文件树**：用于管理你的 `.tex` 源码文件、插入的图片文件以及参考文献的 `.bib` 文件。
- **中间编辑区**：这里是你编写 LaTeX 代码的地方。
- **右侧预览区**：这里显示编译后生成的 PDF 文件。
- ![image-20260411104908368](./latex.assets/image-20260411104908368.png){ style="zoom:50%;" }



**修改 Overleaf 编译器设置：**

- 点击 Overleaf 编辑界面左上角的 **Menu**（菜单）。
- 找到 **Settings** -> **Compiler**（编译器）。
- 将默认的 `pdfLaTeX` 改为 **`LaTeX`**。
- *注意：千万不要选 XeLaTeX 或 LuaLaTeX，就选最基础的 `LaTeX`，这样 Overleaf 就会乖乖去读取你的 `latexmkrc` 配置文件，并使用 `pLaTeX` 和 `dvipdfmx` 来生成 PDF 了。*



**4. 编译与下载**

在你修改了代码后，只需按下快捷键 `Ctrl + S`（或 `Cmd + S`），或者点击预览区上方绿色的"Recompile"按钮，Overleaf 就会自动编译并更新右侧的 PDF。完成写作后，点击右上角的下载按钮即可获取最终的 PDF 文件。



## 研究室模板的结构与编辑

研究室原版模板由教授在2020年左右从beam学术模版改造而来，以下称为第一版，这款主题奠定了研究室seminar的学术报告风格。按照教授的要求，所有研究室内使用的slide都要用它来编译。

然而这款模板有许多小问题，引擎太老、只支持日文，所以2024年左右研究室的学长们给它加上描述文件和其它部件，保证它在大多数编译环境内都能成功编译，并且支持全文件英文内容，这是第二版。

目前新生使用的是第三版，第三版由本人于2025年初，根据计算机专业的标准论文格式重构而来，改写了main.tex的结构，将各章节拆分到doc文件夹中，大幅简化了代码与逻辑，并基本消除了由语言差异带来的报错，正式支持中日英韩与常用科学符号。删掉了已经过时或无用的文件，简化包体。尽管原本想重写整个项目🤔，但是太屎山代码了，哪怕后来有AI也很难搞，所以目前暂时先只能这样了。



下面介绍文件主要结构。main.tex是整个文档的入口，在此可以编辑标题页和各章节的标题。而main的最下方

```latex
\section{References}
%\input{docs/references}

%\section{Appendix and Tips}
%\input{docs/tips}
```

均未启用。这是因为某些引擎对文献支持有差异，可能会有报错，所以干脆先注释掉，如果想要启用把前面百分号去掉就行。另一个原因是Overleaf于2025年底更新了使用政策，导致免费编译时间从15秒下降到12秒，恰好导致文档不够时间编译完，所以只好把最后一页也注释掉以保证各平台兼容性了。如果不是在免费版Overleaf使用，大家可以随时开启下面的两页。

另外该模板有一些黄色警告和少量报错是正常的，不用管它，这是因为日文渲染引擎的屎山代码造成的，只要不是严重报错都可以不用管它。

doc文件夹存放的是各章节实际内容，image文件夹存放的是slide用到的图片。平时书写latex最好按照一定的规范进行操作，这样能大幅减少工作流的错误。



## 使用VS Code进行本地LaTeX编译

虽然 Overleaf 很方便，但当你的论文项目变得庞大，或者网络环境不稳定时，**本地编译**是更专业、更高效的选择。Visual Studio Code (VS Code) 是目前最流行的代码编辑器，通过配置，它可以成为一个完美的 LaTeX 写作环境。

要实现本地编译，我们需要两样东西：**编译器（引擎）\**和\**编辑器（VS Code）**。

### Windows 系统配置教程

1. **安装编译器 (TeX Live)**：
   - 前往清华大学开源软件镜像站或其他镜像，下载 TeX Live 的 `.iso` 镜像文件。
   - 右键装载镜像，右键以管理员身份运行 `install-tl-windows.bat`。
   - 按照默认设置一路安装（过程可能需要几十分钟到一小时，请耐心等待）。
2. **安装并配置 VS Code**：
   - 下载并安装 VS Code。
   - 在 VS Code 左侧的扩展（Extensions）商店中，搜索并安装名为 **LaTeX Workshop** 的插件。如果是初次使用Vscode，建议再搜索一个chinese文本包，这样Vscode就是中文的了。
   - 安装完成后，VS Code 就能自动识别 `.tex` 文件，并调用底层的 TeX Live 进行编译了。

### macOS 系统配置教程

1. **安装编译器 (MacTeX)**：
   - 前往 MacTeX 官网，下载完整版的 `MacTeX.pkg` 安装包。
   - 双击安装包，按照提示完成安装（体积较大，推荐在网络良好的环境下下载）。
2. **安装并配置 VS Code**：
   - 下载并安装针对 macOS 的 VS Code。
   - 同样地，在扩展商店中搜索并安装 **LaTeX Workshop** 插件。
   - （进阶）如果遇到编译中文的问题，可以在 VS Code 的 `settings.json` 中将默认的编译链配置为 `xelatex`。



Overleaf 最省心的一点是它会自动检测需要编译几次、是否需要编译参考文献。在本地，我们可以通过配置 `latexmk` 工具来实现完全一样的效果。

在 VS Code 中按下 `Ctrl + Shift + P`（Mac 为 `Cmd + Shift + P`），输入 `Open Settings (JSON)`，打开 `settings.json` 文件，将以下配置合并到你的 JSON 文件中，如果你之前没有太多自定义设置（或者原来的设置不重要），最不容易出错的方法是**全选覆盖**。

请把 `settings.json` 里面的内容**全部清空（Ctrl+A全选，然后删除）**，然后把下面这一整段（包含最外层的大括号）完完整整地粘贴进去：：

```json
{
    "latex-workshop.latex.tools": [
        {
            "name": "latexmk (xelatex)",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdfxe",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "latexmk (pdflatex)",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "XeLaTeX (推荐, 完美支持中文)",
            "tools": [
                "latexmk (xelatex)"
            ]
        },
        {
            "name": "pdfLaTeX (英文论文常用)",
            "tools": [
                "latexmk (pdflatex)"
            ]
        }
    ],
    "latex-workshop.latex.autoBuild.run": "onFileChange",
    "latex-workshop.view.pdf.viewer": "tab"
}
```

1. 粘贴完之后，按下 **`Ctrl + S`** 确保 `settings.json` 文件已保存（文件标签页上的白色小圆点消失）。
2. 为了保险起见，**把 VS Code 关掉，重新打开**。
3. 再次回到你的 `test.tex` 文件中，随便敲个空格，按 `Ctrl + S` 触发编译。

只要这份配置被成功读取，插件左下角就会显示默认的 `Recipe: XeLaTeX`，而且就能正常编译出 PDF 了！再试一次看看。



如果还是不行，那可能是因为这个模板太祖传了，基于你之前配置的 VS Code 环境（我们用的是 `XeLaTeX`），如果直接编译这份文件，**100% 会报错或者排版错乱**。以下是你必然会遇到的三个核心问题，按严重程度排序：

##### 1. 致命冲突：编译引擎与驱动不匹配 (`dvipdfmx` 冲突)

- **引发报错的代码：** `\documentclass[dvipdfmx,cjk,t,10pt]{beamer}`
- **为什么会报错：** * `[dvipdfmx]` 和 `[cjk]` 这两个选项，是专门为日本传统的 `pLaTeX` 或 `upLaTeX` 编译引擎准备的（流程是：代码 -> DVI 文件 -> PDF）。
  - 而你目前 VS Code 里配置并默认使用的是**现代的 `XeLaTeX` 引擎**（流程是：代码直接生成 PDF）。`XeLaTeX` 不认识也不需要 `dvipdfmx`。如果强行用 `XeLaTeX` 编译，轻则弹出大量 Warning 并导致图片和颜色无法显示，重则直接编译中断。

##### 2. 找不到自定义宏包文件 (File Not Found)

- **引发报错的代码：** * `\usepackage{kasailab_slide_def}`
  - `\usepackage{./kasailab_math}`
- **为什么会报错：** * 这里的 `.sty` 文件是你们实验室学长学姐自己写的自定义样式表。如果你的项目文件夹（`main.tex` 所在的目录）里没有 `kasailab_slide_def.sty` 和 `kasailab_math.sty` 这两个文件，编译器会直接报 `File not found` 错误并停止运行。

##### 3. 找不到章节源文件 (File Not Found)

- **引发报错的代码：** * `\input{docs/chap1}` 到 `\input{docs/tips}`
- **为什么会报错：**
  - `\input` 命令会去读取外部文件。你需要确保你的根目录下有一个名为 `docs` 的文件夹，并且里面确确实实有 `chap1.tex`, `chap2.tex` 等文件。如果缺少任何一个，都会报错。

### 改 VS Code 配置以适配该文件

我们之前在 VS Code 里配置的是强制使用 `XeLaTeX`（参数里带有 `-pdfxe`），这会和实验室的配置"打架"。

请再次打开你的 `settings.json`（`Ctrl + Shift + P` -> `Open User Settings (JSON)`），将里面的 `tools` 和 `recipes` 替换为以下内容：

```json
{
    // ... 前面的其他设置保持不变 ...

    "latex-workshop.latex.tools": [
        {
            "name": "强制使用 pLaTeX (实验室模板专用)",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdfdvi",             // 强制走 DVI 转 PDF 模式
                "-latex=platex",       // 强制锁定底层引擎为 platex
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "编译 Kasai Lab 模板",
            "tools": [
                "强制使用 pLaTeX (实验室模板专用)"
            ]
        }
    ],
    "latex-workshop.latex.autoBuild.run": "onFileChange",
    "latex-workshop.view.pdf.viewer": "tab"
}
```

### 接下来怎么做：

1. 检查并删掉魔法注释（如果有的话）。
2. 保存更新后的 `settings.json`。
3. 回到 `main.tex`，为了防止残留的错误文件干扰，按下 `Ctrl + Shift + P` (Mac 是 `Cmd + Shift + P`)，输入 **`LaTeX Workshop: Clean up auxiliary files`** 清理一下。
4. 再次按 `Ctrl + S` 保存编译。
