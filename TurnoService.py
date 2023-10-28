import BD
from Models import Turnos


def existeTurno(t):
    session = BD.get_session()
    
    
    return session.query(Turnos).filter(Turnos.inicio==t[0],Turnos.fin==t[1]).first()


def saveTurnos(t):
    turno = Turnos()
    turno.inicio = t[0]
    turno.fin = t[1]

    session = BD.get_session()    
    session.add(turno)
    session.commit()