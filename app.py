# waitress-serve --listen=127.0.0.1:8000 app:app
from apiwsgi import Wsgiclass
from jinja2 import Environment, FileSystemLoader
from webob import Request, Response
from whitenoise import WhiteNoise
import os
import mysql.connector
import datetime
import random

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
env = Environment(loader=FileSystemLoader(template_dir))

def conexion_db():
    conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
    return conexion1

app = Wsgiclass()

class Sesion:
    def __init__(self):
        self.acceso=False
        self.administrador=False
    
    def validar_usuario(self,dni):
        try:
            conexion1=conexion_db()
            cursor1=conexion1.cursor()
            query=f"select * from cliente where dni_cliente={dni};"
            cursor1.execute(query)
            self.datos = cursor1.fetchone()
            if self.datos!=None:
                self.acceso=True
                self.id_usuario=self.datos[0]
                query=f"select privilegios from cliente where dni_cliente={dni};"
                cursor1.execute(query)
                privilegio_cliente=cursor1.fetchone()
                if privilegio_cliente[0]==1:
                    self.administrador=True
            conexion1.commit()
            print(self.datos)
        except Exception as e:
            print("Error MySQL:", str(e))
            self.datos=None
        finally:
            cursor1.close()
            conexion1.close()
        return self.datos
    
    def registro_nuevo(self,nombre,apellido,calle,ncalle,dni,correo,telefono):
        try:
            conexion1=conexion_db()
            cursor1=conexion1.cursor()
            query=f"INSERT INTO `bd_practica`.`cliente` (`nom_cliente`, `ap_cliente`, `calle_cliente`, `ncalle_cliente`, `dni_cliente`, `correo_cliente`, `telefono_cliente`) VALUES ('{nombre}', '{apellido}', '{calle}', '{ncalle}', '{dni}', '{correo}', '{telefono}');"
            cursor1.execute(query)
            conexion1.commit()
            self.validar_usuario(dni)
        except Exception as e:
            print("Error MySQL:", str(e))
        finally:
            cursor1.close()
            conexion1.close()
        
    def modificar_datos_usuario(self,nombre,apellido,calle,ncalle,dni,correo,telefono):
        nombre=nombre.title()
        apellido=apellido.title()
        calle=calle.title()
        try:
            conexion1=conexion_db()
            cursor1=conexion1.cursor()
            query=f"UPDATE `cliente` SET `nom_cliente` = '{nombre}',`ap_cliente` = '{apellido}',`calle_cliente` = '{calle}',`ncalle_cliente` = '{ncalle}',`dni_cliente` = '{dni}',`correo_cliente` = '{correo}',`telefono_cliente` = '{telefono}'WHERE (`id_cliente` = '{self.id_usuario}');"
            cursor1.execute(query)
            conexion1.commit()
            query=f"select * from cliente where id_cliente={self.id_usuario};"
            cursor1.execute(query)
            self.datos = cursor1.fetchone()
            print(self.datos)
        except Exception as e:
            print("Error MySQL:", str(e))
        finally:
            cursor1.close()
            conexion1.close()
    
    def historial_usuario(self):
        try:
            conexion1=conexion_db()
            cursor1=conexion1.cursor()
            query=f"select codigo_producto,codigo_pedido,nombre,cantidad_producto,precio_producto,estado_pedido,fecha_venta,total_venta from detalle_pedido inner join pedido on id_pedido=codigo_pedido inner join producto on codigo=codigo_producto inner join venta on num_factura=num_factura_pedido where pedido.cliente_pedido={self.id_usuario};"
            cursor1.execute(query)
            prueba=cursor1.fetchall()
            self.historial=[]
            pedido_act=None
            articulos_pedido=[]
            for x in prueba:
                if pedido_act==None:
                    pedido_act=x[1]
                if x[1]==pedido_act:
                    articulos_pedido.append(x)
                else:
                    self.historial.append(articulos_pedido)
                    articulos_pedido=[x]
                    pedido_act=x[1]
            if articulos_pedido:
                self.historial.append(articulos_pedido)
            conexion1.commit()
        except Exception as e:
            print("Error MySQL:", str(e))
        finally:
            cursor1.close()
            conexion1.close()
        
    def cerrar_sesion(self):
        self.acceso=False
        self.administrador=False
        
class Carrito:
    def __init__(self):
        self.articulos=[]
        self.sucursal=None
    
    def agregar_producto(self,id_producto,cantidad,precio):
        total_prod=cantidad*precio
        for x in self.articulos:
            if id_producto==x[0]:
                x[1]+=cantidad
                x[3]=x[1]*x[2]
                break
        else:
            producto = [id_producto, cantidad, precio, total_prod]
            self.articulos.append(producto)
    
    def eliminar_producto(self,id_producto):
        for x in self.articulos:
            if x[0]==id_producto:
                self.articulos.remove(x)
                break
    
    def mostrar_productos(self):
        if not self.articulos:
            return 0
        else:
            return self.articulos

    def calcular_total(self):
        if not self.articulos:
            return 0
        else:
            total=0
            for x in self.articulos:
                total+=(x[1]*x[2])
                total=round(total,2)
            return total
    
    def registrar_compra(self,medio_pago,total_venta,fecha):
        try:
            conexion1=conexion_db()
            cursor1=conexion1.cursor()
            query=f"INSERT INTO `bd_practica`.`venta` (`fecha_venta`, `total_venta`, `medio_pago_venta`) VALUES ('{fecha}', '{total_venta}', '{medio_pago}');"
            cursor1.execute(query)
            conexion1.commit()
            self.id_venta=cursor1.lastrowid
            if self.sucursal is None:
                lista=[1,2,3]
                self.sucursal=random.choice(lista)
            query=f"INSERT INTO `bd_practica`.`pedido` (`estado_pedido`, `cliente_pedido`, `num_factura_pedido`, `sucursal_pedido`) VALUES ('en proceso', '{usuario.id_usuario}', '{self.id_venta}', '{self.sucursal}');"
            cursor1.execute(query)
            conexion1.commit()
            self.id_pedido=cursor1.lastrowid
            for x in self.articulos:
                query=f"INSERT INTO `bd_practica`.`detalle_pedido` (`codigo_producto`, `codigo_pedido`, `cantidad_producto`, `precio_producto`) VALUES ('{x[0]}', '{self.id_pedido}', '{x[1]}', '{x[2]}');"
                cursor1.execute(query)
                conexion1.commit()
            self.articulos=[]
        except Exception as e:
            print("Error MySQL:", str(e))
        finally:
            cursor1.close()
            conexion1.close()
        
mi_carrito=Carrito()
usuario=Sesion()

def ordenar_productos(tabla):
    contador=0
    db=[]
    columna=[]
    for x in tabla:
        if contador<3:
            columna.append(x)
            contador+=1
        else:
            db.append(columna)
            columna=[]
            columna.append(x)
            contador=1
    if columna:
        db.append(columna)
    return db

def rol_admin(request,response,env):
    if usuario.administrador==True:
        env.globals["administrador"]=1
    else:
        env.globals["administrador"]=0

def categorias(request, response, env):
    try:
        conexion1=conexion_db()
        cursor1=conexion1.cursor()
        cursor1.execute("SELECT * FROM categoria;")
        datos=cursor1.fetchall()
        env.globals["categorias"]=datos
        cursor1.close()
        conexion1.close()
    except Exception as e:
        print("Error MySQL:", str(e))

def marcas(request, response, env):
    try:
        conexion1=conexion_db()
        cursor1=conexion1.cursor()
        cursor1.execute("SELECT * FROM marcas;")
        datos=cursor1.fetchall()
        env.globals["marcas"]=datos
        cursor1.close()
        conexion1.close()
    except Exception as e:
        print("Error MySQL:", str(e))

def medios_de_pago(request, response, env):
    try:
        conexion1=conexion_db()
        cursor1=conexion1.cursor()
        cursor1.execute("SELECT * FROM medio_pago;")
        datos=cursor1.fetchall()
        env.globals["medios_de_pago"]=datos
        cursor1.close()
        conexion1.close()
    except Exception as e:
        print("Error MySQL:", str(e))

def contador_carrito(request, response, env):
    contador=mi_carrito.mostrar_productos()
    if contador==0:
        env.globals["contador"]=contador
    else:
        env.globals["contador"]=len(contador)
    
def productos_carrito(request, response, env):
    lista=mi_carrito.mostrar_productos()
    ids=[]
    if lista!=0:
        for x in lista:
            ids.append(int(x[0]))
        env.globals["botones"]=ids

#----INICIO SESION-------
@app.ruta("/")
def inicio(request, response):
    categorias(request, response, env)
    marcas(request, response, env)
    productos_carrito(request, response, env)
    contador_carrito(request,response,env)
    rol_admin(request,response,env)
    if usuario.acceso==False:
        template = env.get_template("sesion.html")
        rendered_html = template.render()
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/home'
        return response
# ----------VISTA ADMINISTRADOR-----------

@app.ruta("/prueba")
def inicio(request, response):
    categorias(request, response, env)
    marcas(request, response, env)
    productos_carrito(request, response, env)
    contador_carrito(request,response,env)
    rol_admin(request,response,env)
    if usuario.acceso==True and usuario.administrador==True:
        template = env.get_template("admin.html")
        rendered_html = template.render()
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/home'
        return response
   
# --------- VISTAS CLIENTE ---------------
@app.ruta("/registro")
def registro_usuario(request,response):
    categorias(request, response, env)
    marcas(request, response, env)
    productos_carrito(request, response, env)
    contador_carrito(request,response,env)
    if usuario.acceso==False:
        template = env.get_template("registro.html")
        rendered_html = template.render()
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/home'
        return response

@app.ruta("/proceso_registro",methods=['POST'])
def procesar_registro(request,response):
    nombre=request.POST.get('nombre')
    apellido=request.POST.get('apellido')
    calle=request.POST.get('calle')
    ncalle=request.POST.get('numcalle')
    dni=request.POST.get('dni')
    correo=request.POST.get('correo')
    telefono=request.POST.get('telefono')
    usuario.registro_nuevo(nombre,apellido,calle,ncalle,dni,correo,telefono)
    response=Response()
    response.status_code = 302
    response.headers['Location'] = '/home'
    return response

@app.ruta("/cuenta")
def cuenta(request,response):
    categorias(request, response, env)
    marcas(request, response, env)
    productos_carrito(request, response, env)
    contador_carrito(request,response,env)
    rol_admin(request,response,env)
    if usuario.acceso==True:
        template = env.get_template("usuario.html")
        db=usuario.datos
        rendered_html = template.render(db=db)
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta("/cerrar_sesion",methods=['POST'])
def cerrar_sesion_actual(request,response):
    if usuario.acceso==True:
        x=request.POST.get('cerrar_sesion')
        if x=="1":
            usuario.cerrar_sesion()
            response=Response()
            response.status_code = 302
            response.headers['Location'] = '/'
            return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta("/editar_usuario")
def cuenta(request,response):
    categorias(request, response, env)
    marcas(request, response, env)
    productos_carrito(request, response, env)
    contador_carrito(request,response,env)
    rol_admin(request,response,env)
    if usuario.acceso==True:
        template = env.get_template("editar_usuario.html")
        db=usuario.datos
        rendered_html = template.render(db=db)
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta('/confirmar_cambios', methods=['POST'])
def confirmar_cambios(request,response):
    if usuario.acceso==True:
        nombre=request.POST.get('nombre')
        apellido=request.POST.get('apellido')
        calle=request.POST.get('calle')
        ncalle=request.POST.get('numcalle')
        dni=request.POST.get('dni')
        correo=request.POST.get('correo')
        telefono=request.POST.get('telefono')
        usuario.modificar_datos_usuario(nombre,apellido,calle,ncalle,dni,correo,telefono)
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/cuenta'
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta("/historial_de_compras")
def historial_compras(request,response):
    categorias(request, response, env)
    marcas(request, response, env)
    productos_carrito(request, response, env)
    contador_carrito(request,response,env)
    rol_admin(request,response,env)
    if usuario.acceso==True:
        template = env.get_template("historial.html")
        usuario.historial_usuario()
        db=usuario.historial
        rendered_html = template.render(db=db)
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response
    

@app.ruta('/validar_inicio', methods=['GET'])
def validar_inicio(request,response):
    dni=request.GET.get('dni')
    user=usuario.validar_usuario(dni)
    if user:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/home'
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta("/home")
def inicio(request, response):
    if usuario.acceso==True:
        categorias(request, response, env)
        marcas(request, response, env)
        productos_carrito(request, response, env)
        contador_carrito(request,response,env)
        rol_admin(request,response,env)
        try:
            conexion1=conexion_db()
            cursor1=conexion1.cursor()
            cursor1.execute("select codigo,nombre,precio,img_producto,tipo_descuento from producto inner join descuento on descuento_producto=id_descuento;")
            tabla=cursor1.fetchall()
        except Exception as e:
            print("Error MySQL:", str(e))
        descuento=[]
        for x in tabla:
            x=list(x)
            desc=x[2]*(x[4]/100)
            desc=x[2]-desc
            x.append(desc)
            x=tuple(x)
            descuento.append(x)
        db=ordenar_productos(descuento)
        template = env.get_template("index.html")
        rendered_html = template.render(db=db)
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta('/sucursales')
def mostrar_sucursales(request,response):
    if usuario.acceso==True:
        categorias(request, response, env)
        marcas(request, response, env)
        contador_carrito(request,response,env)
        productos_carrito(request, response, env)
        rol_admin(request,response,env)
        try:
            conexion1=conexion_db()
            cursor1=conexion1.cursor()
            cursor1.execute("select * from sucursal;")
            tabla=cursor1.fetchall()
        except Exception as e:
            print("Error MySQL:", str(e))
        template = env.get_template("sucursal.html")
        rendered_html = template.render(db=tabla)
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta("/productos")
def productos(request, response):
    if usuario.acceso==True:
        productos_carrito(request, response, env)
        categorias(request, response, env)
        marcas(request, response, env)
        contador_carrito(request,response,env)
        rol_admin(request,response,env)
        try:
            conexion1=conexion_db()
            cursor1=conexion1.cursor()
            cursor1.execute("SELECT codigo,nombre,precio,img_producto FROM producto;")
            tabla=cursor1.fetchall()
        except Exception as e:
            print("Error MySQL:", str(e))
        db=ordenar_productos(tabla)
        template = env.get_template("productos.html")
        rendered_html = template.render(db=db)
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta('/categoria', methods=['GET'])
def filtro_categoria(request,response):
    if usuario.acceso==True:
        categorias(request, response, env)
        marcas(request, response, env)
        productos_carrito(request, response, env)
        contador_carrito(request,response,env)
        rol_admin(request,response,env)
        id_categoria=request.GET.get('id_categoria')
        try:
            conexion1=conexion_db()
            cursor1=conexion1.cursor()
            query=f'SELECT codigo,nombre,precio,img_producto FROM producto where categoria_producto={id_categoria};'
            cursor1.execute(query)
            tabla=cursor1.fetchall()
        except Exception as e:
            print("Error MySQL:", str(e))
        db=ordenar_productos(tabla)
        template = env.get_template("productos.html")
        rendered_html = template.render(db=db)
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta('/marca', methods=['GET'])
def filtro_marca(request,response):
    if usuario.acceso==True:
        categorias(request, response, env)
        marcas(request, response, env)
        contador_carrito(request,response,env)
        productos_carrito(request, response, env)
        rol_admin(request,response,env)
        id_marca=request.GET.get('id_marca')
        try:
            conexion1=conexion_db()
            cursor1=conexion1.cursor()
            query=f'SELECT codigo,nombre,precio,img_producto FROM producto where marca={id_marca};'
            cursor1.execute(query)
            tabla=cursor1.fetchall()
        except Exception as e:
            print("Error MySQL:", str(e))
        db=ordenar_productos(tabla)
        template = env.get_template("productos.html")
        rendered_html = template.render(db=db)
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta('/agregar_al_carrito', methods=['POST'])
def agregar_al_carrito(request,response):
    if usuario.acceso==True:
        id_producto = request.POST.get('id_producto')
        cantidad = int(request.POST.get('cantidad'))
        precio=float(request.POST.get('precio'))
        mi_carrito.agregar_producto(id_producto,cantidad,precio)
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/productos'
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta('/eliminar_del_carrito', methods=['POST'])
def eliminar_del_carrito(request,response):
    if usuario.acceso==True:
        id_producto = request.POST.get('id_producto')
        mi_carrito.eliminar_producto(id_producto)
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/carrito'
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta('/busqueda_producto',methods=['GET'])
def buscar_producto(request,response):
    if usuario.acceso==True:
        categorias(request, response, env)
        marcas(request, response, env)
        contador_carrito(request,response,env)
        productos_carrito(request, response, env)
        rol_admin(request,response,env)
        buscar=request.GET.get('palabra_busqueda')
        try:
            conexion1=conexion_db()
            cursor1=conexion1.cursor()
            query=f"SELECT codigo,nombre,precio,img_producto FROM producto where nombre like '%{buscar}%' or marca like '%{buscar}%';"
            cursor1.execute(query)
            tabla=cursor1.fetchall()
        except Exception as e:
            print("Error MySQL:", str(e))
        db=ordenar_productos(tabla)
        template = env.get_template("productos.html")
        rendered_html = template.render(db=db)
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta('/carrito')
def mostrar_lista_carrito(request,response):
    if usuario.acceso==True:
        categorias(request, response, env)
        marcas(request, response, env)
        contador_carrito(request,response,env)
        productos_carrito(request, response, env)
        medios_de_pago(request, response, env)
        rol_admin(request,response,env)
        lista={}
        articulos=mi_carrito.mostrar_productos()
        if articulos!=0:
            try:
                conexion1=conexion_db()
                cursor1=conexion1.cursor()
                for x in articulos:
                    query=f"SELECT nombre FROM producto where codigo={x[0]}"
                    cursor1.execute(query)
                    tabla=[]
                    for linea in cursor1:
                        tabla.append(linea)
                    for y in tabla:
                        for z in y:
                            x.append(z)
            except Exception as e:
                print("Error MySQL:", str(e))
        lista["articulos"]=articulos
        total=mi_carrito.calcular_total()
        lista["total"]=total
        template = env.get_template("carrito.html")
        rendered_html = template.render(lista=lista)
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response

@app.ruta('/confirmar_compra',methods=['GET'])
def confirmar_compra(request,response):
    if usuario.acceso==True:
        categorias(request, response, env)
        marcas(request, response, env)
        contador_carrito(request,response,env)
        productos_carrito(request, response, env)
        medios_de_pago(request, response, env)
        rol_admin(request,response,env)
        medio_pago=request.GET.get('medio_pago')
        fecha=datetime.datetime.now()
        total_venta=mi_carrito.calcular_total()
        mi_carrito.registrar_compra(medio_pago,total_venta,fecha)
        lista="funciona"
        template = env.get_template("pago.html")
        rendered_html = template.render(lista=lista)
        response=Response()
        response.text = rendered_html
        return response
    else:
        response=Response()
        response.status_code = 302
        response.headers['Location'] = '/'
        return response
    
app = WhiteNoise(app, root='static/')