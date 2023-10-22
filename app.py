# waitress-serve --listen=127.0.0.1:8000 app:app
from apiwsgi import Wsgiclass
from jinja2 import Environment, FileSystemLoader
from webob import Request, Response
from whitenoise import WhiteNoise
import os
import mysql.connector
import datetime

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
env = Environment(loader=FileSystemLoader(template_dir))
    
app = Wsgiclass()

class Sesion:
    def __init__(self):
        self.acceso=False
    
    def validar_usuario(self,dni):
        try:
            conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
            cursor1=conexion1.cursor()
            query=f"select * from cliente where dni_cliente={dni};"
            cursor1.execute(query)
            self.datos = cursor1.fetchone()
            self.acceso=True
            conexion1.commit()
            print(self.datos)
        except Exception as e:
            print("Error MySQL:", str(e))
            self.datos=None
        finally:
            cursor1.close()
            conexion1.close()
        return self.datos
       
class Carrito:
    def __init__(self):
        self.articulos=[]
    
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
            return total
    
    def registrar_compra(self,medio_pago,total_venta,fecha):
        try:
            conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
            cursor1=conexion1.cursor()
            query=f"INSERT INTO `bd_practica`.`venta` (`fecha_venta`, `total_venta`, `medio_pago_venta`) VALUES ('{fecha}', '{total_venta}', '{medio_pago}');"
            cursor1.execute(query)
            conexion1.commit()
        except Exception as e:
            print("Error MySQL:", str(e))
        
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

def categorias(request, response, env):
    try:
        conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
        cursor1=conexion1.cursor()
        cursor1.execute("SELECT * FROM categoria;")
        datos=[]
        for x in cursor1:
            datos.append(x)
        env.globals["categorias"]=datos
        cursor1.close()
        conexion1.close()
    except Exception as e:
        print("Error MySQL:", str(e))

def marcas(request, response, env):
    try:
        conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
        cursor1=conexion1.cursor()
        cursor1.execute("SELECT * FROM marcas;")
        datos=[]
        for x in cursor1:
            datos.append(x)
        env.globals["marcas"]=datos
        cursor1.close()
        conexion1.close()
    except Exception as e:
        print("Error MySQL:", str(e))

def medios_de_pago(request, response, env):
    try:
        conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
        cursor1=conexion1.cursor()
        cursor1.execute("SELECT * FROM medio_pago;")
        datos=[]
        for x in cursor1:
            datos.append(x)
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

@app.ruta("/")
def inicio(request, response):
    categorias(request, response, env)
    marcas(request, response, env)
    productos_carrito(request, response, env)
    contador_carrito(request,response,env)
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
    

@app.ruta('/validar_inicio', methods=['GET'])
def validar_inicio(request,response):
    categorias(request, response, env)
    marcas(request, response, env)
    contador_carrito(request,response,env)
    productos_carrito(request, response, env)
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
        try:
            conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
            cursor1=conexion1.cursor()
            cursor1.execute("select codigo,nombre,precio,img_producto,tipo_descuento from producto inner join descuento on descuento_producto=id_descuento;")
            tabla=[]
            for x in cursor1:
                tabla.append(x)
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
        try:
            conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
            cursor1=conexion1.cursor()
            cursor1.execute("select * from sucursal;")
            tabla=[]
            for x in cursor1:
                tabla.append(x)
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
        try:
            conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
            cursor1=conexion1.cursor()
            cursor1.execute("SELECT codigo,nombre,precio,img_producto FROM producto;")
            tabla=[]
            for x in cursor1:
                tabla.append(x)
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
        id_categoria=request.GET.get('id_categoria')
        try:
            conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
            cursor1=conexion1.cursor()
            query=f'SELECT codigo,nombre,precio,img_producto FROM producto where categoria_producto={id_categoria};'
            cursor1.execute(query)
            tabla=[]
            for x in cursor1:
                tabla.append(x)
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
        id_marca=request.GET.get('id_marca')
        try:
            conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
            cursor1=conexion1.cursor()
            query=f'SELECT codigo,nombre,precio,img_producto FROM producto where marca={id_marca};'
            cursor1.execute(query)
            tabla=[]
            for x in cursor1:
                tabla.append(x)
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
        categorias(request, response, env)
        marcas(request, response, env)
        contador_carrito(request,response,env)
        productos_carrito(request, response, env)
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
        categorias(request, response, env)
        marcas(request, response, env)
        contador_carrito(request,response,env)
        productos_carrito(request, response, env)
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
        buscar=request.GET.get('palabra_busqueda')
        try:
            conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
            cursor1=conexion1.cursor()
            query=f"SELECT codigo,nombre,precio,img_producto FROM producto where nombre like '%{buscar}%' or marca like '%{buscar}%';"
            cursor1.execute(query)
            tabla=[]
            for x in cursor1:
                tabla.append(x)
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
        lista={}
        articulos=mi_carrito.mostrar_productos()
        if articulos!=0:
            try:
                conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="bd_practica")
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