from src.m.service import Service
from src.m.connexionBDD import connexionBDD
class Entretien(Service):
      def __init__(self, jourService, moisService, anneeService, jourDemande, moisDemande, anneeDemande, rapport, categorie, idClient):
        super(Service, self).__init__(self, jourService, moisService, anneeService, jourDemande, moisDemande, anneeDemande, rapport, categorie)
        self.categorie = 2
        self.etat = 0
        self.idService=self.enregistrerService(self,idClient,self.categorie,self.etat)
     def effectuerEntretien(self):
        self.etat = 1
        connexion  = connexionBDD()
        connexion.cur.execute("UPDATE service SET etat= 1 WHERE idService = ?", (self.idService))
        connexion.seDeconnecter()