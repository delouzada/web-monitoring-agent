from sqlalchemy import Column, Integer, Float, String, DateTime, func
from infrastructure.persistence.connection_factory import Base
from datetime import datetime

class NetworkTestResult(Base):
    """Representa um teste de rede armazenado no banco de dados."""
    __tablename__ = "network_test_results"
    __table_args__ = {'extend_existing': True}  # Permite reuso da tabela no MetaData

    id = Column(Integer, primary_key=True, autoincrement=True)
    site = Column(String, nullable=False)  # Adicionado
    latency = Column(Float, nullable=True)  # Latência em ms
    packet_loss = Column(Float, nullable=True)  # Perda de pacotes em %
    response_time = Column(Float, nullable=True)  # Tempo de resposta em segundos
    timestamp = Column(DateTime, default=datetime.utcnow)
    status_code = Column(Integer, nullable=True)  # Adicionado

    def __repr__(self):
        return (f"<NetworkTestResult(id={self.id}, site='{self.site}', latency={self.latency}, "
                f"packet_loss={self.packet_loss}, response_time={self.response_time}, timestamp={self.timestamp})>")
