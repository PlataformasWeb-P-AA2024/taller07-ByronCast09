from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


with open('data/datos_clubs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        nombre, deporte, fundacion = line.strip().split(';')
        club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
        session.add(club)

session.commit()
#------------------------	
with open('data/datos_jugadores.txt', 'r', encoding='utf-8') as file:
    for line in file:
        club_id, posicion, dorsal, nombre = line.strip().split(';')

        club = session.query(Club).filter_by(id=club_id).first()
        # Buscar el club por su id
        #club = session.query(Club).filter_by(nombre= club_id).one()
        
        jugador = Jugador(nombre=nombre, dorsal=dorsal, posicion=posicion, club=club)
        session.add(jugador)
        
session.commit()