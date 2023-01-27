---
aliases: 
tags: 
title: 安装 Nginx 和 php 服务
date created: 星期五, 十月 7日 2022, 3:16:45 下午
date modified: 星期五, 一月 27日 2023, 11:10:38 上午
---

# 安装 Nginx 和 php 服务

```bash
sudo apt-get update
sudo apt-get install nginx php7.3-fpm php7.3-cli php7.3-curl php7.3-gd php7.3-cgi
sudo service nginx start
sudo service php7.3-fpm restart
```

如果安装成功，可通过 `192.168.x.x` (* 树莓派 IP*) 访问到 Nginx 的默认页. Nginx 的根目录在 `/var/www/html`

设置 Nginx：

```bash
sudo vi /etc/nginx/sites-available/default
```

将其中的如下内容：

```bash
location / {
            # First attempt to serve request as file, then
            # as directory, then fall back to displaying a 404.
            try_files $uri $uri/ =404;
}
```

替换为：

```bash
location / {
    index  index.html index.htm index.php default.html default.htm default.php;
}
 
location ~\\.php$ {
    fastcgi_pass unix:/run/php/php7.3-fpm.sock;
    #fastcgi_pass 127.0.0.1:9000;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    include fastcgi_params;
}
```

# 重启 Nginx

```bash
sudo service nginx restart
```

# 安装 pi-dashboard

```bash
sudo apt-get install git
cd /var/www/html
sudo git clone <https://github.com/spoonysonny/pi-dashboard.git>
```

即可通过 `http://树莓派IP/pi-dashboard` 访问部署好了的 Pi Dashboard.
