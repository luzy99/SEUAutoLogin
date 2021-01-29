# encoding=utf-8
import json
from login import login


# 加载全局配置
with open("./config.json", "r", encoding="utf-8") as f:
    configs = f.read()
configs = json.loads(configs)


def getGradeList(ss, terms):
    ss.get("http://ehall.seu.edu.cn/appShow?appId=4768574631264620")

    url = 'http://ehall.seu.edu.cn/jwapp/sys/cjcx/modules/cjcx/xscjcx.do'

    params = {"querySetting": [{"name": "SHOWMAXCJ", "caption": "显示最高成绩", "linkOpt": "AND",
                                "builderList": "cbl_String", "builder": "equal", "value": 0, "value_display": "否"}],
              "*order": "-XNXQDM,-KCH,-KXH",
              "pageSize": 100,
              "pageNumber": 1}
    res = ss.post(url, data=params)
    data = json.loads(res.text)['datas']['xscjcx']
    print("成功读取 %s 门课程成绩" % data['totalSize'])

    sum_xf = 0
    sum_gpa = 0
    term_xf = 0
    term_gpa = 0
    for item in data['rows']:
        if item['KCXZDM_DISPLAY'] == '必修':
            sum_xf += float(item['XF'])
            sum_gpa += float(item['XF']) * computeGpa(item['ZCJ'])
            if item['XNXQDM'] in terms:
                term_xf += float(item['XF'])
                term_gpa += float(item['XF']) * computeGpa(item['ZCJ'])
    print("必修总学分：%f, 累计绩点：%f" % (sum_xf, sum_gpa / sum_xf))
    if term_xf > 0:
        print("Terms in ", terms)
        print("学年必修总学分：%f, 学年绩点：%f" % (term_xf, term_gpa / term_xf))


def computeGpa(score):
    score = float(score)
    if score >= 96:
        gpa = 4.8
    elif score >= 93:
        gpa = 4.5
    elif score >= 90:
        gpa = 4.0
    elif score >= 86:
        gpa = 3.8
    elif score >= 83:
        gpa = 3.5
    elif score >= 80:
        gpa = 3.0
    elif score >= 76:
        gpa = 2.8
    elif score >= 73:
        gpa = 2.5
    elif score >= 70:
        gpa = 2.0
    elif score >= 66:
        gpa = 1.8
    elif score >= 63:
        gpa = 1.5
    elif score >= 60:
        gpa = 1.0
    else:
        gpa = 0.0
    return gpa


if __name__ == '__main__':
    ss = login(configs['user']['cardnum'], configs['user']['password'])
    if ss:
        getGradeList(ss, ['2020-2021-1'])
