# create:

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='password')

cursor = connection.cursor()

# 創建資料庫
cursor.execute("CREATE DATABASE `database`;")


# 取得所有資料庫名稱
# cursor.execute("SHOW DATABASES;")
# records = cursor.fetchall()
# for r in records:
#     print(r)


# 選擇資料庫
# cursor.execute("USE `sql_tutorial`;")


# 創建表格
# cursor.execute('CREATE TABLE `qq`(qq INT);')

cursor.close()
connection.close()

---------------------------------------------------------
# select:

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='password',
                                    database='sql_tutorial')

cursor = connection.cursor()

# 取的部門表格所有資料
cursor.execute('SELECT * FROM `branch`;')

records = cursor.fetchall()
for r in records:
    print(r)

cursor.close()
connection.close()


-------------------------------------------------------
# update

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='password',
                                    database='sql_tutorial')

cursor = connection.cursor()

# 新增
# cursor.execute("INSERT INTO `branch` VALUES(5, 'qq', NULL)")


# 修改
# cursor.execute('UPDATE `branch` SET `manager_id` = 206 WHERE `branch_id` = 4;')


# 刪除
# cursor.execute("DELETE FROM `branch` WHERE `branch_id` = 5;")


cursor.close()
connection.commit()
connection.close()

