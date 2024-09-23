from domain.entities import Student
from domain.entities import Problema

class AssignmentException (Exception):
    pass

class Assignments_for_Students:
    """
    Clasa pentru assignarea unei probleme de laborator si notarea acesteia
    Domain: Dictionar de dictionare unde valoare la inner_key(problema) este nota
    Invariant: Nu i se poate atribui unui student aceasi problema din acelasi lab de 2 ori
    """
    
    def __init__ (self):
        self.__assignments = {}

    def assign (self, stud_id, prob):
        """
        Functie care assigneaza unui student o problema
        Preconditii:
            student_id : string - id - ul unui student valid
            prob : Problema object
        Postconditii:
            problema a fost assignata studentului in reposit
        Raises:
            AssignmentException cu mesaj : str
                "aceasta problema a fost deja atribuita studentului"
        """
        if self.size(stud_id) == 0:
            element = {prob : None}
            self.__assignments[str(stud_id)] = element
        else:
            if self.getproblema(stud_id, prob.getnumar_lab(), prob.getnumar_prob()) != None:
                raise AssignmentException("aceasta problema a fost deja atribuita studentului")
            else:
                self.__assignments[str(stud_id)][prob] = None

    def evaluate (self, stud_id, prob, nota):
        """
        Functie care evalueaza studentul la o problema pe care a facut - o oferindui o nota
        Preconditii:
            stud_id : str - id - ul unui student care exista in ASSIGNMENTS REPO
            prob : Problema object - problema care va fi evaluata (prob trebuie sa exista in ASSIGNMENTS REPO)
            nota : int - nota care va fi primita de student la problema respectiva
        Postconditii:
            studentul a primit o nota pentru problema respectiva
        Raises:
            AssignmentException cu mesaj : str - "studentul pe care doriti sa il evaluati nu a primit nici o problema"
                                               - "studentul nu a primit aceasta problema ca sa puteti sa o evaluati"
        """
        if self.__assignments.get(str(stud_id)) == None:
            raise AssignmentException("studentul pe care doriti sa il evaluati nu a primit nici o problema")   #verificam daca studentul exista in Repo Assignments
        else:
            probleme = self.getprobleme(stud_id)
            ok = False
            for problema in probleme:
                if problema.getnumar_lab() == prob.getnumar_lab() and problema.getnumar_prob() == prob.getnumar_prob():   #verificam daca problema studentului exista in Repo Assignments
                    ok = True
            if ok == False:
                raise AssignmentException("studentul nu a primit aceasta problema ca sa puteti sa o evaluati")
        self.__assignments[str(stud_id)][prob] = nota

    def getproblema (self, stud_id, prob_lab, prob_num):
        """
        Getter pentru problema pe care o are un student
        Preconditii: stud_id : int
        """
        if self.__assignments.get(str(stud_id)) != None:
            probleme = self.getprobleme(stud_id)
            for problema in probleme:
                if problema.getnumar_lab() == int(prob_lab) and problema.getnumar_prob() == int(prob_num):
                    return problema
            return None
        else:
            return None

    def get_probleme_lab (self, stud_id, prob_lab):
        lista = []
        if self.__assignments.get(str(stud_id)) != None:
            probleme = self.getprobleme(stud_id)
            for problema in probleme:
                if problema.getnumar_lab() == int(prob_lab):
                    lista.append(problema)
            if len(lista) == 0:
                return None
            else:
                return lista
        else:
            return None

    def getprobleme (self, stud_id):
        """
        Getter pentru problemele pe care le are un student
        Preconditii: stud_id : int
        """
        if self.__assignments.get(str(stud_id)) != None:
            return list(self.__assignments[str(stud_id)].keys())
        else:
            return None
        
    def getnote (self, stud_id):
        if self.__assignments.get(str(stud_id)) != None:
            return list(self.__assignments[str(stud_id)].values())
        else:
            return None
        
    def getnota (self, stud_id, prob_lab, prob_num):
        """
        getter pentru nota unui student de la o anume problema
        Preconditii: stud_id : int
        """
        problema = self.getproblema(stud_id, prob_lab, prob_num)
        if problema != None:
            return self.__assignments[str(stud_id)].get(problema)
        else:
            return None
        # if self.__assignments.get(str(stud_id)) != None:
        #     probleme = self.getprobleme(stud_id)
        #     for problema in probleme:
        #         if problema.getnumar_lab() == prob_lab and problema.getnumar_prob() == prob_num:
        #             return self.__assignments[str(stud_id)].get(problema)                                        #incearca sa faci cu getproblema
        #     return None
        # else:
        #     return None
        
    def size (self, stud_id):
        """
        cate probleme are un student
        """
        if self.__assignments.get(str(stud_id)) != None:
            return len(self.__assignments[str(stud_id)])
        return 0
    
    def get_studenti (self):
        return list(self.__assignments.keys())



def testassign():
    repo_assignments = Assignments_for_Students()
    stud1 = Student("2", "Stefan", "210")
    prob1 = Problema("1", "2", "Descriere1", "Deadline1")
    repo_assignments.assign(stud1.getId(), prob1)
    problema = repo_assignments.getproblema(stud1.getId(), prob1.getnumar_lab(), prob1.getnumar_prob())
    problema.getdescriere() == "Descriere1"
    problema.getdeadline() == "Deadline1"
    nota = repo_assignments.getnota(stud1.getId(), prob1.getnumar_lab(), prob1.getnumar_prob())
    assert nota == None
    try:
        repo_assignments.assign(stud1.getId(), prob1)
        assert False
    except AssignmentException as ex:
        assert str(ex) == "aceasta problema a fost deja atribuita studentului"

def testevaluate ():
    repo_assignments = Assignments_for_Students()
    stud1 = Student("2", "Stefan", "210")
    prob1 = Problema("1", "2", "Descriere1", "Deadline1")
    repo_assignments.assign(stud1.getId(), prob1)
    repo_assignments.evaluate("2", prob1, 10)
    nota = repo_assignments.getnota(stud1.getId(), prob1.getnumar_lab(), prob1.getnumar_prob())
    assert nota == 10

    try:
        repo_assignments.evaluate("1", prob1, 7)
        assert False
    except AssignmentException as ex:
        assert str(ex) == "studentul pe care doriti sa il evaluati nu a primit nici o problema"

    prob2 = Problema("1", "1", "ceva", "something")
    try:
        repo_assignments.evaluate("2",prob2, 7)
        assert False
    except AssignmentException as ex:
        assert str(ex) == "studentul nu a primit aceasta problema ca sa puteti sa o evaluati"

testevaluate()
testassign()