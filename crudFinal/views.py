import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime

def barra(request):
    
    # Realiza una solicitud GET para obtener los datos de la API
    response = requests.get('http://127.0.0.1:8001/Api/select/')

    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
            # La solicitud fue exitosa, obtener los datos
            data = response.json()


            return render(request,"barra.html",{"data":data[1],"total":data[0],"contador":data[2]})
    else:
            # La solicitud no fue exitosa, manejar el error
          return JsonResponse({'error': 'No se pudo obtener los datos de la API'}, status=500)

def select(request):
     # Realizar una solicitud GET para obtener los datos de la API
    response = requests.get('http://127.0.0.1:8001/Api/select/')
    
    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        # La solicitud fue exitosa, obtener los datos
        data = response.json()

        return JsonResponse(data,safe=False)
    else:
        # La solicitud no fue exitosa, manejar el error
        return JsonResponse({'error': 'No se pudo obtener los datos de la API'}, status=500)
    
def insert(request):
     if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        valor = request.POST.get('valor')
        fecha = request.POST.get('fecha')
        fechar = datetime.strptime(fecha, '%Y-%m-%d').strftime('%Y-%m-%d')
        categoria = request.POST.get('categoria')

        # Crea un diccionario con los datos del formulario
        objecto = {
            'nombre': nombre,
            'descripcion': descripcion,
            'valor': valor,
            'fecha': fechar,
            'categoria': categoria
        }

        # Realizar una solicitud POST para crear un nuevo registro en la API
        response = requests.post('http://127.0.0.1:8001/Api/insert/', data=objecto)
        
        # Verificar el código de estado de la respuesta
        if response.status_code == 200:
            # La creación fue exitosa
            # return JsonResponse({'success': 'Registro creado correctamente'})
            return redirect('/')
        else:
            # La creación no fue exitosa, manejar el error
            return JsonResponse({'error': 'No se pudo crear el registro en la API'}, status=500)
     else:
      return JsonResponse({'error': 'Solicitud no válida'}, status=400)
      # Si la solicitud no es POST, retornar un error
         


def delete(request):
     if request.method == 'POST':
        # Obtener los datos del formulario
        id = request.POST.get('id')

         # Crea un diccionario con los datos del formulario
        payload = {
            'id': id,
        }

        
        # Realizar una solicitud POST para crear un nuevo registro en la API
        response = requests.post('http://127.0.0.1:8001/Api/delete/', data=payload)
        
        # Verificar el código de estado de la respuesta
        if response.status_code == 200:
            # La creación fue exitosa
            # return JsonResponse({'success': 'Registro creado correctamente'})
            return redirect('/')
        else:
            # La creación no fue exitosa, manejar el error
            return JsonResponse({'error': 'No se pudo eliminar el registro en la API'}, status=500)
     else:
      return JsonResponse({'error': 'Solicitud no válida'}, status=400)
      # Si la solicitud no es POST, retornar un error


def actualizar_gasto(request, gasto_id):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        valor = request.POST.get('valor')
        fecha = request.POST.get('fecha')
        fechar = datetime.strptime(fecha, '%Y-%m-%d').strftime('%Y-%m-%d')
        categoria = request.POST.get('categoria')

        # Crea un diccionario con los datos del formulario
        datos_gasto = {
            'nombre': nombre,
            'descripcion': descripcion,
            'valor': valor,
            'fecha': fechar,
            'categoria': categoria
        }

        # Realizar una solicitud POST para actualizar un registro en la API
        response = requests.post('http://127.0.0.1:8001/Api/update/', data=datos_gasto)
        
   # Realizar una solicitud a la API para obtener los detalles del gasto
    response = requests.get(f'http://127.0.0.1:8001/Api/detalle/{gasto_id}/')
    if response.status_code == 200:
        detalle_gasto = response.json()
        # Pasar los detalles del gasto al contexto de la plantilla
        return render(request, 'actualizar.html', {'detalle_gasto': detalle_gasto})
    else:
        # Manejar el caso en el que no se puedan obtener los detalles del gasto
        return JsonResponse({'error': 'No se pudieron obtener los detalles del gasto'}, status=500)
    




#otra seccion




# def actualizar_gasto(request, gasto_id):
#     if request.method == 'POST':
#         # Obtener datos del formulario
#         nombre = request.POST.get('nombre')
#         descripcion = request.POST.get('descripcion')
#         valor = request.POST.get('valor')
#         fecha = request.POST.get('fecha')
#         categoria = request.POST.get('categoria')

#         # Crear un diccionario con los datos del formulario
#         datos_gasto = {
#             'id': gasto_id,
#             'nombre': nombre,
#             'descripcion': descripcion,
#             'valor': valor,
#             'fecha': fecha,
#             'categoria': categoria
#         }

#         # Enviar la solicitud POST a la API para actualizar el gasto
#         response = requests.post('http://127.0.0.1:8001/Api/update/', data=datos_gasto)

#         if response.status_code == 200:
#             # Redirigir a alguna vista de éxito o a la página principal
#             return redirect('/')
#         else:
#             # Manejar el error si la actualización falla
#             return JsonResponse({'error': 'No se pudo actualizar el gasto en la API'}, status=500)

#     else:
#         # Si la solicitud es GET, obtener los detalles del gasto para mostrar el formulario de actualización
#         response = requests.get(f'http://127.0.0.1:8001/Api/detalle/{gasto_id}/')
#         if response.status_code == 200:
#             detalle_gasto = response.json()
#             return render(request, 'actualizar.html', {'detalle_gasto': detalle_gasto})
#         else:
#             return JsonResponse({'error': 'No se pudieron obtener los detalles del gasto'}, status=500)
