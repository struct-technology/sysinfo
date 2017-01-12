from sqlalchemy import Column, Integer, String, Float

from config import ModelBase


class SystemUsage(ModelBase):
    __tablename__ = 'system_usage'

    id = Column(Integer, primary_key=True)
    hash = Column(String, nullable=False)
    memory_usage = Column(Float, nullable=False)
    cpu_usage = Column(Float, nullable=False)
    total_uptime = Column(String(30), nullable=False)