/* JS de menu de Hexagonos */
const hexagons = document.querySelectorAll('.hex');

hexagons.forEach(hex => {
    const hexImage = hex.querySelector('.hex-inner');
    hex.addEventListener('mouseenter', () => {
        hexImage.style.transform = 'scale(1.2)';
    });
    hex.addEventListener('mouseleave', () => {
        hexImage.style.transform = 'scale(1)';
    });
});

/* fin */


/* PARA REPLICAR EL HEADER*/

let miHeader =  `   
<!-- Header logo -->
<a href="index.html">
  <div class="header-logo">
    <img width="150" src="./img/logo blanco.png" alt="logo " />
  </div>
</a>
<!-- fin header -->
<br />
<!-- Menu nav -->
<nav class="header-menu">
  <ul>
    <li><a href="index.html">Inicio</a></li>
    <li><a href="modulos.html">Modulos</a></li>
    <li><a href="nosotros.html">Sobre Nosotros</a></li>
    <li><a href="acercade.html">Acerca de</a></li>
    <li><a href="contacto.html">Contactos</a></li>

  </ul>
</nav>
<!-- fin nav -->
`
document.querySelector("header").innerHTML = miHeader;

/* PARA REPLICAR EL FOOTER */

let miFooter = `

<div class="footer-container">
<div class="footer-column">
  <h3><i class="fas fa-cogs"></i> Nuestra Plataforma</h3>
  <ul style="background-color: #3330;">
    <li>Sencillez y agilidad</li>
    <li>Una herramienta que se adapta a las necesidades y procesos actuales de tu organización</li>
    <li>Data Analytics para medir la operación en tiempo real</li>
    <li>APIs de integración</li>
    <li>Privacidad y resguardo de datos</li>
  </ul>
 
</div>
<div class="footer-column">
  <h3><i class="fas fa-cubes"></i> Módulos Disponibles</h3>
  <p>Toma el control absoluto para entregar la mejor experiencia a tus pacientes.</p>
  <div class="hex-container">
    <!-- Aquí coloca tus hexágonos o enlaces a los módulos disponibles -->
  </div>
</div>
<div class="footer-column">
  <h3><i class="fas fa-map-marker-alt"></i> Ubicación</h3>
  <div id="map"><iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14029.25880567122!2d-65.78533767015857!3d-28.470067763185654!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x942428bf1d0f9fcd%3A0x7e1edd4b1609861a!2sSan%20Fernando%20del%20Valle%20de%20Catamarca%2C%20Catamarca!5e0!3m2!1ses-419!2sar!4v1685286269393!5m2!1ses-419!2sar" width="200" height="100" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div>
<div class="footer-column">
  <h3><i class="fas fa-whatsapp"></i> Contacto</h3>
  <p>Contáctanos a través de:</p>
  <a href="gesfar.servicio@hotmail.com" class=""><img src="./img/gmail (1).png" width="20px" alt="Email"><strong>E-mail</strong></a>
  <a href="https://wa.me/11111111" class="whatsapp-link"><img src="./img/whatsapp (1).png" width="20px" alt="WhatsApp"><strong>  11111111</strong></a>
  <p>Nuestras Redes:</p>
  <a href="#" class=""><img src="./img/facebook (1).png" width="20px" alt="Facebook"><strong>Facebook</strong></a>
  <a href="#" class=""><img src="./img/instagram (1).png" width="20px" alt="Instagram"><strong>Instagram</strong></a>
</div>
</div>
</footer>
<section class="sub-footer" style="background-color: #f3e3f9; text-align: center; padding: 10px;">
<div class="sub-footer-container">
<div class="row">
    <div class="col-sm-10 text-center text-sm-left">
      <span class="">Ges-Far 2023 ©. <span class="d-block d-sm-inline mb-2">Todos los derechos reservados.<br>Sitio Desarrollado por: The 4 Big Brains.</span></span>
    </div>
    <div class="col-sm-2 text-center text-sm-right">
      <a href="index.html" target="_blank" class="hvr-float-shadow">
          <img src="./img/silueta logo.png" width="48px" alt="Ges-Far">
      </a>
    </div>
</div>
</div>
</section>


`
document.querySelector("footer").innerHTML = miFooter;

// para funcionar los videos 

window.addEventListener('DOMContentLoaded',(event)=>{
  var video= document.getElementById('miVideo');
  video.play()
});


// //// REcibir los mensajes en nuestro email

// function validarFormulario() {
//   // Obtenemos los valores de los campos
//   var nombre = document.getElementById("nombre").value;
//   var email = document.getElementById("email").value;
//   var mensaje = document.getElementById("mensaje").value;

//   // Validamos que los campos no estén vacíos
//   if (nombre == "" || email == "" || mensaje == "") {
//     alert("Todos los campos son obligatorios");
//     return false;
//   }

//   // Validamos la dirección de correo electrónico
//   var expReg = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
//   if (!expReg.test(email)) {
//     alert("La dirección de correo electrónico no es válida");
//     return false;
//   }

//   // Si todo está bien, se envía el formulario
//   alert("Formulario enviado correctamente");
//   return true;
// }
 
  