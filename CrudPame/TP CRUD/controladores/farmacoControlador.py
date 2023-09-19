from flask import jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from app import app, ma

from modelos.farmacoModelo import *


farmacos_schema = FarmacosSchema()            # El objeto producto_schema es para traer un producto
farmacos_schema = FarmacosSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto

# crea los endpoint o rutas (json)
@app.route('/farmacos',methods=['GET'])
def get_Farmacos():
    all_farmacos=Farmacos.query.all()         # el metodo query.all() lo hereda de db.Model
    result=farmacos_schema.dump(all_farmacos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla

@app.route('/farmacos/<id>',methods=['GET'])
def get_farmacos(id):
    farmacos=Farmacos.query.get(id)
    return farmacos_schema.jsonify(farmacos)   # retorna el JSON de un farmaco recibido como parametro

@app.route('/farmacos/<id>',methods=['DELETE'])
def delete_farmaco(id):
    farmacos=Farmacos.query.get(id)
    db.session.delete(farmacos)
    db.session.commit()
    return farmacos_schema.jsonify(farmacos)   # me devuelve un json con el registro eliminado


@app.route('/farmacos', methods=['POST']) # crea ruta o endpoint
def create_farmacos():
    #print(request.json)  # request.json contiene el json que envio el cliente
    codigo_barras = request.json['codigo_barras']
    nombre = request.json['nombre']
    presentacion = request.json['presentacion']
    laboratorio = request.json['laboratorio']
    concentracion = request.json['concentracion']
    lote = request.json['lote']
    stock = request.json['stock']
    fecha_vencimiento = request.json['fecha_vencimiento']
    
    new_farmacos=Farmacos(codigo_barras,nombre,presentacion,laboratorio,concentracion,lote,stock,fecha_vencimiento)
    db.session.add(new_farmacos)
    db.session.commit()
    return farmacos_schema.jsonify(new_farmacos)

    

@app.route('/farmacos/<id>' ,methods=['PUT'])
def update_farmacos(id):
    farmacos=Farmacos.query.get(id)
 
    codigo_barras = request.json['codigo_barras']
    nombre = request.json['nombre']
    presentacion = request.json['presentacion']
    laboratorio = request.json['laboratorio']
    concentracion = request.json['concentracion']
    lote = request.json['lote']
    stock = request.json['stock']
    fecha_vencimiento = request.json['fecha_vencimiento']


    farmacos.codigo_barras = codigo_barras
    farmacos.nombre = nombre
    farmacos.presentacion = presentacion
    farmacos.laboratorio = laboratorio
    farmacos.concentracion = concentracion
    farmacos.lote = lote
    farmacos.stock = stock
    farmacos.fecha_vencimiento = fecha_vencimiento
    

    db.session.commit()
    return farmacos_schema.jsonify(farmacos)

