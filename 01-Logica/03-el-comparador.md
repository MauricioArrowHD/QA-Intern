# El comparador

Martín está aprendiendo a programar y su maestra le pidió escribir un programa que compare pares de números. Para cada par, el programa debe indicar si el primer número es menor, mayor o igual que el segundo. Martín sabe que parece sencillo, pero quiere asegurarse de que funcione con números negativos y con muchos casos de prueba.

## Entrada

Cada línea contiene dos enteros `a` y `b`, cuyo valor absoluto es menor que 1 000 000 001. La entrada termina con el fin de archivo (EOF).

## Salida

Para cada caso de prueba imprime en una línea uno de los siguientes símbolos:

- `<` si `a` es menor que `b`
- `>` si `a` es mayor que `b`
- `=` si `a` es igual a `b`

## Ejemplo de entrada

```
10 20
20 10
-5 -5
-7 3
```

## Ejemplo de salida

```
<
>
=
<
```
