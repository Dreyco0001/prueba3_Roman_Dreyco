#nro de validacines ¿? indeterminado de momento
import time as tp


import numpy
modulos_mascotas = numpy.empty((2,5),object)
modulos_mascotas.fill("🟨")
ruts=[]
nombres=[]
identificador_unic=[]
nombre_mascota=[]
cant_dias=[]
bloque_X_mascota=[]
bloque_y_mascota=[]

bloque_X=[2,1]
bloque_y=[1,2,3,4,5]

menu=0
valor_dia=15000

def menu_movimiento():
    print('''
    \t menu
    1)_Grabar
    2)_Buscar
    3)_Retirarse
    4)_salir

    Para navegar en el menu 
   

    ''')
    
def navegar_menu():
    while True:
        try:
            menu=int(input("ingrese nro de opcion_ "))
            if menu in(1,2,3,4):
                return menu
            else:
                print("ERROR ingrese (1,2,3,4)")
        except:
            print("ERROR solo nro enteros")

#grabar
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
def validar_nombre_mascota():
    while True:
        nombre_mascota12 = input("Ingrese nombre mascota: ")
        if len(nombre_mascota12.strip()) >= 3 and nombre_mascota12.isalpha():
            return nombre_mascota12
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
def codigo_automatico():
    codigo_automatico01=1
    print("creando codigo de validacion automatico")
    print(f"codigo unico es:_{codigo_automatico01}")

    if codigo_automatico01 <10:
        codigo_automatico01+=1    
        return codigo_automatico01
    elif codigo_automatico01>=10:
        #no se cargan mas datos
        print(f"ultimo codigo disponible {codigo_automatico01}")
        return codigo_automatico01 
def cantidad_dias():
    while True:
        print("cuantos dias se va a quedar")
        print("dias maximos 30 y minimos 1")
        try:
            dias=int(input("Ingrese nro de días_"))
            if dias>=1 and dias<=30:
                return dias
            else:
                print("ERROR de datos ingrese nro validos")
        except:
            print("ERROR de datos solo nro enteros")
def mostrar_modulos_disponibles():
    contador=2
    for x in range(2):#filas
        print(f"Bloque X {contador}\t|", end=" ")
        for y in range(5):#columnas
            print(modulos_mascotas[x][y], end=" ")
        print()
        print("bloque y           1   2   3   4   5")
        contador -= 1
    tp.sleep(4)
def seleccionebloqueX():
    bloque_X1=int(input("ingrese nro de altura deseado_"))
    if bloque_X1 in bloque_X:
        posicionX=bloque_X.index(bloque_X1)
        bloque_X.append(posicionX)
        return posicionX
def seleccionebloqueY():
    bloque_y1=int(input("ingrese nro de columna deseado_"))
    if bloque_y1 in bloque_y:
        posicionY=bloque_y.index(bloque_y1)
        bloque_y.append(posicionY)
        return posicionY
    

def opc_1():
    rut=validar_rut()
    nombre=validar_nombre()
    nombre_mascota12=validar_nombre_mascota()
    codigo_unico=codigo_automatico()
    dias=cantidad_dias()
    mostrar_modulos_disponibles()
    posicionX=seleccionebloqueX()
    posicionY=seleccionebloqueY()
    ruts.append(rut)
    nombres.append(nombre)
    identificador_unic.append(codigo_unico)
    nombre_mascota.append(nombre_mascota12)
    cant_dias.append(dias)
    bloque_X_mascota.append(posicionX)
    bloque_y_mascota.append(posicionY)
    modulos_mascotas[posicionX][posicionY]="⬜"
    mostrar_modulos_disponibles()
    print("datos ingresados")



#-------------------------------------------------------
#opc2
def validar_rut2():
    rut=int(input("ingrese rut deseado_"))
    if rut in ruts:
        posicion=ruts.index(rut)
        ruts.append(posicion)
        return posicion
def rescatando_datos():
    print("recibiendo datos")
    
def opc_2():
    posicion=validar_rut2()
    mostrar_modulos_disponibles()
    mascota=nombre_mascota[posicion]
    altura=bloque_X_mascota[posicion]
    columna=bloque_y_mascota[posicion]
    altura+=1
    print(f"altura: {altura} y columna {columna+1}")
    print(f"nombre de mascota: {mascota}")
    tp.sleep(3)
#------------------------------------------------------



def opc_3():
    rut=validar_rut()
    if rut in ruts:
        posicion=ruts.index(rut)
        ruts.append(posicion)
        calculo=valor_dia*cant_dias[posicion]
        
        while True:
            try:
                print("Desea pagar? (si=1/no=2)")
                pagar=int(input(":_"))
                if pagar in(1,2):
                    break
                else:
                    print("numero no valido")
            except:
                print("ERROR solo numeros enteros")  
        if pagar==1:
            while True:
                print(f"Su total a pagar es de: ${calculo} precio del día es: ${valor_dia}")
                try:
                    print("ingrese monto")
                    pago=int(input(":_"))
                    if pago>=calculo:
                        break
                    else:
                        print("numero no valido")
                except:
                    print("ERROR solo numeros enteros") 
            if pago == calculo:
                print("suma justa gracias")
            elif pago > calculo:
                print("calculando vuelto")
                vuelto=pago-calculo
                print(f"su vuelto es de ${vuelto}")
            posicionXX=bloque_X_mascota[posicion]
            posicionYY=bloque_y_mascota[posicion]
            modulos_mascotas[posicionXX][posicionYY]="🟨"
            ruts.pop(posicion)
            nombres.pop(posicion)
            identificador_unic.pop(posicion)
            nombre_mascota.pop(posicion)
            cant_dias.pop(posicion)
            bloque_X_mascota.pop(posicion)
            bloque_y_mascota.pop(posicion)
            print("terminando proceso")
            mostrar_modulos_disponibles()
            tp.sleep(3)
        elif pagar==2:
            print("Regresando")
            tp.sleep(3)
    else:
        print("Regresando")
        tp.sleep(3)



def validacion_cerrar_todo():
    while True:
        try:
            print("Desea cerrar ejercicio? (si=1/no=2)")
            cerrar=int(input(":_"))
            if cerrar in(1,2):
                return cerrar
            else:
                print("numero no valido")
        except:
            print("ERROR solo numeros enteros")    
    
    
