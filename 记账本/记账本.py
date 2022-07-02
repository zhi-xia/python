import datetime
import json

import PySimpleGUI as sg


# 初始化数据
def initData():
    d = '[{"时间":"2022/06/28 14:20:21", "项目":"收到货款", "金额":20000, "分类":"收入"}]'
    with open(r"data.txt", "w") as f:
        f.write(d)


def readData():  # 读取json数据
    with open(r"data.txt", "r") as f:
        jsonData = f.read()
        dataList = json.loads(jsonData)
        return dataList


def writeData(dataList):  # 写入数据
    jsonData = json.dumps(dataList, ensure_ascii=False)
    with open(r"data.txt", "w") as f:
        f.write(jsonData)


def showData():  # 显示数据
    data = readData()
    dataLists = []
    for d in data:
        if d["分类"] == "收入":
            dataList = [d["时间"], d["项目"], d["金额"], d["分类"]]
            dataLists.append(dataList)
        else:
            dataList = [d["时间"], d["项目"], d["金额"] * -1, d["分类"]]
            dataLists.append(dataList)
    return dataLists


def sumin():  # 计算总收入
    sumin = 0
    data = readData()
    for d in data:
        if d["分类"] == "收入":
            sumin += d["金额"]
    return sumin


def sumout():  # 计算总支出
    sumout = 0
    data = readData()
    for d in data:
        if d["分类"] == "支出":
            sumout += d["金额"]
    return sumout


def addData(content, amount, cla):  # 添加数据
    dataList = readData()
    t = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")  # 获取当前时间
    data = {"时间": t, "项目": content, "金额": amount, "分类": cla}
    dataList.append(data)
    writeData(dataList)


def delData(content):  # 删除数据
    dataList = readData()
    n = len(dataList)
    while n:
        if dataList[n - 1]["项目"] == content:
            del dataList[n - 1]
            writeData(dataList)
            updataData()
            return 1
        n -= 1
    return 0


def updataData():  # 更新数据
    list = showData()
    sin = sumin()
    sout = sumout()
    text = "总收入是" + str(sin) + "元，总支出是" + str(sout) + "元，结余是" + str(sin - sout) + "元"
    window["-show-"].update(values=list)
    window["-text-"].update(value=text)
    window["-content-"].update("")
    window["-amount-"].update("")


def initLayout():  # 初始化界面
    layout = [
        [sg.T("账目清单")],
        [sg.Table(list,
                  headings=["时间", "项目", "金额", "分类"],
                  justification="c",  # 居中
                  auto_size_columns=False,  # 取消自动列宽
                  def_col_width=15,  # 设置列宽
                  select_mode="browse",
                  key="-show-"
                  )],
        [sg.T("总收入是" + str(sin) + "元，总支出是" + str(sout) + "元，结余是" + str(sin - sout) + "元", key="-text-")],
        [sg.T("请输入账单项目："), sg.In(key="-content-")],
        [sg.T("请输入账单金额："), sg.In(key="-amount-")],
        [sg.T("请选择账单分类：")] + [sg.Radio(i, group_id=1, key=i) for i in ["收入", "支出"]],
        [sg.B("确认提交")] + [sg.B("删除账单")] + [sg.T("小组成员：周文博  俞树深  王小康")]
    ]
    return layout


def delLayout():  # 删除账单界面
    layout = [
        [sg.T("请输入要删除的项目："), sg.In(key="-content-")],
        [sg.B("确认删除")]
    ]
    window = sg.Window("删除账单", layout)
    while True:
        event, values = window.read()

        if event == "确认删除":
            if delData(values["-content-"]):
                sg.popup("删除成功")
            else:
                sg.popup("没有该项目")
            window["-content-"].update("")

        if event is None:
            break
    window.close()


if __name__ == '__main__':
    try:
        sin = sumin()
    except FileNotFoundError:
        initData()
        sin = sumin()
    sout = sumout()
    list = showData()
    window = sg.Window("记账本", initLayout())
    while True:
        event, values = window.read()

        if event == "确认提交":
            try:
                content = values["-content-"]
                amount = float(values["-amount-"])
                for k, v in values.items():
                    if v == True:  # 这个地方不知道为什么一定要这么写，而不能直接写v
                        cla = k
                        addData(content, amount, cla)
                        updataData()
                sg.popup("添加成功")  # 弹窗
            except ValueError:
                pass

        if event == "删除账单":
            delLayout()

        if event is None:
            break

    window.close()
