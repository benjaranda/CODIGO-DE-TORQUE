
#IMPORTACION DE LIBRERIAS
import math as m

#DESCRIPCION DE MODO DE USO
print('CALCULADORA de TORQUE\n\n')
print('PARA calcular torque, escribir T(R,r,h,e,mu,omega,tipo)\n')
print('Donde tipo puede ser:\n')
print('A: Cono invertido\n')
print('B: Semiesfera\n')
print('C: Cilindro')

#DEF DE FUNCION
def T(R,r,h,e,mu,omega,tipo):
    #EVALUACION DE CASOS
    #CONO
    if (tipo == "A"):
        t = ((m.pi*mu*omega*(2*m.pi/60))/(2*e))*((R**4)-(r**4)+(R**3)*m.sqrt((h**2)+(R**2)))
        torque = round(t,2) #Redondeo de 2 decimales
        return print('El torque para el cono invertido es: T =',torque,'[Nm]')
    #SEMIESFERA
    elif (tipo == "B"):
        t = ((m.pi*mu*omega*(2*m.pi/60))/(2*e))*((11/3)*(R**4)-(r**4))
        torque = round(t,2) #Redondeo de 2 decimales
        return print('El torque para la semiesfera es: T =',torque,'[Nm]')
    #CILINDRO
    elif (tipo == "C"):
        t = ((m.pi*mu*omega*(2*m.pi/60))/(2*e))*(2*(R**4)-(r**4)+4*(R**3)*h)
        torque = round(t,2) #Redondeo de 2 decimales
        return print('El torque para el cilindro es: T =',torque,'[Nm]')
