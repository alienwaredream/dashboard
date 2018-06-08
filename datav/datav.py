#!/usr/bin/python
#coding=utf8

# import module
import pymysql

his = 'zjhis/*@oracle'
SelMZRC = '''select count(*) JZRC from zj_jzxx where JZRQ between to_date(to_char(sysdate,'yyyy-mm-dd') || ' 00:00:01','yyyy-mm-dd hh24:mi:ss') and to_date(to_char(sysdate,'yyyy-mm-dd') || ' 23:59:59','yyyy-mm-dd hh24:mi:ss')
'''

SelCYRC = '''select count(*) from zy_patient_information where out_date between to_date(to_char(sysdate,'yyyy-mm-dd') || ' 00:00:01','yyyy-mm-dd hh24:mi:ss') 
and to_date(to_char(sysdate,'yyyy-mm-dd') || ' 23:59:59','yyyy-mm-dd hh24:mi:ss')
'''

SelGHRC = '''select count(*) from gh_ghk where GHRQ between to_date(to_char(sysdate,'yyyy-mm-dd') || ' 00:00:01','yyyy-mm-dd hh24:mi:ss') 
and to_date(to_char(sysdate,'yyyy-mm-dd') || ' 23:59:59','yyyy-mm-dd hh24:mi:ss')
'''

#定义oracle查询数据函数
def OracleSQL(sql,DBinfo):
    import re
    import cx_Oracle as oracle
 
    # connect oracle database
    db = oracle.connect(DBinfo)

    # create cursor
    cursor = db.cursor()
 
    # execute sql
    cursor.execute (sql)
 
    # fetch data
    res = cursor.fetchone().__str__()
    

    res = re.sub("\D", "", res)
    #print(type(res),res)

    # close cursor and oracle
    cursor.close()
    db.close()

    return res


GHRC_today = OracleSQL(SelGHRC,his)

MZRC_today = OracleSQL(SelMZRC,his)
#print(MZRC_today)

CYRC_today = OracleSQL(SelCYRC,his)
#print(CYRC_today)




def MysqlINSERT(sql,data,DBinfo):
    import pymysql

    # 打开数据库连接
    
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = DBinfo.cursor()
 
    # SQL 插入语句

    try:
       # 执行sql语句
       cursor.execute(sql)
	   
       # 提交到数据库执行
       #DBinfo.commit()
       #print("执行成功！")
    except:
       # 如果发生错误则回滚
       DBinfo.rollback()
       #print("执行失败！")
 
    # 关闭数据库连接
    #DBinfo.close()

INSERTSQL1 = "UPDATE today SET mzrc = %s WHERE dw = 'qz' " %MZRC_today
INSERTSQL2 = "UPDATE today SET cyrc = %s WHERE dw = 'qz' " %CYRC_today
INSERTSQL3 = "UPDATE today SET ghrc = %s WHERE dw = 'qz' " %GHRC_today

MysqlDBinfo = pymysql.Connect(
            host='*',
            port=3306,
            user='datav',
            passwd='datav',
            db='datav',
            charset='utf8'
    )

MysqlINSERT(INSERTSQL1,MZRC_today,MysqlDBinfo)
MysqlINSERT(INSERTSQL2,CYRC_today,MysqlDBinfo)
MysqlINSERT(INSERTSQL3,GHRC_today,MysqlDBinfo)


# 提交到数据库执行
MysqlDBinfo.commit()

# 关闭数据库连接
MysqlDBinfo.close()