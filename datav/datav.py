#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql


def MysqlINSERT(sql,data,DBinfo):
    import pymysql

    # 打开数据库连接
    
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = DBinfo.cursor()
 
    # SQL 插入语句

    try:
       # 执行sql语句
       cursor.execute(sql)
       
       
    except:
       # 如果发生错误则回滚
       DBinfo.rollback()

 


a = 321
b = 987
INSERTSQL1 = "UPDATE today SET mzrc = %s WHERE dw = 'qz' " %a
INSERTSQL2 = "UPDATE today SET cyrc = %s WHERE dw = 'qz' " %b
MysqlDBinfo = pymysql.Connect(
            host='120.0.1.34',
            port=3306,
            user='datav',
            passwd='datav',
            db='datav',
            charset='utf8'
    )

MysqlINSERT(INSERTSQL1,a,MysqlDBinfo)
MysqlINSERT(INSERTSQL2,b,MysqlDBinfo)


# 提交到数据库执行
MysqlDBinfo.commit()
# 关闭数据库连接
MysqlDBinfo.close()