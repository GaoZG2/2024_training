# 导入pymysql模块
import pymysql

# 建立数据库连接
conn = pymysql.connect(
    host='hadoop104',
    port=3306,
    user='root',
    password='root',
    charset='utf8mb4'
)

# 获取mysql服务信息（测试连接，会输出MySQL版本号）
print(conn.get_server_info())

# 创建游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("school")

# 增
sql = "INSERT INTO student (id, name) VALUES (4, 'Jiabin Ji'), (5, 'Tailai Zhou')"
cursor.execute(sql)

# 删
sql = "DELETE FROM student WHERE id = 4"
cursor.execute(sql)

# 改
sql = "UPDATE student SET name = 'Tailai2 Zhou' WHERE id = 5"
cursor.execute(sql)

# 提交事务
conn.commit()

# 查
sql = "SELECT * FROM student"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()

