from django import http

from calery_tasks.main import app
from calery_tasks.moules import WebUrls
from libs import mysqlconnect
from pymysql import *
import json



@app.task
def save_urls(addurls,errorurls):
    addurls = addurls
    errorurls = errorurls
    sucurl = []
    # 重复的url
    checkurls = []
    # 数据库连接
    urlslist = []
    for url in addurls:
        print(url)
        sucurl.append(url)

    # errmsg = '添加成功，成功添加子域名' + str(len(addurls)) + '个,错误格式子域名' + str(len(errorurls)) + '个,重复子域名' + str(
    #     len(checkurls)) + '个。'
    # return http.JsonResponse(
    #     {'code': 200, 'errmsg': errmsg, 'addurls': addurls, 'errorurls': errorurls, 'checkurls': checkurls})
    return http.JsonResponse({'code': 200, 'errmsg':sucurl} )


@app.task
def refersh_urls():
    addurls = []
    # 重复的url
    checkurls = []
    # 数据库连接
    urlslist = []
    #Sylas数据库连接
    conn = connect(host=mysqlconnect.host, user=mysqlconnect.user, password=mysqlconnect.password,
                   database=mysqlconnect.database2, charset='utf8')
    # cursor()方法获取操作游标
    cursor = conn.cursor()
    # 查询收集到的域名
    sql = mysqlconnect.sql
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有记录的列表
        results = cursor.fetchall()
        for row in results:
            # 获取收录的子域名
            url = row[1]
            try:
                a = WebUrls.objects.filter(urls=url)[0]
                if a.urls == url:
                    checkurls.append(url)
                    pass
            except Exception as e:
                print(e)
                # save_urls.delay(url)
                # 记录成功添加的域名
                try:
                    # 取id的最大值然后新增时+1达到自增加的需求
                    urlsdata = WebUrls.objects.all()
                    for i in urlsdata:
                        urlslist.append(i.urid)
                    max_data = max(urlslist)
                    urlsdemo = WebUrls(urid=max_data + 1, urls=url)
                except:
                    urlsdemo = WebUrls(urid=1, urls=url)
                urlsdemo.save()
                addurls.append(url)
    except Exception as e:
        print(e)

    cursor.close()
    conn.commit()
    conn.close()

    errmsg = '添加成功，成功添加子域名' + str(len(addurls)) + '个,重复子域名' + str(len(checkurls)) + '个。'
    return http.JsonResponse({'code': 200, 'errmsg': errmsg, 'addurls': addurls, 'checkurls': checkurls})