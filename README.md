# MySQL-Note
# 模組安裝 pip install mysql-connector-python
# 載入模組 mysql.connector
# 連結資料庫 connection = mysql.connector.connect(host='本機localhost',
                                    port='3306',
                                    user='root',
                                    password='password')

# 開始使用     cursor = connection.cursor()
# 使用完要關閉  cursor.close()
# 使用完要關閉  connection.close()
