from Repository.Problem_repository import Reposity_for_Problems
from domain.entities import Problema
from domain.validator import ProblemaValidator
from domain.entities import InitializareException
from domain.validator import ValidatorException
from Repository.Problem_repository import RepositoryException1

class ProblemService:
    """
    Servcie pentru probleme
    Domain: repositary : Reposity_for_Problems
            validator : ProblemaValidator
    """
    
    def __init__ (self, repositary, validator):
        """
        Initializarea service
        repository : object that stores the problems
        validator : object that validates the problems
        """
        self.__rep = repositary
        self.__val = validator

    def CreateProblem (self, numar_lab, numar_prob, descriere, deadline):
        """
        Coordoneaza creearea problemei si il returneaza
        Preconditii: numar - string
                     descriere - string
                     deadline - string
        Postconditii: o problema valida introdusa in repository
        Raises: InitializareException
                ValidatorException
                RepositoryException
        """
        prob = Problema(numar_lab, numar_prob, descriere, deadline)
        self.__val.validate(prob)
        self.__rep.store(prob)

        return prob
    
    def DeleteProblem (self, numar_lab, numar_prob):
        """
        Coordoneaza stergerea unei probleme
        Preconditii: numar - string
        postconditii: daca exista numarul atunci problema este stearsa
        Raises: RepositoryException daca nu exista o problema cu acel numar
        """
        self.__rep.delete(numar_lab, numar_prob)

    def ModifyProblem (self, numar_lab, numar_prob, descriere, deadline):
        """
        Coordoneaza modificarea unei probleme
        Preconditii: numar - string
                     descriere - string
                     deadline - string
        Posconditii: daca numarul exista atunci problema a fost modificata numar : int > 0
                                                                      descriere : string nevid
                                                                      deadline : string nevid
        Raises: RepositoryException cu mesaj : string
                    "numarul nu exista"
                IntializareException
                ValidatorException
        """
        prob = Problema(numar_lab, numar_prob, descriere, deadline)
        self.__val.validate(prob)
        self.__rep.modify(numar_lab, numar_prob, descriere, deadline)

    def getproblema (self, numar_lab, numar_prob):
        """
        numar - string
        """
        prob = self.__rep.getProblem(numar_lab, numar_prob)
        return prob.getdescriere(), prob.getdeadline()


    def getAllProblems (self, numar_lab):
        return self.__rep.getProblems(numar_lab)
    
    def getlabs (self):
        return self.__rep.getLabs()

def testmodifyproblem ():
    rep = Reposity_for_Problems()
    val = ProblemaValidator()
    service = ProblemService(rep, val)
    
    prob1 = service.CreateProblem("1","1", "ceva 1","3 mai")
    prob2 = service.CreateProblem("1", "2", "ceva 2", "4 mai")
    service.ModifyProblem("1", "1", "ceva nou", "7 mai")
    allprobs = service.getAllProblems(1)
    assert allprobs[1].getnumar_prob() == 1
    assert allprobs[1].getdescriere() == "ceva nou"
    assert allprobs[1].getdeadline() == "7 mai"
    try:
        service.ModifyProblem("1", "1", "ceva", "")
        assert False
    except ValidatorException as ex:
        assert str(ex) == "deadline - ul este vid\n"

def testDeleteProblem ():
    rep = Reposity_for_Problems()
    val = ProblemaValidator()
    service = ProblemService(rep, val)
    
    prob1 = service.CreateProblem("1", "1", "ceva 1","3 mai")
    prob2 = service.CreateProblem("1", "2", "ceva 2", "4 mai")
    service.DeleteProblem("1","1")
    allprobs = service.getAllProblems(1)
    assert allprobs[0].getnumar_prob() == prob2.getnumar_prob()
    assert len(allprobs) == 1
    try:
        service.DeleteProblem("1", "1")
        assert False
    except RepositoryException1 as ex:
        assert str(ex) == "numarul problemei nu exista in reposit"

def testCreateProblem ():
    rep = Reposity_for_Problems()
    val = ProblemaValidator()
    service = ProblemService(rep, val)
    
    problem = service.CreateProblem("1", "1", "ceva 1","3 mai")
    allprobs = service.getAllProblems(1)
    assert problem.getnumar_prob() == allprobs[0].getnumar_prob()
    assert len(allprobs) == 1
    try:
        prob_bad = service.CreateProblem("1ce","ceva", "Ion","mai 3")
        assert False
    except InitializareException as ex:
        assert str(ex) == "numarul nu este un numar intreg\n"
    try:
        prob_bad = service.CreateProblem("1", "1", "cineva", "45 mai")
        assert False
    except RepositoryException1 as ex:
        assert str(ex.get_errors()) == "numarul unei probleme trebuie sa apara o singura data"

testCreateProblem()
testDeleteProblem()
testmodifyproblem()
print("7")