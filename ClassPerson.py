import json

class Persona:
  idd = 0
  ListaMiembros = []
  data = {}
  data['ListaMiembros'] = []

  def __init__(self, Id=None, name=None, email=None, cel=None, prestamo=None):
    self.Id    = Id
    self.name  = name
    self.email = email
    self.cel   = cel
    self.prestamos  = 3
  
  def RegistroPersona(self, nombre, correo, cel):
    self.idd += 1
    newMiembro = Persona( self.idd, nombre, correo, cel)
    self.ListaMiembros.append(newMiembro)
    self.data['ListaMiembros'].append(encoderPersona(newMiembro))
    with open('dataPersonas.json', 'w') as file:
      json.dump(self.data, file, indent=4)
    return newMiembro
  
  def VerPersonas(self):
    with open('dataPersonas.json') as f:
      listillaJSON = json.load(f)
      for li in listillaJSON['ListaMiembros']:
        newMiembro = Persona(li['Id'],li['name'],li['email'],li['cel'],li['prestamos'])
        self.ListaMiembros.append(newMiembro)
    return self.ListaMiembros

  def ValidarDatosPersona(self, miembro):
    for m in self.ListaMiembros:
      if miembro == m.Id:
        if m.prestamos > 0:
          return True
        else: print("| Prestamo Rechazado|No le quedan mas prestamos disponibles")
        break
    return print("| Prestamo Rechazado|Miembro no registrado")

  def PrestamosDisponibles(self, miembro, prestamosD):
    for m in self.ListaMiembros:
      if miembro == m.Id:
        m.prestamos += prestamosD
        return True
    return False



def encoderPersona(persona):
  if isinstance(persona,Persona):
    return {
      'Id'        : persona.Id,
      'name'      : persona.name,
      'email'     : persona.email,
      'cel'       : persona.cel,
      'prestamos' : 3
    }
  raise TypeError(f'El objeto {persona} no es de tipo Persona')