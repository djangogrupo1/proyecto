const { createApp } = Vue;
  createApp({
    data() {
      return {
        farmacos:[],
        //url:'http://localhost:5000/productos', 
        // si el backend esta corriendo local  usar localhost 5000(si no lo subieron a pythonanywhere)
        url:'https://pamelacardozo.pythonanywhere.com/farmacos',   // si ya lo subieron a pythonanywhere
        error:false,
        cargando:true,
        /*atributos para el guardar los valores del formulario */
        id:0,
        codigo_barras:"",
        nombre:"", 
        presentacion:"",
        laboratorio:"",
        concentracion:"",
        lote:"",
        stock:0,
        fecha_vencimiento:"",
      };  
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.farmacos = data;
                    this.cargando = false;
                })
                .catch(err => {
                    console.error(err);
             
                });
        },
        eliminar(id) {
            const url = this.url+ '/' + id;
            var options = {
                method: 'DELETE',
            };
            fetch(url, options)
                .then(res => res.text()) // or res.json()
                .then(() => {
			        alert('Eliminado');
                    location.reload(); // recarga el json luego de eliminado el registro
                });
        },
        agregar(){
            let farmacos = {
                codigo_barras: this.codigo_barras,
                nombre: this.nombre,
                presentacion: this.presentacion,
                laboratorio: this.laboratorio,
                concentracion: this.concentracion,
                lote: this.lote,
                stock: this.stock,
                fecha_vencimiento:this.fecha_vencimiento,
            };
            var options = {
                body:JSON.stringify(farmacos),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            };
            fetch(this.url, options)
                .then(function () {
                    alert("Registro grabado")
                    window.location.href = "./farmacos.html";  // recarga productos.html
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar")  // puedo mostrar el error tambien
                });      
        },
    },
    created() {
        this.fetchData(this.url)
    },
  }).mount('#app');

  