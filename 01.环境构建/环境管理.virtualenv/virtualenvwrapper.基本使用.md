---
aliases: 
tags: 
title: virtualenvwrapper.基本使用
date created: 星期六, 九月 3日 2022, 9:53:55 上午
date modified: 星期日, 三月 26日 2023, 9:02:38 上午
---

# virtualenvwrapper.基本使用

`virtualenvwrapper` 是 `virtualenv` 的扩展包，可以把新创建的环境记录下来，不需要每次启动虚拟环境时执行 source 命令，可以更方便的管理虚拟环境。

## 安装

使用以下命令安装 `virtualenvwrapper`：

```bash
pip install virtualenvwrapper
```

然后找到 `virtualenvwrapper.sh` 所在位置：

```bash
which virtualenvwrapper.sh
```

或者

```bash
find / -name virtualenvwrapper.sh
```

同时找到 `python3` 所在位置：

```bash
which python3
```

得到以下结果:

- `/home/<username>/.local/bin/virtualenvwrapper.sh`
- `/usr/bin/python3`

## 配置环境变量 [linux]

然后在 `.bashrc` 文件中增加对应环境变量：

```bash
sudo vi ~/.bashrc
```

```bash
# ~/.bashrc
....

export PATH=$PATH:$HOME/.local/bin
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source $HOME/.local/bin/virtualenvwrapper.sh
```

```bash
source ~/.bashrc
```

显示以下结果即表示安装完成：

```bash
virtualenvwrapper.user_scripts creating /home/<username>/.virtualenvs/premkproject
virtualenvwrapper.user_scripts creating /home/<username>/.virtualenvs/postmkproject
virtualenvwrapper.user_scripts creating /home/<username>/.virtualenvs/initialize
...
```

## 创建虚拟环境

通过 `mkvirtualenv --python=[python3 path] [venv name]` 即可创建虚拟环境，例如：

```bash
mkvirtualenv --python=python3.8 gamedev
```

显示以下信息即表示创建完成:

```bash
created virtual environment CPython3.10.4.final.0-64 in 197ms
  creator CPython3Posix(dest=/home/<username>/.virtualenvs/webdev, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/<username>/.local/share/virtualenv)
    added seed packages: pip==22.2.2, setuptools==65.3.0, wheel==0.37.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
virtualenvwrapper.user_scripts creating /home/<username>/.virtualenvs/webdev/bin/predeactivate
virtualenvwrapper.user_scripts creating /home/<username>/.virtualenvs/webdev/bin/postdeactivate
...
```

## virtualenvwrapper.基本使用

```bash
# 进入/切换虚拟环境
workon [venv name]

# 退出虚拟环境
deactivate

# 列出所有虚拟环境
workon
# 或者
lsvirtualenv

# 删除虚拟环境
rmvirtualenv [venv name]
```
