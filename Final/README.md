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
Creamos una pagina web ecomerce 

<h2 class="code-line" data-line-start=30 data-line-end=31 ><a id="Funcionamiento_30"></a>Funcionamiento</h2>
<p class="has-line-data" data-line-start="32" data-line-end="33">Una vez ya todo instalado, tenemos los codigo .py establecidos, necesarios para su funcionamiento,Para ejecutarlo lo hacemos ocn el comando.</p>
 <pre><code>        python main.py
</code></pre> 
 </ul>
