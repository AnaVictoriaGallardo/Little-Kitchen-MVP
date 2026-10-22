#Creación de inventario base de ingredientes
inventario = [{
    'Ingrediente': 'arroz',
    'Clasificación': 'despensa seca',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{
    'Ingrediente': 'aceite',
    'Clasificación': 'despensa seca',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{   'Ingrediente': 'pasta',
    'Clasificación': 'despensa seca',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{   'Ingrediente': 'harina',
    'Clasificación': 'despensa seca',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{ 'Ingrediente': 'vinagre',
    'Clasificación': 'despensa seca',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{ 'Ingrediente': 'sal',
    'Clasificación': 'despensa seca',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{ 'Ingrediente': 'azucar',
    'Clasificación': 'despensa seca',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{ 'Ingrediente': 'atún en lata',
    'Clasificación': 'despensa seca',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{'Ingrediente': 'huevo',
    'Clasificación': 'frescos y refrigerados',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{'Ingrediente': 'cebolla',
    'Clasificación': 'frescos y refrigerados',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{'Ingrediente': 'ajo',
    'Clasificación': 'frescos y refrigerados',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{'Ingrediente': 'tomate',
    'Clasificación': 'frescos y refrigerados',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{'Ingrediente': 'leche',
    'Clasificación': 'frescos y refrigerados',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{'Ingrediente': 'manteca',
    'Clasificación': 'frescos y refrigerados',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{'Ingrediente': 'pimienta negra',
    'Clasificación': 'condimentos y especias',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{'Ingrediente': 'orégano',
    'Clasificación': 'condimentos y especias',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
},
{'Ingrediente': 'pimentón',
    'Clasificación': 'condimentos y especias',
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida': input('Ingrese Kg/Lts/Unidad: ')
}]

#Función para agregar ingredientes sin repetirlos
def agregar_ingrediente (inventario):
    nuevo_ingrediente = {
    'Ingrediente': input('Ingrese el nuevo ingrediente: '),
    'Clasificación': input('Ingrese despensa seca / frescos y refrigerados / condimentos y especias: '),
    'Cantidad': float(input('Ingrese la cantidad poseída: ')),
    'Unidad de medida' : input('Ingrese Kg/Lts/Unidad'),
    }
    coincidencias = any(i['Ingrediente'].lower() == nuevo_ingrediente['Ingrediente'].lower() for i in inventario )
    if coincidencias :
        print('Este ingrediente ya existe en el inventario')
    else:
        inventario.append(nuevo_ingrediente)
        print('Ingrediente agregado correctamente al inventario')
        for indice, item in enumerate(inventario,1):
            if item['Cantidad'] > 0:
                print(f"Los ingredientes disponibles son: \n {indice}-{item['Ingrediente']}")













