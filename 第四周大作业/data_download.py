import requests
import zipfile

# 文件的URL
url = 'https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16146316576563200.zip?authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%2F2024-06-14T20%3A59%3A23Z%2F604800%2F%2F1c07b057542a3d39c52ab3770020d9a85f98b56718780462b2aa0f78160d9d0f'

# 文件保存路径
download_path = 'D:/DataFiles/autoData/single-vehicle-side-example_16146316576563200.zip'

# 发送HTTP请求
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(download_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=65536): 
            f.write(chunk)

# 解压文件
unzip_path = 'D:/DataFiles/autoData/single-vehicle-side-example_16146316576563200'

with zipfile.ZipFile(download_path, 'r') as zip_ref:
    zip_ref.extractall(unzip_path)

print('文件下载解压成功！')
