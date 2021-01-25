class Persona:
    def __init__(self, Id=None, name=None, email=None, cel=None):
        self.Id    = Id
        self.name  = name
        self.email = email
        self.cel   = cel
        self.listaPersonas = []

    def setPersona(self, Id=None, name=None, email=None, cel=None):
        if (Id != None):
          self.Id = Id
        if (name != None):
          self.name = name
        if (email != None):
            self.email = email
        if (cel != None):
            self.cel = cel
        
    def getPersona(self):
        return self.Id,self.name,self.email,self.cel

    def addObject(self, persona):
        self.listaPersonas.append(persona)

    def removeObject(self, Id=None, name=None):
        if (Id != None):
            i = 0
            for p in self.listaPersonas:
                if (Id == p.Id):
                    self.listaPersonas.pop(i)
                    return True
                i += 1
        return False
                
    def updateObject(self, Id, persona):
        i = 0
        for p in self.listaPersonas:
            if Id == p.Id:
                self.listaPersonas[i] = persona
                return 'Datos actualizados'
            i += 1
        return 'Miembro no encontrado'

    def searchObject(self, Id=None, name=None):
        i = 0
        if (Id != None or name != None):
            for p in self.listaPersonas:
                if (Id == p.Id or name == p.name):
                    return self.listaPersonas[i]
                i += 1
        return 'Miembro no encontrado'

    def getLista(self):
        return self.listaPersonas