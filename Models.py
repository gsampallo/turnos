from sqlalchemy import Column, Integer, String, Float, DateTime
import BD

class Turnos(BD.Base):
    __tablename__ = 'turnos'

    id = Column(Integer, primary_key=True)
    inicio = Column(DateTime)
    fin = Column(DateTime)
    vencido = Column(Integer)