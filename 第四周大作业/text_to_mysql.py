import pymysql

# 数据库连接配置
config = {
    'user': 'root',
    'password': 'root',
    'host': 'hadoop104',
    'port': 3306,
    'database': 'autodata'
}

# 连接到MySQL数据库
conn = pymysql.connect(**config)
cursor = conn.cursor()

# 查询data_info表中的所有记录
query = "SELECT * FROM data_info"
cursor.execute(query)
records = cursor.fetchall()

# 列名称作为变量
column_names = ['calib_camera_intrinsic', 'calib_lidar_to_camera', 'label_camera_std', 'label_lidar_std']

# 更改表结构，新增几列
alter_table_query = f'''
ALTER TABLE data_info
ADD COLUMN {column_names[0]} TEXT,
ADD COLUMN {column_names[1]} TEXT,
ADD COLUMN {column_names[2]} TEXT,
ADD COLUMN {column_names[3]} TEXT;
'''

# 执行SQL语句
try:
    cursor.execute(alter_table_query)
    conn.commit()
    print("新列添加成功。")
except pymysql.Error as err:
    print(f"Error: {err}")

# 对每行写入新数据
for record in records:
    # 路径前缀
    prefix_path = 'D:/DataFiles/autoData/single-vehicle-side-example_16146316576563200/single-vehicle-side-example/'
    # 获取各个json文件的路径
    calib_camera_intrinsic_path = prefix_path + record[5]
    calib_lidar_to_camera_path = prefix_path + record[6]
    label_camera_std_path = prefix_path + record[7]
    label_lidar_std_path = prefix_path + record[8]
    column_paths = [calib_camera_intrinsic_path, calib_lidar_to_camera_path, label_camera_std_path, label_lidar_std_path]

    for index, column_name in enumerate(column_names):
        try:
            with open(column_paths[index], 'r') as file:
                file_content = file.read()
        except FileNotFoundError:
            print(f"未找到文件: { column_paths[index]}")
            continue
        except Exception as e:
            print(f"读文件时发生错误: {e}")
            continue

        # 将数据写入对应的行
        update_query = f" UPDATE data_info  SET  {column_name} = %s  WHERE id = %s "
        try:
            cursor.execute(update_query, (file_content, record[0]))  # id是record的第1个元素
            conn.commit()
        except pymysql.Error as e:
            print(f"更新数据（id = {record[0]}，column_name = {column_name}）时发生错误: {e}")
            conn.rollback()  # 如果有错误，回滚事务

# 关闭游标和连接
cursor.close()
conn.close()

print("文本数据写入完毕。")
