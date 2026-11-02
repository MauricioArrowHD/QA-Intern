# El validador de llaves

Sofía trabaja en el equipo de QA y está revisando archivos de configuración generados automáticamente. Varias veces el generador ha dejado paréntesis, corchetes o llaves sin cerrar, o cerrados en el orden equivocado, y eso rompe el despliegue. Antes de reportar el bug quiere un programa que le diga qué líneas están mal.

Una línea es válida si cada símbolo de apertura `(`, `[` o `{` se cierra con su símbolo correspondiente `)`, `]` o `}`, y en el orden correcto: el último símbolo que se abrió debe ser el primero en cerrarse.

## Entrada

Cada línea contiene una cadena formada únicamente por los caracteres `(`, `)`, `[`, `]`, `{` y `}`, con una longitud entre 1 y 100 000. La entrada termina con el fin de archivo (EOF).

## Salida

Para cada línea imprime `Si` si la cadena es válida o `No` si no lo es.

## Ejemplo de entrada

```
([]{})
([)]
((
{[()()]}
)(
```

## Ejemplo de salida

```
Si
No
No
Si
No
```
