#Prueba3 Dreyco Román Valdenegro
import validaciones_prueba as vali
while True:
    vali.menu_movimiento()
    
    menu=vali.navegar_menu()
    if menu==1:#a medias
        vali.opc_1()
    elif menu==2:#sinterminr
        vali.opc_2()
    elif menu==3:#sinterminar
        vali.opc_3()
    else:#listo
        cerrar=vali.validacion_cerrar_todo()
        if cerrar==1:
            break
        else:
            print("Back")