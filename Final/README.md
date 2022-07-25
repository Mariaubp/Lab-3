# Sitio Web eCommerce con API y Base de Datos 
Integrantes :
**Florencia Fernandez**
**, Constanza Gigli**

-Link de la api :
<a href="https://www.frankfurter.app/">https://www.frankfurter.app/</a><br>
## Frankfurter API
 <img src="logoFrank.png" width="120">    
La api rastrea las tasas de referencia de divisas publicadas por el Banco Central Europeo ,está organizada en torno a rutas que designan la fecha solicitada o el intervalo de fechas. </li>
  
## Conversion
Puede convertir cualquier valor entre monedas utilizando los puntos finales en combinación con el amountparámetro.
 <pre><code>        
 const host = 'api.frankfurter.app';
fetch(`https://${host}/latest?amount=10&from=GBP&to=USD`)
  .then(resp => resp.json())
  .then((data) => {
    alert(`10 GBP = ${data.rates.USD} USD`);
  });
</code></pre> 
En el ejemplo anterior convertimos 10 libras esterlinas a dólares estadounidenses.
### Nuestro proyecto 
Es una página web que simula un carrito de compras.

-Lo primero que vez son los productos disponibles (cargados en base de datos)

-Podes ir agregando las diversas opciones de compra a nuestro carrito 

-En la sección de My Cart, podes ver todo lo que deseamos comprar con su precio detallado,podemos ver el total de la “compra” y convertirlo a la moneda deseada, ya que los precios de la página están en dólares (uso de la API).

<h2 class="code-line" data-line-start=30 data-line-end=31 ><a id="Funcionamiento_30"></a>Funcionamiento</h2>
<p class="has-line-data" data-line-start="32" data-line-end="33">Para poder probar  nuestra pagina vamos a usar a Xampp como servidor web de manera local.
Con el Apache podemos mostrar nuestra pagina web.
Con MySql podemos manejar el sistema de base de datos.
Entonces para poder enlazar esas dos aplicaciones usamos el lenguaje php, deben estar activados para que el Xampp funcione como servidor local y muestre la pagina web.


