# 使用MkDocs部署github个人主页







### 准备工作

在开始之前，请确保你的电脑上已经安装了以下工具：

1. **Python** (建议 3.8 或更高版本)
2. **Git**
3. 拥有一个 **GitHub 账号**

### 第一步：安装 MkDocs 和 Material 主题

打开你的终端（命令行/PowerShell），运行以下命令来安装 MkDocs 和 Material 主题：

Bash

```
pip install mkdocs-material
```

=== "Windows"
    windows下统一使用pip + “对应的命令”

=== "macOS"
    macOS有所不同，需要改成pip3 -m + “对应的命令”，后面所有命令均需要做同样的改动



### 第二步：初始化项目

找一个你喜欢存放项目代码的文件夹，然后在终端中运行以下命令来创建一个新的 MkDocs 项目（假设我们命名为 `my-wiki`）：

Bash

```
mkdocs new my-wiki
cd my-wiki
```

此时，你的文件夹里会生成两个核心内容：

1. `mkdocs.yml`：这是你的网站全局配置文件。
2. `docs/` 文件夹：这里面存放你的网站内容，默认有一个 `index.md`。



### 第三步：配置 Material 主题

使用文本编辑器（如 VS Code、Notepad++ 等）打开 `mkdocs.yml` 文件，将里面的内容修改为以下配置，以启用 Material 主题：

YAML

```
site_name: 我的专属知识库  # 你可以改成任何你喜欢的名字
theme:
  name: material
```

### 第四步：本地预览效果

在终端中（确保当前路径在 `my-wiki` 文件夹下），运行以下命令启动本地服务器：

Bash

```
mkdocs serve
```

终端会提示一个本地地址（通常是 `http://127.0.0.1:8000`）。在浏览器中打开这个链接，你就能看到你的网站雏形了！按下 `Ctrl + C` 可以停止本地预览。

### 第五步：将代码提交到 GitHub

1. 登录 GitHub，点击右上角的 **"+"** 号，选择 **"New repository"** 创建一个新的仓库（例如命名为 `my-wiki`），**不要**勾选 "Add a README file"，直接创建。
2. 回到你的本地终端，依次运行以下命令，将本地代码关联并推送到 GitHub（请将下面命令中的链接替换为你刚刚创建的 GitHub 仓库链接）：

Bash

```
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/你的仓库名.git
git push -u origin main
```

### 第六步：配置 GitHub Actions 实现自动化部署（强烈推荐）

为了让你以后每次修改文章后，网站都能自动更新，我们可以配置自动化部署。

1. 在你的项目根目录下，依次创建文件夹 `.github`，然后在里面创建子文件夹 `workflows`。

   ===“macOS“

   在macOS中如果无法直接创建，在终端直接输入

   ```
   mkdir -p .github/workflows && touch .github/workflows/ci.yml
   ```

   如果你在使用 Visual Studio Code (VS Code) 或者其他代码编辑器来修改你的项目：

   1. 直接在 VS Code 里用 `打开文件夹` 的方式，把你的整个 `my-wiki` 文件夹加载进去。
   2. 在 VS Code 左侧的文件目录树里，点击新建文件夹的图标。
   3. 输入 `.github`，按下回车。在这里创建是完全没有任何阻碍的。
   4. 接着在 `.github` 里面新建 `workflows` 文件夹，再新建 `ci.yml` 即可

   

2. 在 `workflows` 文件夹中创建一个名为 `ci.yml` 的文件。

3. 将以下官方推荐的配置代码复制粘贴到 `ci.yml` 中：

YAML

```
name: ci
on:
  push:
    branches:
      - main
      - master
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configure Git Credentials
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
      - uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material 
      - run: mkdocs gh-deploy --force
```

1. 保存文件后，将这些新的改动推送到 GitHub：

   Bash

   ```
   git add .
   git commit -m "Add GitHub Actions for deployment"
   git push
   ```

### 第七步：开启 GitHub Pages 展示你的网站

1. 回到你的 GitHub 仓库页面。
2. 点击上方的 **Settings**（设置）选项卡。
3. 在左侧菜单栏找到 **Pages**。
4. 在 **Build and deployment** 下的 Source 下拉菜单中，选择 **Deploy from a branch**。
5. 在 Branch 下拉菜单中，选择 **`gh-pages`** 分支，文件夹保持默认的 `/ (root)`，然后点击 **Save**。

等待一两分钟（你可以在仓库的 **Actions** 选项卡中查看部署进度），完成后，在 Settings -> Pages 页面顶部会显示出你网站的最终公开链接（格式通常为 `https://你的用户名.github.io/你的仓库名/`）。

至此，你的网站就成功上线了！以后你只需要在本地 `docs/` 文件夹里修改或增加 Markdown 文件，然后执行 `git add .`、`git commit -m "更新内容"` 和 `git push`，GitHub 就会自动帮你把最新的内容发布到网站上。



如果报错refusing to allow a Personal Access Token to create or update workflow... without workflow scope怎么办？这个报错 是 GitHub 的一个**安全保护机制**。

**原因解释**： 因为你在第六步添加了一个 `.github/workflows/ci.yml` 文件。这属于 GitHub Actions 的自动化工作流文件，权限非常高（相当于允许服务器自动运行代码）。为了安全，GitHub 要求你推送这类文件时，使用的“访问令牌（Token）”必须明确拥有 `workflow`（工作流）的权限。而你当前电脑里缓存的旧 Token 没有这个权限，所以被拒绝了。

解决这个问题只需要两步：**获取一个带有 workflow 权限的新 Token，并在 Mac 上替换掉旧的。**具体请问Gemini怎么做。



既然代码已经传上去了，你可以去网页端看看成果了：

1. **查看自动构建进度**：

   - 打开你的浏览器，进入你刚才的 GitHub 仓库页面。
   - 点击仓库名称下方的 **Actions** 选项卡。
   - 你应该能看到一个正在运行的工作流（通常会有一个黄色的旋转小圆圈，名字可能是 "ci" 或者是你刚才填写的 commit 信息）。
   - 等待大约 1 到 2 分钟，当这个黄色小圆圈变成**绿色的对号 (✅)** 时，说明 GitHub 已经按照你的 `ci.yml` 指令，帮你把网站静态文件打包并发布好了！

2. **获取你的网站链接**：

   - 在你的仓库页面，点击右上方的 **Settings**（设置）。

   - 在左侧菜单栏往下滑，找到并点击 **Pages**。

   - 此时，页面的最上方应该会出现类似这样的一句话：

     > **Your site is live at `https://用户名.github.io/my-wiki/`**

   - （*注意：如果这里还没显示链接，或者只显示了 Source 配置，请确保 Source 下拉菜单选择的是 **Deploy from a branch**，并且 Branch 选择的是 `gh-pages` 和 `/ (root)`，然后点击 Save。*）

点击那个链接，你就能看到基于 Material for MkDocs 主题的专属知识库正式上线了！

以后你要写新文章或者修改内容，只需要在本地的 `docs/` 文件夹里修改 Markdown 文件，然后依次执行 `git add .` -> `git commit -m "更新"` -> `git push`，剩下的事情 GitHub 都会在后台自动帮你搞定，再也不用管什么 Token 权限啦。享受你的建站之旅吧！



在doc文件夹下创建md文件，输入

```
---
date: 2026-04-10
categories:
  - 随笔
---

# 这是我的第一篇博客！

你好，世界！我已经成功在本地跑起了 Material for MkDocs！
```

效果如下：

![image-20260410230441808](./如何撰写blog.assets/image-20260410230441808.png)



如果你的页面没有发生变化，页面没有变化的原因是：**Material for MkDocs 的博客插件对文章存放的路径有严格的“默认规矩”。** 当你只在 `mkdocs.yml` 里写了 `- blog` 时，插件会自动去寻找 `docs/blog/posts/` 这个特定的文件夹。由于我们刚才把 `hello-world.md` 直接放在了 `docs/blog/` 下，插件把它当成了普通页面，没有把它识别为博客文章，所以博客列表才没有更新。

我们来快速修正一下，只需调整一下文件夹结构即可：

### 修正步骤：把文章放进 `posts` 文件夹

1. 打开你的 `docs/blog/` 文件夹。
2. 在里面新建一个名为 **`posts`** 的子文件夹。
3. 把你刚才写的 **`hello-world.md`** 移动到这个 `posts` 文件夹里。

调整后的正确目录结构应该是这样的：

```
my-blog/
├── mkdocs.yml
└── docs/
    ├── index.md
    └── blog/
        └── posts/              <-- 关键在这里！所有博客文章必须放在 posts 目录下
            └── hello-world.md
```

接着打开 `mkdocs.yml`，在最下面加上 `nav`（导航）配置。你的完整配置文件现在应该长这样（你可以直接复制替换）：

```
site_name: 我的个人主页

theme:
  name: material
  language: zh

plugins:
  - search
  - blog

# 新增这一段，手动指定顶部导航栏
nav:
  - 主页: index.md
  - 博客: blog/
```

保存后，如果顶部出现了“博客”字样，点击它就能进去了！或者你也可以直接在浏览器里访问 `http://127.0.0.1:8000/blog/` 试试看。
