## crontab

```
0 0 * * * /root/.pyenv/shims/python /root/selenium/ths_stock_info_spider_linux.py
```

## Linux 下 selenium 安装

安装chrome内核：

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum install ./google-chrome-stable_current_x86_64.rpm
```

下载chromedriver，注意要和安装的chrome内核对应（版本列表：http://chromedriver.chromium.org/downloads）：

```
wget https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip
```

参考：[Linux 无GUI下使用selenium](https://www.jianshu.com/p/b5f3025b5cdd)
