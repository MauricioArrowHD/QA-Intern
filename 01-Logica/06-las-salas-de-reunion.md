# Las salas de reunión

La oficina de Valeria está creciendo y cada día hay más reuniones. Antes de rentar un piso nuevo, quiere saber cuántas salas de reunión necesita como mínimo para que ninguna reunión tenga que cambiar de horario.

Cada reunión tiene una hora de inicio y una de fin, en minutos desde que abre la oficina. Una reunión ocupa la sala desde su inicio hasta justo antes de su fin, así que si una reunión termina en el minuto 10 y otra empieza en el minuto 10, pueden usar la misma sala.

## Entrada

La entrada contiene varios casos de prueba. Cada caso empieza con una línea con un entero `N` (1 ≤ N ≤ 100 000), la cantidad de reuniones. Le siguen `N` líneas, cada una con dos enteros `inicio` y `fin` (0 ≤ inicio < fin ≤ 1 000 000). Las reuniones no vienen ordenadas. La entrada termina con el fin de archivo (EOF).

## Salida

Para cada caso de prueba imprime en una línea la cantidad mínima de salas necesarias.

## Ejemplo de entrada

```
6
0 30
5 10
15 20
10 15
25 35
12 28
3
0 10
10 20
20 30
```

## Ejemplo de salida

```
3
1
```
