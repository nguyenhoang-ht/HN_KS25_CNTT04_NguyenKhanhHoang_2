from database import Base
from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.orm import relationship

class DeviceCategory(Base):
    __tablename__ = "category"
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    name = Column(String,nullable=False,unique=True)
    device = relationship("Device",back_populates="category")
