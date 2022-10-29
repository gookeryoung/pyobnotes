---
aliases: 
tags: 
title: postgresql 服务
date created: 星期六, 十月 29日 2022, 3:36:49 下午
date modified: 星期六, 十月 29日 2022, 8:24:53 晚上
---

# postgresql 服务

## 安装服务

使用以下命令安装 Postgresql 服务：

```bash
sudo apt install postgresql
```

默认情况下，PostgreSQL 服务在安装后自动启动。您可以使用以下命令确认它是否正在运行：

```bash
sudo systemctl status postgresql
```

如果成功则显示状态未 active：

```bash
● postgresql.service - PostgreSQL RDBMS
     Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor preset: enabled)
     Active: active (exited) since Sat 2022-10-29 15:36:15 CST; 15s ago
    Process: 792191 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
   Main PID: 792191 (code=exited, status=0/SUCCESS)
        CPU: 1ms
```

## 运行 postgres

切换 linux 用户到 postgres，并执行 `psql`：

```bash
sudo su - postgres
psql
```

正常情况会进入以下界面：

```bash
postgres=#
```

## 创建用户和数据库

```sql
# 创建用户，如wiki
postgres=# create user wiki with password 'mypass';
# CREATE ROLE

# 创建数据库，如wikidb
postgres=# create database wikidb owner wiki;
# CREATE DATABASE

# 授予所有权限
postgres=# grant all privileges on database wikidb to wiki;
# GRANT

# 退出
postgres=# \q
```
