class Carro:
    def __init__(self, request):
        self.request=request
        self.session = request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        #else:
        self.carro=carro

    def agregar(self, producto):

        if(str(producto) not in self.carro.keys()):
            self.carro[producto]={
                "producto_id":producto,
                "descripcion":producto,
                "precio":producto,
                "cantidad":1,
                "imagen":producto,
            }
        else:
            for key. value in self.carro.items():
                if key==str(producto.cod_prod):
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if produxcto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key.value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"]-1
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
