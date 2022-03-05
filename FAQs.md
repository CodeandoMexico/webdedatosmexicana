# Preguntas frecuentes

## ¿Por qué crear este proyecto?

México tiene bastantes iniciativas de datos muy buenas, pero muchas de ellas existen porque desde gobierno no existe la iniciativa de trabajar los datos holísticamente. Los datos de una persona servidora pública se encuentran repartidos en innumerables servidores de innumerables dependencias sin nunca hablarse entre sí. Si quisiéramos obtener una visión 360 de un servidor público que en diferentes momentos ha sido candidato, proveedor, gobernante y comprador, tendríamos que buscar en innumerables bases y nos encontraríamos con el problema obvio de identificar cuando un registro en una base efectivamente se refiere a la misma persona física. Lo mismo ocurre con personas morales: una empresa aparece en distintos lugares con nombres ligeramente distintos haciendo la consolidación de la información una tarea difícil. 

La respuesta obvia parecería siempre exponer homoclaves identificadoras, por ejemplo, el CURP o el RFC. Sin embaargo dichos datos no siempre se encuentran disponibles para ser cruzados, o en las ocasiones en las que se encuentran públicos, aún existe una barrera de acceso para realizar análisis masivos por computadora, por que no todos los servicios de data pública se encuentran disponibles mediante un URL que les sea asignado exclusivamente.

Es así como volvemos a un viejo adagio de la teoría de los datos abiertos. En el modelo de apertura de datos de Tim Berners-Lee de las 5 estrellas de la web de datos, la cuarta estrella significa que el recurso se encuentra disponible mediante URI asignada a sí mismo. Esto es, para el registro de una empresa debería existir una URL pública a la que pudiéramos apuntar. Por ejemplo: https://rpc.economia.gob.mx/RFCDELAEMPRESA. De tal modo que bastaría tener una lista de sitios fuente que describen los datos de una empresa para acceder a una visión panorámica de la misma. Nos construyendo perfiles completos de una empresa, un partido político, o una persona simplemente consultando una lista de páginas y su homoclave y cosechando las versiones públicas de sus datos (y en su caso las versiones internas, consultables con las medidas de seguridad pertinentes). Algo como esto:

| URL | Qué podría consultar públicamente | Qué podría consultar de manera privada |
| --- | --- | --- |
| http://sat.gob.mx/RFCDELAEMPRESA | La cédula de identificación fiscal, o una cédula pública que de datos suficientes para facturar | Mi propia información fiscal como empresa | 
| https://rpc.economia.gob.mx/RFCDELAEMPRESA | El registro público de la empresa ante la secretaría de economía | El registro privado de mi empresa para realizar trámites ante la secretaría de economía | 
| https://rnp.ine.mx/RFCDELAEMPRESA | La versión pública de mi empresa ante el Registro nacional de proveedores del INE | El registro privado de mi empresa como proveedor ante el INE |

En su quinta estrella, Berners-Lee imaginó una web totalmente interconectada. Esto es, que en cada una de esas webs, se apuntara a las URL de otra web cuando es pertinente, reemplazando repetir información a través de cadenas de texto, por apuntadores. Extendiendo el ejemplo anterior, nos imaginamos que la versión pública del registro de la empresa se vería así:

| Página visitada | https://rpc.economia.gob.mx/RFCDELAEMPRESA |
| --- | --- |
| Nombre de la empresa: | Empresa SA de CV |
| Board de la empresa: | https://rpc.economia.gob.mx/RFCDELAEMPRESA#board |
| Giro: | https://rpc.economia.gob.mx/catalogos/giros#servicios |
| #Board: | Juan Pérez https://sat.gob.mx/RFCDELAPERSONA |

Es decir, dado que las versiones públicas de la información están disponibles a través de URLs (cuarta estrella) los documentos refieren a los URLs en lugar de reproducir el dato en su base de datos, lo cual genera asincronías de información para los gobiernos y datos desconectados para los ciudadanos. Eso a su vez se traduce en trámites de actualización de información.

Para resolver la falta de gestión de los datos para exponer catálogos importantes de información en URLs públicas, organizaciones de la sociedad civil han compuesto distintos catálogos 
