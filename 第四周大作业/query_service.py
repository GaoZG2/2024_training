from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, DateTime, String, JSON
from sqlalchemy.orm import sessionmaker, scoped_session
from starlette.responses import FileResponse
from starlette.requests import Request
from pathlib import Path
import uvicorn

# 创建 FastAPI 实例
app = FastAPI(title="query service")

# 定义类 DataInfo，与数据库中的 data_info 表进行交互
Base = declarative_base()
class DataInfo(Base):
    __tablename__ = 'data_info'
    id = Column(Integer, primary_key=True)
    image_path = Column(String(255))
    image_timestamp = Column(DateTime)
    pointcloud_path = Column(String(255))
    point_cloud_stamp = Column(DateTime)
    calib_camera_intrinsic_path = Column(String(255))
    calib_lidar_to_camera_path = Column(String(255))
    label_camera_std_path = Column(String(255))
    label_lidar_std_path = Column(String(255))
    calib_camera_intrinsic = Column(JSON)
    calib_lidar_to_camera = Column(JSON)
    label_camera_std = Column(JSON)
    label_lidar_std = Column(JSON)
    image_size = Column(Integer)
    pointcloud_size = Column(Integer)

# 定义数据库的连接URL
DATABASE_URL = "mysql+pymysql://root:root@hadoop104:3306/autodata"

# 创建数据库引擎
engine = create_engine(DATABASE_URL)

# 创建会话工厂
session_factory = sessionmaker(bind=engine)

# 创建作用域会话
Session = scoped_session(session_factory)

# 返回关联的 lidar/*.json的json数据、返回关联的calib/*/*.json数据
@app.get("/load_data/{image_path}")
async def load_data(image_path:str):
    # 检查文件是否有后缀
    image_path=Path(image_path)
    if image_path.suffix:
        # 如果后缀不是.jpg，将其改为.jpg
        if image_path.suffix != '.jpg':
            image_path = image_path.with_suffix('.jpg')
    else:
        # 如果文件没有后缀，添加.jpg后缀
        image_path = image_path.with_suffix('.jpg')

    # 扩展 image_name 到指定长度
    image_path = str(image_path).zfill(10)
    image_path = 'image/' + image_path

    with Session() as session:
        data = session.query(DataInfo).filter(DataInfo.image_path == image_path).first()
        if data is None:
            raise HTTPException(status_code=404, detail="Image not found.")
        response = {
            'image_path': data.image_path,
            'label_lidar_std': data.label_lidar_std,
            'calib_camera_intrinsic': data.calib_camera_intrinsic,
            'calib_lidar_to_camera': data.calib_lidar_to_camera
        }
        return response


# 返回关联的图片本地HTTP地址，地址可以复制到浏览器下载
# 路径前缀
prefix_path = 'D:/DataFiles/autoData/single-vehicle-side-example_16146316576563200/single-vehicle-side-example/'

# 下载图片
@app.get("/download_image/{image_name}")
async def download_image(image_name: str):
    # 生成图片完整路径
    image_path = Path(prefix_path + 'image/' + image_name)

    # 检查文件是否存在
    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Image not found.")

        # 发送文件
    return FileResponse(image_path, media_type="image/jpg", filename=image_name)

# 获取图片的 HTTP 地址
@app.get("/get_image_path/{image_name}")
async def get_image_path(image_name: str, request: Request):
    # 检查文件是否有后缀
    image_name=Path(image_name)
    if image_name.suffix:
        # 如果后缀不是.jpg，将其改为.jpg
        if image_name.suffix != '.jpg':
            image_name = image_name.with_suffix('.jpg')
    else:
        # 如果文件没有后缀，添加.jpg后缀
        image_name = image_name.with_suffix('.jpg')

    # 扩展 image_name 到指定长度
    image_name = str(image_name).zfill(10)
    # 获取 URL
    image_url = request.url_for("download_image", image_name=image_name)
    # 返回图片的下载URL
    return {"image_url: ": image_url}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
