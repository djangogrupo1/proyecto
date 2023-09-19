from app import app,ma,db

# defino la tabla
class Farmacos(db.Model):   # la clase Farmacos hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    codigo_barras = db.Column(db.String(100))
    nombre  =db.Column(db.String(200))
    presentacion = db.Column(db.String(200))
    laboratorio = db.Column(db.String(200))
    concentracion = db.Column(db.String(100))
    lote = db.Column(db.String(100))
    stock = db.Column(db.Integer)
    fecha_vencimiento = db.Column(db.String(50))
    
    def __init__(self,codigo_barras,nombre,presentacion,laboratorio,concentracion,lote,stock,fecha_vencimiento):   #crea el  constructor de la clase
        self.codigo_barras = codigo_barras    # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.nombre = nombre
        self.presentacion = presentacion   
        self.laboratorio = laboratorio
        self.concentracion = concentracion
        self.lote = lote
        self.stock = stock
        self.fecha_vencimiento = fecha_vencimiento
    
    #  si hay que crear mas tablas , se hace aqui

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************

class FarmacosSchema(ma.Schema):
    class Meta:
        fields=('id','codigo_barras','nombre','presentacion','laboratorio','concentracion','lote','stock','fecha_vencimiento')



