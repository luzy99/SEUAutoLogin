# SEU Auto Login

东南大学信息门户自动登录，采用requests库，获取登录session，无需浏览器依赖，全平台通用。

**本项目仅供学习使用**

- 🌡**自动每日健康上报**
- 💯**绩点计算**

## 📋目录结构

```sh
│  config.json	# 配置文件
│  dayReport.py	# 每日上报脚本
│  gpa.py		# gpa计算脚本
│  ids-encrypt.js	# SEU 身份认证AES加密算法
│  ids_encrypt.py	# js2py调用js代码
│  login.py		# 登录
│  readme.md
│  requirements.txt
```

## 🛠安装依赖

开发环境：python 3.7

依赖包

```
requests~=2.23.0
Js2Py~=0.70
beautifulsoup4~=4.9.3
```

安装依赖，请执行：

```sh
pip install -r requirements.txt
```

## 📐功能说明

**请先在`config.json`中填写好一卡通号和密码**

```json
    "user": {
        "cardnum": "你的一卡通号",
        "password": "登录密码"
    },
```

### 自动每日健康上报

- 运行方式，双击或命令行输入运行

```
./dayReport.py
```

默认采用昨日信息填报。

**⚠ 重要：每月1号学校系统会清空填报记录，所以请手动填报！！！**

**⚠ 重要：每月1号学校系统会清空填报记录，所以请手动填报！！！**

**⚠ 重要：每月1号学校系统会清空填报记录，所以请手动填报！！！**

- （可选，不推荐）手动设置填报信息

  > 出现问题概不负责（逃

  修改`config.json`文件，修改或添加配置，以下配置将覆盖昨日信息

  ```json
  "dailyReport": {
          "school": {
              "DZ_JSDTCJTW": 36.5,	// 体温
              "DZ_SZWZLX": "002",		// 在校内
              "DZ_SZWZLX_DISPLAY": "在校内",
              "LOCATION_PROVINCE_CODE": "",
              "LOCATION_PROVINCE_CODE_DISPLAY": "",
              "LOCATION_CITY_CODE": "",
              "LOCATION_CITY_CODE_DISPLAY": "",
              "LOCATION_COUNTY_CODE": "",
              "LOCATION_COUNTY_CODE_DISPLAY": "",
              "DZ_SZXQ": "002",
              "DZ_SZXQ_DISPLAY": "九龙湖校区"
          },
      // 若不清楚区域编号请勿随意修改！！！！
          "home": {
              "DZ_JSDTCJTW": 36.555,
              "DZ_SZWZLX": "003",		// 在校外(在南京以外)
              "DZ_SZWZLX_DISPLAY": "在校外(在南京以外)",
              "LOCATION_PROVINCE_CODE": "110100",		// 省份编号
              "LOCATION_PROVINCE_CODE_DISPLAY": "北京市",
              "LOCATION_CITY_CODE": "110100",		// 城市编号
              "LOCATION_CITY_CODE_DISPLAY": "北京市",
              "LOCATION_COUNTY_CODE": "110101",	// 区编号
              "LOCATION_COUNTY_CODE_DISPLAY": "市辖区",
              "DZ_SZXQ": "",
              "DZ_SZXQ_DISPLAY": ""
          }
      ...
  }
  ```

  带配置启动方式：

  ```sh
  ./dayReport.py -c home
  ```

### GPA计算

> 按照学生手册公式计算，仅供参考

- 运行方式

  ```sh
  ./dayReport.py -t 学期号
  ```

  ```sh
  usage: gpa.py [-h] [--term TERM]
  
  Test for argparse
  
  optional arguments:
    -h, --help            show this help message and exit
    --term TERM, -t TERM  学期 20(计算20-21学年所有学期), 2020-2021-1(指定某一学期)
  examples:
  	
  ```

- examples

  ```sh
  # 一个学年
  ❯ ./gpa.py -t 19
  XXX  登陆成功！
  成功读取 50 门课程成绩
  必修总学分：90.000000, 累计绩点：4.8
  Terms in  ['2019-2020-1', '2019-2020-2', '2019-2020-3', '2019-2020-4']
  学年必修总学分：46.000000, 学年绩点：4.522826
  
  # 指定学期
  ❯ ./gpa.py -t 2020-2021-1
  XXX  登陆成功！
  成功读取 50 门课程成绩
  必修总学分：90.000000, 累计绩点：4.8
  Terms in  ['2020-2021-1']
  学年必修总学分：10.000000, 学年绩点：4.629412
  ```

  