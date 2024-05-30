<div align="center">

# nonebot-plugin-template

_✨ <your_plugin_description> ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/<your_github>/nonebot-plugin-template.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-template">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-template.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>

<!-- 以下为模板库使用说明，请完成后删除 -->

这是一个使用 [`PDM`](https://github.com/pdm-project/pdm) 作为包管理器的 nonebot2 插件项目的模板库, 你可以直接使用本模板创建你的 nonebot2 插件项目的仓库

<details>
<summary>模板库使用方法</summary>

1. 点击仓库中的 "Use this template" 按钮, 输入仓库名与描述, 点击 "  Create repository from template" 创建仓库
2. 在创建好的新仓库中, 在 "Add file" 菜单中选择 "Create new file", 在新文件名处输入`LICENSE`, 此时在右侧会出现一个 "Choose a license template" 按钮, 点击此按钮选择开源协议模板, 然后在最下方提交新文件到主分支
3. 本地机器首先需要安装 git, python 3.9+ 和 pdm 2.13+
4. 克隆你刚刚创建的仓库到本地, 并进入仓库目录, 执行 `pdm sync` 安装虚拟环境与依赖
5. 利用编辑器打开仓库目录, 执行以下全局替换操作：
    - 全局替换`nonebot-plugin-template` 为你插件的包名 (用于 pip 安装等)
    - 全局替换`nonebot_plugin_template` 为你插件的包名 (用于 python 导入等)
    - 全局替换`<your_plugin_humanized_name>` 为你插件的可读名 (用于插件商店 等)
    - 全局替换`<your_plugin_description>` 为你插件的简单描述
    - 全局替换`<your_github>` 为你的 github 用户名
    - 全局替换`<your_email>` 为你的邮箱
    
6. 修改 README 中的插件名和插件描述, 并在下方填充相应的内容

</details>

<details>
<summary>配置发布工作流</summary>

模块库中自带了一个发布工作流, 你可以使用此工作流自动发布你的插件到 pypi

1. 前往 https://pypi.org/ 并注册一个账号。
2. 前往 https://pypi.org/manage/account/publishing/, 下翻到 `Pending publishers`
3. 选择 `Github` 选项栏，填写相关信息：
    - PyPI Project Name: 你的插件包名，如 `nonebot-plugin-template`
    - Owner: 你的 Github 用户名
    - Repository name: 你的插件仓库名称，如 `nonebot-plugin-template`
    - Workflow name: 请填入 `release.yml`
4. 点击 `Add` 按钮，完成发布工作流配置

</details>

<details>
<summary>触发发布工作流</summary>

1. 任意提交后，在 Github 仓库界面点击 `Releases` 选项，点击 `Create a new release` 按钮。若没有 `Release` 选项，可在仓库主页点击 `Tags` 选项，在新界面点击 `Create a new release` 按钮
2. 点击 `Choose a tag`，输入以 `v` 开头的版本号，如 `v0.0.1`，然后点击 `Create new tag` 按钮
3. 填写 `Release title` 和 `Describe this release`。或点击 `Generate release notes` 自动生成相关信息
4. 点击 `Publish release` 按钮，触发发布工作流

</details>

<!-- 以上为模板库使用说明，请完成后删除 -->

## 介绍

这里是插件的详细介绍部分

## 安装方法

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-template

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-template
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-template
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-template
</details>


打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_template"]

</details>

# ...
<!-- 此处填写插件的其他介绍 -->
