"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas....
"""
data=open('D:/Users/lacevedog/OneDrive - Linea Directa S.A.S/Escritorio/data.csv','r')
data=[z.replace("\n", "") for z in data]
data=[z.split("\t") for z in data]


def pregunta_01():
    columna2=[int(z[1])for z in data]
    return sum(columna2)


def pregunta_02():
    columna1=[k[0] for k in data]
    lista=[]
    for i in sorted(list(set(columna1))):
        lista.append((i,columna1.count(i)))
    return lista


def pregunta_03():
    columna1=[k[0] for k in data]
    lista1=[]
    for i in sorted(list(set(columna1))):
        filtrado=[z for z in data if z[0]==i]
        columna2f=[int(w[1]) for w in filtrado]
        lista1.append((i, sum(columna2f)))
    return lista1


data = [z + [z[2].split("-")[1]] for z in data]
def pregunta_04():
    columnam=[k[5] for k in data]
    lista2=[]
    for i in sorted(list(set(columnam))):
        lista2.append((i,columnam.count(i)))
    return lista2

def pregunta_05():
    columna1=[k[0] for k in data]
    lista3=[]
    for i in sorted(list(set(columna1))):
        filtrado=[z for z in data if z[0]==i]
        columna2f=[int(w[1]) for w in filtrado]
        lista3.append((i, max(columna2f),min(columna2f)))  
    return lista3


def pregunta_06():
    lista4=[]
    columna5sep=[z[4].split(",") for z in data]
    columna5uni=columna5sep[0]
    for i in range(len(columna5sep)-1):
          columna5uni+=columna5sep[i+1]
    set_keys=sorted(list(set([j[:3] for j in columna5uni])))
    for k in set_keys: 
        listavalues=[int(w[4:]) for w in columna5uni if w[:3]==k]
        lista4.append((k,min(listavalues),max(listavalues)))

    return lista4


def pregunta_07():
    lista5=[]
    columna2=[int(z[1])for z in data]
    for i in sorted(list(set(columna2))):
        filtradocol=[z for z in data if z[1]==str(i)]
        columna1f=[w[0] for w in filtradocol]
        lista5.append((i,columna1f))
    return lista5


def pregunta_08():
    lista6=[]
    columna2=[int(z[1])for z in data]
    for i in sorted(list(set(columna2))):
        filtradocol=[z for z in data if z[1]==str(i)]
        columna1f=[w[0] for w in filtradocol]
        lista6.append((i,sorted(list(set(columna1f)))))
    return lista6

def pregunta_09():
    dictionary={}
    columna5sep=[z[4].split(",") for z in data]
    columna5uni=columna5sep[0]
    for i in range(len(columna5sep)-1):
          columna5uni+=columna5sep[i+1]
    set_keys=sorted(list(set([j[:3] for j in columna5uni])))
    for k in set_keys: 
        listavalues=[int(w[4:]) for w in columna5uni if w[:3]==k]
        dictionary[k]=len(listavalues)

    return dictionary

def pregunta_10():
    lista7=[]
    columna1=[z[0] for z in data]
    columna4=[z[3].split(",") for z in data]
    columna5=[z[4].split(",") for z in data]
    for i in range(len(columna1)):
        lista7.append((columna1[i],len(columna4[i]),len(columna5[i])))
    return lista7


def pregunta_11():
    dictionary1={}
    columna4=[z[3].split(",") for z in data]
    columna2=[int(z[1]) for z in data]
    columna4uni=columna4[0]
    for i in range(len(columna2)-1):
          columna4uni+=columna4[i+1]
    for j in sorted(list(set(columna4uni))):
        filtradocol4=[z for z in data if j in z[3]]
        columna2f=[int(z[1]) for z in filtradocol4]
        dictionary1[j]=sum(columna2f)

    return dictionary1


def pregunta_12():
    dictionary2={}
    columna1= [k[0] for k in data]
    for j in sorted(list(set(columna1))):
        filtradocol1=[z for z in data if z[0]==j]
        columna5sep=[z[4].split(",") for z in filtradocol1]
        columna5uni=columna5sep[0]
        for i in range(len(columna5sep)-1):
           columna5uni+=columna5sep[i+1]
        listavalues=[int(w[4:]) for w in columna5uni]
        dictionary2[j]=sum(listavalues)

    return dictionary2
