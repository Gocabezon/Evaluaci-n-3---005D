import json



URL_Bibliotecas = "biblioteca.json"

def leerArchivo(url):
    try:
        with open(url, "r") as archivo:

            return json.load(archivo)
    except:
        return []
    

    
def agregarAutor (url):
    archivo= leerArchivo(url)
    
    nombreNuevo = input("Ingrese nombre de nuevo autor")
    nacionalidadNueva= input("Ingrese nacionalidad")
    autorNuevo = {
            "AutorID": int(len(archivo["Autor"])+1),
            "Nombre": nombreNuevo,
            "Nacionalidad": nacionalidadNueva
        }
    
    archivo["Autor"].append(autorNuevo)
    with open(url, "w") as archivoJson:
        json.dump(archivo, archivoJson)
    return print("Autor agregado")

def buscaAutor (url):
    archivo = leerArchivo(url)
    buscarID = input("Ingrese ID a buscar")
    encontraID= False
    contador =int(0)
    for i in archivo["Autor"]:
        
        if archivo["Autor"][contador]["AutorID"] == buscarID:
            encontraID=True
            print("found")
            break
    
        contador +=1  

    if encontraID == True:
        return print("Encontrado")
    else:
        return print("No encontrado")


def editarAutor (url):
    archivo = leerArchivo(url)
    buscarID = input("Ingrese ID a buscar")
    encontraID= False
    contador =int(0)
    for i in archivo["Autor"]:
        
        if archivo["Autor"][contador]["AutorID"] == buscarID:
            encontraID=True
            print("found")
            break
    
        contador +=1  

    if encontraID == True:
        print("ingrese nuevos valores de nombre y nacionalidad")
        nuevoNombre = input("Ingrese nombre")
        nuevoNacionalidad = input("ingrese nacionalidad")
        archivo["autor"][contador]={
            "AutorID": buscarID,
            "Nombre": nuevoNombre,
            "Nacionalidad": nuevoNacionalidad
        }
        with open(url, "w") as archivoJson:
            json.dump(archivo, archivoJson)
            return print("Autor editado")



    else:
        return print("No encontrado")
    

def eliminarAutor (url):
    archivo = leerArchivo(url)
    buscarID = input("Ingrese ID a buscar")
    encontraID= False
    contador =int(0)
    for i in archivo["Autor"]:
        
        if archivo["Autor"][contador]["AutorID"] == buscarID:
            encontraID=True
            print("found")
            break
    
        contador +=1  

    if encontraID == True:
        eliminar= input("Autor encontrado, ¿Esta seguro de eliminar este autor? (Si/No)")
        if eliminar == "Si":
            archivo.remove(buscarID)
            with open(url, "w") as archivoJson:
                json.dump(archivo, archivoJson)
                return print("Autor borrado")


    else:
        return print("No encontrado")







    


    


    
