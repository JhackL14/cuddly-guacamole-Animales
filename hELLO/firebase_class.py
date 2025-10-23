from config import SDK, URL_DB
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db




class FB:
    def __init__(self):
        # Recibe la credencial del usuario
        cred = credentials.Certificate(SDK)

        # Inicializa la base de datos con los permisos dado por la credencial
        firebase_admin.initialize_app(cred, {'databaseURL': URL_DB})

        # Se guarda en la variable 'ref' una refencia en la base de datos
        ref = db.reference('server/saving-data')
            
        # Crea un nodo secundario llamado 'Users'
        users_ref = ref.child('Users')

    # Funcion para crear un usuario en la base de datos
    def create(nombre, edad, sexo, rol, contraseña):
        """nombre: recibe el nombre para asignar una clave, donde los datos seran valores dentro de este\n
        edad: almacena la informacion de edad
        sexo: almacena la inforamcion del sexo\n
        rol: almacena la informacion del rol (Estudiante, Profesor)\n
        contraseña: almacena la contraseña del usuario"""

        #users_ref.child(nombre).set: crea un nodo secundario en la base de datos como una clave,
        #con la variable nombre y agrega los datos dentro como valores
        ref_user = db.reference(f'server/saving-data/Users/{nombre}')
        
        if ref_user.get() == None:  # Condicion para saber si esta el nombre dado esta en la base de datos
            users_ref.child(nombre).set({
                    'Edad' : edad,
                    'Sexo' : sexo,
                    'Rol' : rol,
                    'Contraseña' : contraseña
            })
            return True # Cuando se ha creado el nuevo usuario
        else:
            return False #Que ocurre cuando el usuario ya existe dentro de la base de datos

    #create("nombre", 'edad', 'sexo', 'rol', 'contraseña')

    def acceso_usuarios(user, password):
        ref_password = db.reference(f'server/saving-data/Users/{user}/Contraseña')
        ref_user = db.reference(f'server/saving-data/Users/{user}')
        
        if ref_user.get() != None:  # Condicion para saber si esta el nombre dado esta en la base de datos
            contraseña = ref_password.get()
            if contraseña == password:
                return user
            
            else:
                return False # Ocurre cuando la contraseña ingresada es incorrecta

    # Funcion para leer inforamcion de un usuario en la base de datos
    def read(value):
        """value: Recibe el valor de una clave para buscarlo en la base de datos"""
        # Recibe el nombre en value y lo busca como clave en la base de datos
        ref = db.reference(f'server/saving-data/Users/{value}')

        if ref.get() != None:  # Condicion para saber si esta el nombre dado esta en la base de datos
            return True
            #print(ref.get()) #Obtiene los valores dentro de la clave dada en value
        else:
            #print('Usuario no encontrado') 
            return False

    def update(ref, key, val):
        """ ref: Recibe el valor de una clave para buscar en la base de datos
            key: recible en valor de una clave anidada para cambiar un valor
            val: recibe el valor nuevo para asignar a la clave anterior"""
        # Recibe el nombre en value y lo busca como clave en la base de datos
        update_ref = db.reference(f'server/saving-data/Users/{ref}')
        if update_ref.get() != None:  # Condicion para saber si esta el nombre dado esta en la base de datos
            update_ref.update({       # Dada una clave actualiza el valor
                key : val
            })
        else:
            print('Usuario no encontrado')

    # Funcion para eliminar usuarios de la base de datos
    def delete(value):
        """value: Recibe el valor de una clave para buscarlo en la base de datos"""
    # Recibe el nombre en value y lo busca como clave en la base de datos
        ref = db.reference(f'server/saving-data/Users/{value}')
        if ref.get() != None:  # Condicion para saber si esta el nombre dado esta en la base de datos
            # Borra la clave dada en ref (vendria a ser el usuario)
            ref.delete()
 
