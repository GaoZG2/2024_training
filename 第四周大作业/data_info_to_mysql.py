import pymysql
import json

# SQLAlchemy

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

# 创建表的SQL语句
create_table_query = '''
CREATE TABLE IF NOT EXISTS data_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_path VARCHAR(255) NOT NULL,
    image_timestamp BIGINT NOT NULL,
    pointcloud_path VARCHAR(255) NOT NULL,
    point_cloud_stamp BIGINT NOT NULL,
    calib_camera_intrinsic_path VARCHAR(255) NOT NULL,
    calib_lidar_to_camera_path VARCHAR(255) NOT NULL,
    label_camera_std_path VARCHAR(255) NOT NULL,
    label_lidar_std_path VARCHAR(255) NOT NULL
)
'''

# 执行创建表的SQL语句
try:
    cursor.execute(create_table_query)
    print("建表成功。")
except pymysql.Error as err:
    print(f"建表失败，错误信息: {err}")
    # 关闭游标和连接
    cursor.close()
    conn.close()
    exit(1)

# 读取JSON文件
try:
    with open('D:/DataFiles/autoData/single-vehicle-side-example_16146316576563200/single-vehicle-side-example/data_info.json', 'r') as file:
        data_info = json.load(file)
    print("文件读取成功。")

    # 文件未找到的错误处理逻辑
except FileNotFoundError as fnf_err:
    print(f"文件未找到，错误信息: {fnf_err}")
    exit(1)

    # JSON解码错误的处理逻辑
except json.JSONDecodeError as json_err:
    print(f"JSON解码错误，错误信息: {json_err}")
    exit(1)

    # 其他错误处理逻辑    
except Exception as e:
    print(f"预期外错误，错误信息: {e}")
    exit(1)

# 插入数据的SQL语句
insert_data_query = '''
INSERT INTO data_info (image_path, image_timestamp, pointcloud_path, point_cloud_stamp, calib_camera_intrinsic_path, calib_lidar_to_camera_path, label_camera_std_path, label_lidar_std_path)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
'''

# 插入每条数据
for item in data_info:
    try:
        # 检查是否有字段为空
        if(not item['image_path'] or
        not item['image_timestamp'] or
        not item['pointcloud_path'] or
        not item['point_cloud_stamp'] or
        not item['calib_camera_intrinsic_path'] or
        not item['calib_lidar_to_camera_path'] or
        not item['label_camera_std_path'] or
        not item['label_lidar_std_path']):
            print(f"跳过该条记录，因为存在空值。")
            continue

        cursor.execute(insert_data_query, (
            item['image_path'],
            item['image_timestamp'],
            item['pointcloud_path'],
            item['point_cloud_stamp'],
            item['calib_camera_intrinsic_path'],
            item['calib_lidar_to_camera_path'],
            item['label_camera_std_path'],
            item['label_lidar_std_path']
        ))
    except pymysql.Error as e:
        print(f"数据插入时遇到预料外错误: {e}\n所有已插入数据均已撤回")
        conn.rollback()
        break

# 提交事务
conn.commit()
print("所有数据均已插入。")

# 关闭游标和连接
cursor.close()
conn.close()
