const { createApp } = Vue

  createApp({
    data() {
      return {
        farmacos:[],
        
        carga:true,
        editar:false,
      
        message:"Espere un momento a que se carguen los datos",
        url:'https://pamelacardozo.pythonanywhere.com/farmacos'
      }
    },
    methods: {
    
        fetchData(url) { 
           
           fetch(url)
            .then(response => response.json())
            .then(data => {
              console.log(data)
              this.productos=data
        this.carga=false
           })
            .catch(error=>{
               alert("Ups... se produjo un error: "+ error);
               this.error=true
             })
        
        }
      },
      created() {
        this.fetchData(this.url)
      }
    

  }).mount('#app')