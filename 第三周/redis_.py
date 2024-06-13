import redis

host = 'hadoop104'
port = 6379
r = redis.Redis(host=host,port=port,db=0)

# 增（添加数据）
r.set('name2', 'Zhengshan Tian')  # 添加键值对
r.mset({'name3': 'Jiabin Ji', 'name4': 'Tailai Zhou', 'name': 'gzg'})  # 添加多个键值对

# 查（获取数据）
value = r.get('name').decode('utf-8')  # 获取单个键的值
print(f"Value of name: {value}")

values = r.mget(['name2', 'name3'])  # 获取多个键的值
print("Values of name2 and name3:", [v.decode('utf-8') for v in values])

# 改（更新数据）
r.set('name', 'Zengguang2 Gao')  # 更新键的值
print(f"Updated value of name: {r.get('name').decode('utf-8')}")

# 删（删除数据）
r.delete('name')  # 删除键
print(f"name deleted: {r.get('name') is None}")

# 其他操作
print(r.exists('name'))  # 检查键是否存在
r.expire('name2', 10)  # 设置键的过期时间为10秒
print(r.ttl('name2'))  # 查看键的剩余过期时间
