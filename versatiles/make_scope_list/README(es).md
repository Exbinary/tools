# make_scope_list (version 2)
Esta herramienta hecha con python ha sido diseñada para crear una 'wordlist' que servira para utilidades que requieren de una lista (wordlist.txt), como herramientas de Fuerza Bruta (Hydra, wfuzz, etc...)

El objetivo es simplificar la lista de manera que cumpla con los rasgos del usuario 'victima' 

Por ejemplo, si ya sabes que el usuario victima es una mujer latinoamericana, es rentable probar antes que nada una lista que contenga solo nombres y apellidos de mujer latinoamericana.

### Uso
Ejecuta el script con python3.

El programa te pedira que eligas un modo (Mode).

Modo 1 - 'Scope'  te pedira que introduzcas datos sobre el usuario como Lenguaje y Genero. Luego el tamaño deseado de la lista resultante.

Mode 2 - 'Laser'  te pedira que introduzcas datos mas concretos del usuario como Nombre y Apellidos (si no conoces los apellidos te pedira que selecciones el lenguaje para hacer uso de la lista especifica en /data). 

Actualmente hay 4 opciones de lenguaje:

1 - UK english (Ingles de Gran Bretaña)

2 - US english (Ingles de EEUU)

3 - Spain spanish (Español de España)

4 - LATAM spanish (Español de LATAM)

Habiendo elegido cualquiera de los modos, el archivo resultante 'wordlist.txt' estara disponible en el mismo directorio de la herramienta.
________________

Puedes editar las listas de nombres y/o apellidos contempladas en /data.

La opcion de tamaño 'Extra' corta el archivo resultante a 1 millon y medio de palabras en la lista. Si quieres una lista mayor, puedes editar el script añadiendo un numero mayor (sobre la linea 172)

Tanto para listas en Ingles o Español, si no has conseguido resultados, recomiendo que uses la otra variante de idioma. (Ejemplo: Si elegiste LATAM, prueba de nuevo con España)
________________

________________

###### Considero esta herramienta como mi primer proyecto personal de programacion con python que es 'relevante'. Cualquier problema, duda, idea que surja sera un placer leerla.

###### Creado por Exbinary
