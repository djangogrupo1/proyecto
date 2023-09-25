function enviarFormulario() {
  // Obtener los valores de los campos del formulario
  var nombre = document.getElementById("name").value;
  var asunto = document.getElementById("subject").value;
  var email = document.getElementById("email").value;
  var telefono = document.getElementById("phone").value;
  var mensaje = document.getElementById("message").value;

  // // Crear un objeto de datos con los valores del formulario
  // var data = {
  //     nombre: nombre,
  //     asunto: asunto,
  //     email: email,
  //     telefono: telefono,
  //     mensaje: mensaje
  // };

  // Validamos que los campos no estén vacíos
  if (nombre == "" ||asunto ==""|| email == ""||telefono =="" || mensaje == "") {
    alert("Todos los campos son obligatorios");

    return false;
  }

  // Agrega aquí la dirección de e-mail donde se enviará el mensaje

  var direccionEmail = "gesfar.servicio@hotmail.com";
  alert("El formulario se ha enviado a " + direccionEmail + ".");

  // Validamos la dirección de correo electrónico
  var expReg = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
  if (!expReg.test(email)) {
    alert("La dirección de correo electrónico no es válida"); return false;
  }

  //Si todo está bien, se envía el formulario
  alert("Formulario enviado correctamente");
  return true;
};

  // Realizar una solicitud HTTP POST utilizando fetch
  fetch("https://outlook.live.com/mail/0/", {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
  })
  .then(function(response) {
      if (response.ok) {
          // El formulario se envió correctamente
          alert("Formulario enviado correctamente");
      } else {
          // Hubo un error al enviar el formulario
          alert("Error al enviar el formulario");
      }
  })
  .catch(function(error) {
      // Hubo un error de red u otro error
      console.error("Error:", error);
      alert("Error al enviar el formulario");
  });


document.getElementById("contact-form").addEventListener("submit", function (event) {
  event.preventDefault();
  enviarFormulario();
});
enviarFormulario()  

// function validarFormulario() {
//     // Obtenemos los valores de los campos
//     var nombre = document.getElementById("name").value;
//     var email = document.getElementById("email").value;
//     var mensaje = document.getElementById("message").value;

//     // Validamos que los campos no estén vacíos
//     if (nombre == "" || email == "" || mensaje == "") {
//       alert("Todos los campos son obligatorios");
//       return false;
//     }

//      // Agrega aquí la dirección de e-mail donde se enviará el mensaje
     
//      var direccionEmail = "gesfar.servicio@hotmail.com";
//      alert("El formulario se ha enviado a " + direccionEmail + ".");
  
//     // Validamos la dirección de correo electrónico
//     var expReg = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
//     if (!expReg.test(email)) {
//       alert("La dirección de correo electrónico no es válida");
//       return false;
//     }
  
//     // Si todo está bien, se envía el formulario
//     alert("Formulario enviado correctamente");
//     return true;
// };
// document.getElementById("contact-form").addEventListener("submit", function(event) {
//   event.preventDefault();
//   validarFormulario();
// });
// validarFormulario()                                                        