from database import Base
from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.orm import relationship

class Device(Base):
    __tablename__ = "device"
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    name = Column(String,nullable=False,unique=True)
    category = relationship("DeviceCategory",back_populates="category")
