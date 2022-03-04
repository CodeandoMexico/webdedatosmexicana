# Preguntas frecuentes

## ¿Por qué crear este proyecto?

México tiene bastantes iniciativas de datos muy buenas, pero muchas de ellas existen porque desde gobierno no existe la iniciativa de trabajar los datos holíticamente. Los datos de una persona servidora pública se encuentran repartidos en innumerables servidores de innumerables dependencias sin nunca hablarse entre sí. Si quisiéramos obtener una visión 360 de un servidor público que en diferentes momentos ha sido candidato, proveedor, gobernante y comprador, tendríamos que buscar en innumerables bases y nos encontraríamos con el problema obvio de identificar cuando un registro en una base efectivamente se refiere a la misma persona física. Lo mismo ocurre con personas morales: una empresa aparece en distintos lugares con nombres ligeramente distintos haciendo la consolidación de la información una tarea difícil. 

La respuesta obvia parecería siempre exponer homoclaves identificadoras, por ejemplo, el CURP o el RFC. Sin embaargo dichos datos no siempre se encuentran disponibles para ser cruzados, o en las ocasiones en las que se encuentran públicos, aún existe una barrera de acceso para realizar análisis masivos por computadora, por que no todos los servicios de data pública se encuentran disponibles mediante un URL que les sea asignado exclusivamente.

Es así como volvemos a un viejo adagio de la teoría de los datos abiertos. En el modelo de apertura de datos de Tim Berners-Lee de las 5 estrellas de los datos abiertos, la cuarta estrella significa que el recurso se encuentra disponible mediante URI asignada a sí mismo. Esto es, para el registro de una empresa debería existir una URL pública a la que pudiéramos apuntar. Por ejemplo: https://rpc.economia.gob.mx/RFCDELAEMPRESA. De tal modo que bastaría tener una lista de sitios fuente que describen los datos de una empresa para acceder a una visión panorámica de la misma. Nos construyendo perfiles completos de una empresa, un partido político, o una persona simplemente consultando una lista de páginas y su homoclave y cosechando las versiones públicas de sus datos (y en su caso las versiones internas, consultables con las medidas de seguridad pertinentes). Algo como esto:

| URL | Qué podría consultar públicamente | Qué podría consultar de manera privada |
| --- | --- | --- |
| http://sat.gob.mx/RFCDELAEMPRESA | La cédula de identificación fiscal, o una cédula pública que de datos suficientes para facturar | Mi propia información fiscal como empresa | 
| https://rpc.economia.gob.mx/RFCDELAEMPRESA | El registro público de la empresa ante la secretaría de economía | El registro privado de mi empresa para realizar trámites ante la secretaría de economía | 
| https://rnp.ine.mx/RFCDELAEMPRESA | La versión pública de mi empresa ante el Registro nacional de proveedores del INE | El registro privado de mi empresa como proveedor ante el INE |

