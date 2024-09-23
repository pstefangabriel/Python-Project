from domain.entities import Problema

class RepositoryException1 (Exception):
    def __init__ (self, mesaj):
        self.__erori = mesaj

    def get_errors (self):
        return self.__erori

class Reposity_for_Problems:
    """
    Repository pentru probleme
    Domain: prob : Problema object
    Invariant: Nu trebuie sa existe doi 2 probleme cu acelasi numar
    """
    def __init__ (self):
        """
        initializarea 
        """
        self._problems = {}

    def store (self, prob):
        """
        Functie care adauga problema in repository
        Preconditii: prob : Problema object Valid
        Postconditii: prob a fost adaugat in repository
        Raises: RepositoryError cu mesaj : string 
                    "numarul unei probleme trebuie sa apara o singura data" daca numarul problemei apare de mai multe ori in repository
        """
        if self.size(prob.getnumar_lab()) == 0:
            element = {str(prob.getnumar_prob()) :  prob}
            self._problems[str(prob.getnumar_lab())] = element
        else:
            if str(prob.getnumar_prob()) in  self._problems[str(prob.getnumar_lab())]:
                raise RepositoryException1("numarul unei probleme trebuie sa apara o singura data")
            else:
                self._problems[str(prob.getnumar_lab())][str(prob.getnumar_prob())] = prob

    def delete (self, prob_lab, prob_numar):
        """
        Functie care elimina o problema din reposit
        Preconditii: prob_numar : string - numarul unei probleme
        Postconditii: problema este eliminata din reposit
        Raises: RepositoryException cu mesaj : string
                    "problema nu exista in reposit"
        """
        if prob_lab in self._problems:
            if prob_numar in self._problems[prob_lab]:
                self._problems[prob_lab].pop(prob_numar)
            else:
                raise RepositoryException1("numarul problemei nu exista in reposit")
        else:
            raise RepositoryException1("numarul labului nu exista in reposit")
        
    def modify (self, prob_lab, prob_numar, prob_descriere, prob_deadline):
        """
        Functie care modifica o problema din repository dupa numar (daca exista) stergandu-l si adaugandu-l cu acelasi numar, noua descriere si noul deadline
        Preconditii: prob_numar : string
                     prob_descriere : string
                     prob_deadline : string
        Postconditii: problema este modificata  prob_numar : int
                                                prob_descriere : string
                                                prob_deadline : string
        Raises: RepositoyException cu mesaj : string
                    "problema nu exista"
        """
        if prob_lab in self._problems:
            if prob_numar in self._problems[prob_lab]:
                self._problems[prob_lab].pop(prob_numar)
            else:
                raise RepositoryException1("numarul problemei nu exista in reposit")
        else:
            raise RepositoryException1("numarul labului nu exista in reposit")
        self._problems[str(prob_lab)][str(prob_numar)] = Problema(prob_lab, prob_numar, prob_descriere, prob_deadline)

    def getProblem (self, prob_lab, prob_numar):
        """
        prob_numar : string
        """
        if self._problems.get(str(prob_lab)) == None:
            raise RepositoryException1("numarul problemei nu exista")
        else:
            if str(prob_numar) in self._problems[str(prob_lab)]:
                return self._problems[str(prob_lab)][str(prob_numar)]
            else:
                raise RepositoryException1("numarul problemei nu exista")

    
    def size (self, numar_lab):
        if str(numar_lab) in self._problems:
            return len(self._problems[str(numar_lab)])
        else:
            return 0
    
    def getProblems (self, numar_lab):
        """
        Getter pentru toate problemele
        """
        if str(numar_lab) in self._problems:
            return list(self._problems[str(numar_lab)].values())
        else:
            return 0 
        
    def getLabs (self):
        return list(self._problems.keys())

def testmodify():
    rep = Reposity_for_Problems()
    prob1 = Problema("7", "1", "O descriere 1", "10 Mai")
    rep.store(prob1)
    prob2 = Problema("7", "2", "O descriere 2", "11 Mai")
    rep.store(prob2)
    prob3 = Problema("8", "1", "O descriere 2", "11 Mai")
    rep.store(prob3)
    rep.modify("7", "1",  "O descriere noua", "24 Mai")
    allprobs = rep.getProblems(7)
    assert allprobs[1].getdescriere() == "O descriere noua"
    assert allprobs[1].getdeadline() == "24 Mai"
    assert allprobs[1].getnumar_prob() == 1
    try:
        rep.modify("7", "3", "nu","3")
        assert False
    except RepositoryException1 as ex:
        assert str(ex) == "numarul problemei nu exista in reposit"
    rep.modify("8", "1", "nu","3")

def testdelete():
    rep = Reposity_for_Problems()
    prob1 = Problema("7", "8", "O descriere 1", "10 Mai")
    rep.store(prob1)
    prob2 = Problema("7", "11", "O descriere 2", "11 Mai")
    rep.store(prob2)
    rep.delete("7", "11")
    allprobs = rep.getProblems(7)
    assert allprobs[0].getnumar_prob() == prob1.getnumar_prob()
    try:
        rep.delete("7","11")
        assert False
    except RepositoryException1 as ex:
        assert str(ex) == "numarul problemei nu exista in reposit"

def teststore ():
    rep = Reposity_for_Problems()
    prob1 = Problema("7", "1", "O descriere 1", "10 Mai")
    rep.store(prob1)
    prob2 = Problema("8", "2", "O descriere 2", "30 Mai")
    rep.store(prob2)
    assert rep.size(7) == 1
    assert rep.size(8) == 1
    try:
        prob3 = Problema("7", "1", "cineva", "89 Mai")
        rep.store(prob3)
        assert False
    except RepositoryException1 as ex:
        assert str(ex) == "numarul unei probleme trebuie sa apara o singura data"

teststore()
testdelete()
testmodify()

