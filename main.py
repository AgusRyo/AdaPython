class Agenda:
  
  def inicializar(self):
    self.contactos=[]

  def menu(self):
    continuar=True
    while continuar== True:
      print("  Bienvenido a la Agenda")
      print("1. Añadir Contacto")
      print("2. Lista Contacto")
      print("3. Buscar Contacto")
      print("4. Editar Contacto")
      print("5. Cerrar Agenda")

      self.opcion=input("Ingrese la opcion")

      if self.opcion=="1":
        self.anadir()
      elif self.opcion =="2":
        self.lista()
      elif self.opcion =="3":
        self.buscar()
      elif self.opcion== "4":
        self.editar()
      elif self.opcion == "5":
        continuar=False  
      else:
        print("Opcion Inválida")

          

  def anadir(self):
    print(" ")
    print("Añadir nuevo contacto")
    print("----------------------")
    nom=input("Introduzca el nombre: ")
    telf= int(input("Ingrese el telefono: "))
    correo=input("Introduzca el mail: ")
    self.contactos.append({'nombre':nom, 'telefono':telf, 'email':correo})

  def lista(self):
    print("  ")
    print("Lista de Contactos")
    print("-------------------")
    if len(self.contactos) ==0:
      print("No hay contactos en la agenda")
    else: 
      for x in range(len(self.contactos)):
        print(self.contactos[x]['nombre'])

  def buscar(self):
    print("  ")
    print("Buscar Contacto")
    print("----------------")
    nom=input("Ingrese el contacto a buscar")
    for x in range (len(self.contactos)):
      if nom == self.contactos[x]['nombre']:
        print("Datos del Contacto")
        print("Nombre: ", self.contactos[x]['nombre'])
        print("Telefono: ", self.contactos[x]['telefono'])
        print("Email: ", self.contactos[x]['email'])
        return x

  def editar(self):
    print("  ")
    print("Buscar Contacto")
    print("----------------")
    data=self.buscar()
    condicion=False
    while condicion==False:
      print("Selecciona que quieres editar")
      print("1. Nombre")
      print("2. Telefono")
      print("3. Email")
      print("4. Volver")
      opcion=input("Ingrese la opcion")
      if opcion=="1":
        nom=input("Ingrese el nuevo nombre: ")
        self.contactos[data]['nombre']=nom
      elif opcion=="2":
        telf=input("Ingrese el nuevo telefono: ")
        self.contactos[data]['telefono']=telf
      elif opcion=="3":
        email=input("Ingrese el nuevo email: ")
        self.contactos[data]['email']=email
      elif opcion== "4":
        condicion=True  
      else:
        print("Opcion Invalida")     








agenda=Agenda()
agenda.inicializar()
agenda.menu()