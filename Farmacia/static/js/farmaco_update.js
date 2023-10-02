console.log(location.search)     // lee los argumentos pasados a este formulario
var id=location.search.substr(4)  // producto_update.html?id=1
console.log(id)
const { createApp } = Vue
  createApp({
    data() {
      return {
        id:0,
        codigo_barras:"",
        nombre:"", 
        presentacion:"",
        laboratorio:"",
        concentracion:"",
        lote:"",
        stock:0,
        fecha_vencimiento:"",
        url:'https://pamelacardozo.pythonanywhere.com/farmacos'+id,
       }  
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.id = data.id
                    this.codigo_barras = data.codigo_barras
                    this.nombre = data.nombre
                    this.presentacion = data.presentacion
                    this.laboratorio = data.laboratorio
                    this.concentracion = data.concentracion
                    this.lote = data.lote
                    this.stock= data.stock
                    this.fecha_vencimiento = data.fecha_vencimiento
                })
                .catch(err => {
                    console.error(err);
                    this.error=true              
                })
        },
        modificar() {
            let farmacos = {
                // codigo_barras: this.codigo_barras,
                nombre: this.nombre,
                // presentacion: this.presentacion,
                // laboratorio: this.laboratorio,
                // concentracion: this.concentracion,
                // lote: this.lote,
                stock: this.stock,
                // fecha_vencimiento: this.fecha_vencimiento,
            }
            var options = {
                body: JSON.stringify(farmacos),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function () {
                    alert("Modificado")
                    window.location.href = "./farmacos.html"; // navega a productos.html          
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar")
                })      
        }
    },
    created() {
        this.fetchData(this.url)
    },
}).mount('#app')
