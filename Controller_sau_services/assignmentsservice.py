from Repository.Assignments import Assignments_for_Students
from Repository.Problem_repository import Reposity_for_Problems
from Repository.Student_repository import Reposity_for_Students
from domain.entities import Problema
from domain.entities import Student
from Repository.Problem_repository import RepositoryException1
from Repository.Student_repository import RepositoryException
from Repository.Assignments import AssignmentException
from domain.entities import Primi10Dto
from Utilities.sortari import gnomeSort, quickSortRec

class Service_for_Assignments:
    """
    Clasa care coordoneaza asignarea problemelor studentilor
    Domain: Repositary_for_Assignments - Assignments_for_Students Object
            Repositary_for_Students - Student repositary Object
            Repositary_for_Problems - Problem repositary Object
    Invariant: id - ul studentului care i se asigneaza problema trebuie sa existe
               problema care i se assigneaza trebuie sa existe
               unui student i se poate assigna aceasi problema o singura data
    """

    def __init__ (self, repositary_for_assignments, repositary_for_students, repositary_for_problems):
        self.__repo_assignments = repositary_for_assignments
        self.__repo_students = repositary_for_students
        self.__repo_problems = repositary_for_problems

    def assign_problem (self, studid, prob_lab, prob_num):
        """
        Functie care coordoneaza asignarea
        Preconditii: studid - str
                     prob_lab - str
                     prob_num - str
        Postconditii: Daca studid exista in reposit for students si prob_lab si prob_num exista in reposit for problems atunci 
                      studentului respectiv o sa ii fie assignata problema  DACA NU A FOST ASIGNATA DEJA
        Raises: RepositoryException1 cu mesaj : str - "numarul problemei nu exista"
                RepositoryException cu mesaj : str - "id - ul nu exista"
                AssignmentException cu mesaj : str - "aceasta problema a fost deja atribuita studentului"
        """
        self.__repo_students.getStudent(str(studid)) #verificam daca da raise la Exceptie
        prob = self.__repo_problems.getProblem(str(prob_lab), str(prob_num)) #verificam da da raise la Exceptie
        self.__repo_assignments.assign(studid, prob)

    def evaluate_problem (self, studid, prob_lab, prob_num, nota):
        prob = self.get_problema_assignata(studid, prob_lab, prob_num)
        if prob == None:
            raise AssignmentException("aceasta problema nu a fost asignata")
        self.__repo_assignments.evaluate(studid, prob, nota)

    def view_assignments (self, studid):
        if self.__repo_assignments.getprobleme(studid) == None:
            raise AssignmentException("studentul respectiv nu are probleme")
        else:
            return self.__repo_assignments.getprobleme(studid), self.__repo_assignments.getnote(studid)

    def get_problema_assignata (self, studid, problab, probnum):
        return self.__repo_assignments.getproblema(studid, problab, probnum)
    
    def get_probleme_assignate (self, studid):
        return self.__repo_assignments.getprobleme(studid)
    
    def get_nota (self, studid, prob_lab, prob_num):
        return self.__repo_assignments.getnota(studid, prob_lab, prob_num)
    
    def get_size (self, stud_id):
        return self.__repo_assignments.size(stud_id)

    #recursiv
    def creaza_vector(self, lista, index, lungime, studenti, prob_lab, prob_num):
        if index < lungime and self.__repo_assignments.getproblema(str(studenti[index]), prob_lab, prob_num) != None:
            lista.append(self.__repo_students.getStudent(str(studenti[index])))
            self.creaza_vector(lista, index + 1, lungime, studenti, prob_lab, prob_num)
        elif index < lungime:
            self.creaza_vector(lista, index + 1, lungime, studenti, prob_lab, prob_num)

    def ordoneaza_nume (self, prob_lab, prob_num):
        ordonarea = []
        self.creaza_vector(ordonarea, 0, len(self.__repo_assignments.get_studenti()), self.__repo_assignments.get_studenti(), prob_lab, prob_num)
        # for stud_id in self.__repo_assignments.get_studenti():
        #     if self.__repo_assignments.getproblema(str(stud_id), prob_lab, prob_num) != None:
        #         ordonarea.append(self.__repo_students.getStudent(str(stud_id)))
        if len(ordonarea) == 0:
            raise AssignmentException("nu s - a putut efectua ordonarea")
        ordonarea.sort(key = lambda x : x.getnume())

        return ordonarea
    
    def toti_sub5 (self, prob_lab):
        ordonarea = []
        for stud_id in self.__repo_assignments.get_studenti():
            #if self.__repo_assignments.getproblema(str(stud_id), prob_lab, prob_num) != None:
                #if self.__repo_assignments.getnota(str(stud_id), prob_lab, prob_num) != None and self.__repo_assignments.getnota(str(stud_id), prob_lab, prob_num) < 5:
            medie = self.medie_lab(stud_id, prob_lab)
            if medie != None and medie < 5:
                stud = self.__repo_students.getStudent(str(stud_id))
                stud.set_medie(medie)
                ordonarea.append(self.__repo_students.getStudent(str(stud_id)))
        if len(ordonarea) == 0:
            raise AssignmentException("nu exista studenti cu nota sub 5 la aceasta problema")

        return ordonarea

    # de analizat complexitatea
    def medie_lab (self, stud_id, prob_lab):
        probleme = self.__repo_assignments.get_probleme_lab(stud_id, prob_lab)
        if probleme != None:
            medie = 0
            #contor = 0
            for problema in probleme:
                if self.__repo_assignments.getnota(str(stud_id), prob_lab, problema.getnumar_prob()) != None:
                    medie += self.__repo_assignments.getnota(str(stud_id), prob_lab, problema.getnumar_prob())
            medie = medie / len(probleme)

            return medie
        else:
            return None

    #recursiv
    def formeaza_lista_studenti(self, ordonare, index, lungime, lista, prob_lab, prob_num):
        if index < lungime and self.__repo_assignments.getnota(str(lista[index].getId()), prob_lab, prob_num) != None:
            ordonare.append(lista[index])
            self.formeaza_lista_studenti(ordonare, index + 1, lungime, lista, prob_lab, prob_num)
        elif index < lungime:
            self.formeaza_lista_studenti(ordonare, index + 1, lungime, lista, prob_lab, prob_num)

    def __get_studenti_with_problem (self, prob_lab, prob_num):
        ordonare = []
        self.formeaza_lista_studenti(ordonare, 0, len(self.__repo_students.getStudents()), self.__repo_students.getStudents(), prob_lab, prob_num)
        # studenti = self.__repo_students.getStudents()
        # for student in studenti:
        #     if self.__repo_assignments.getnota(str(student.getId()), prob_lab, prob_num) != None:
        #         lista.append(student)
        if len(ordonare) == 0:
            raise RepositoryException1("Nu exista studenti care sa aibe note la aceasta problema")
        else:
            return ordonare

    def ordoneaza_dupa_nume (self, lista):
        """
        Elementele sunt Primi10DTO
        """
        i = 0
        while i < len(lista) - 1:
            ordonare = []
            inceput = -1
            while lista[i].get_nota() == lista[i+1].get_nota():
                inceput = i
                ordonare.append(lista[i])
                i += 1
            if i != 0 and lista[i].get_nota() == lista[i-1].get_nota():
                ordonare.append(lista[i])
            if len(ordonare) != 0:
                gnomeSort(ordonare, key = lambda x : x.get_nume()) #(key = lambda x : x.get_nume())
                lista[inceput : i+1] = ordonare
            i += 1

        return lista

    def primi_10 (self, prob_lab, prob_num):
        lista_ordonata = self.ordoneaza_pentru_primi_10(prob_lab, prob_num)

        return lista_ordonata[:len(lista_ordonata) // 10]

    def ordoneaza_pentru_primi_10 (self, prob_lab, prob_num):
        ordonare = []
        studenti = self.__get_studenti_with_problem(prob_lab, prob_num)
        for student in studenti:
            nota = self.__repo_assignments.getnota(str(student.getId()), prob_lab, prob_num)
            primi_10 = Primi10Dto(student.getId(), student.getnume(), nota)
            ordonare.append(primi_10)
        quickSortRec(ordonare, 0, len(ordonare) - 1, key = lambda x : x.get_nota())#(key = lambda x : x.get_nota())

        return self.ordoneaza_dupa_nume(ordonare)

def test_ordoneaza_pentru_primi_10 ():
    repo_for_students = Reposity_for_Students()
    repo_for_problems = Reposity_for_Problems()
    repo_for_assignments = Assignments_for_Students()
    serv_assignments = Service_for_Assignments(repo_for_assignments, repo_for_students, repo_for_problems)

    stud1 = Student("7", "Stefan", "211")
    repo_for_students.store(stud1)
    stud2 = Student("8", "Cezar", "212")
    repo_for_students.store(stud2)
    stud3 = Student("9", "Andrei", "213")
    repo_for_students.store(stud3)
    stud4 = Student("10", "Berila", "214")
    repo_for_students.store(stud4)
    stud5 = Student("11", "Claudiu", "700")
    repo_for_students.store(stud5)

    prob1 = Problema("1", "2", "Descriere1", "Deadline1")
    repo_for_problems.store(prob1)
    prob2 = Problema("3", "4", "Descriere2", "Deadline2")
    repo_for_problems.store(prob2)

    serv_assignments.assign_problem("7", "1", "2")
    serv_assignments.assign_problem("8", "1", "2")
    serv_assignments.assign_problem("9", "1", "2")
    serv_assignments.assign_problem("10", "1", "2")
    serv_assignments.assign_problem("11", "1", "2")

    serv_assignments.evaluate_problem("7", "1", "2", 9)
    serv_assignments.evaluate_problem("8", "1", "2", 8)
    serv_assignments.evaluate_problem("9", "1", "2", 8)
    serv_assignments.evaluate_problem("10", "1", "2", 4)

    lista_sortata = serv_assignments.ordoneaza_pentru_primi_10("1", "2")
    assert len(lista_sortata) == 4
    assert lista_sortata[0].get_nume() == "Berila"
    assert lista_sortata[1].get_nume() == "Andrei"
    assert lista_sortata[2].get_nume() == "Cezar"
    assert lista_sortata[3].get_nume() == "Stefan"

def test_ordoneaza_dupa_nume ():
    repo_for_students = Reposity_for_Students()
    repo_for_problems = Reposity_for_Problems()
    repo_for_assignments = Assignments_for_Students()
    serv_assignments = Service_for_Assignments(repo_for_assignments, repo_for_students, repo_for_problems)

    stud1 = Primi10Dto(1, "Stefan", 10)
    stud2 = Primi10Dto(2, "Andrei", 10)
    stud3 = Primi10Dto(3, "Berila", 7)
    lista = [stud1, stud2, stud3]
    serv_assignments.ordoneaza_dupa_nume(lista)
    assert lista[0].get_nume() == "Andrei"
    assert lista[1].get_nume() == "Stefan"
    assert lista[2].get_nume() == "Berila"
def toti_sub5test ():
    repo_for_students = Reposity_for_Students()
    repo_for_problems = Reposity_for_Problems()
    repo_for_assignments = Assignments_for_Students()
    serv_assignments = Service_for_Assignments(repo_for_assignments, repo_for_students, repo_for_problems)

    stud1 = Student("7", "Stefan", "211")
    repo_for_students.store(stud1)
    stud2 = Student("8", "Andrei", "212")
    repo_for_students.store(stud2)
    stud3 = Student("9", "Cezar", "213")
    repo_for_students.store(stud3)
    stud4 = Student("10", "Berila", "214")
    repo_for_students.store(stud4)

    prob1 = Problema("1", "2", "Descriere1", "Deadline1")
    repo_for_problems.store(prob1)
    prob2 = Problema("1", "4", "Descriere2", "Deadline2")
    repo_for_problems.store(prob2)

    serv_assignments.assign_problem("7", "1", "2")
    serv_assignments.assign_problem("8", "1", "2")
    serv_assignments.assign_problem("9", "1", "2")
    serv_assignments.assign_problem("10", "1", "2")
    serv_assignments.assign_problem("7", "1", "4")
    serv_assignments.assign_problem("8", "1", "4")
    serv_assignments.assign_problem("9", "1", "4")
    serv_assignments.assign_problem("10", "1", "4")

    serv_assignments.evaluate_problem("7", "1", "2", 4)
    serv_assignments.evaluate_problem("8", "1", "2", 3)
    serv_assignments.evaluate_problem("9", "1", "2", 8)
    serv_assignments.evaluate_problem("10", "1", "2", 4)
    serv_assignments.evaluate_problem("7", "1", "4", 3)
    serv_assignments.evaluate_problem("8", "1", "4", 8)
    serv_assignments.evaluate_problem("9", "1", "4", 3)
    serv_assignments.evaluate_problem("10", "1", "4", 2)

    ordonat = []
    #print (serv_assignments.medie_lab("10","1"))
    ordonat = serv_assignments.toti_sub5("1")
    for student in ordonat:
        #print(student.get_medie())
        assert student.get_medie() < 5
    assert len(ordonat) == 2

def ordoneaza_numetest ():
    repo_for_students = Reposity_for_Students()
    repo_for_problems = Reposity_for_Problems()
    repo_for_assignments = Assignments_for_Students()
    serv_assignments = Service_for_Assignments(repo_for_assignments, repo_for_students, repo_for_problems)

    stud1 = Student("7", "Stefan", "211")
    repo_for_students.store(stud1)
    stud2 = Student("8", "Andrei", "212")
    repo_for_students.store(stud2)
    stud3 = Student("9", "Cezar", "213")
    repo_for_students.store(stud3)
    stud4 = Student("10", "Berila", "214")
    repo_for_students.store(stud4)

    prob1 = Problema("1", "2", "Descriere1", "Deadline1")
    repo_for_problems.store(prob1)
    prob2 = Problema("3", "4", "Descriere2", "Deadline2")
    repo_for_problems.store(prob2)

    serv_assignments.assign_problem("7", "1", "2")
    serv_assignments.assign_problem("8", "1", "2")
    serv_assignments.assign_problem("9", "1", "2")
    serv_assignments.assign_problem("10", "1", "2")

    serv_assignments.evaluate_problem("7", "1", "2", 10)
    serv_assignments.evaluate_problem("8", "1", "2", 9)
    serv_assignments.evaluate_problem("9", "1", "2", 8)

    ordonat = []
    ordonat = serv_assignments.ordoneaza_nume("1","2")
    #print(ordonat)
    #print(ordonat[0].getId(), ordonat[1].getId(), ordonat[2].getId(), ordonat[3].getId())
    assert ordonat[0].getId() == 8
    assert ordonat[1].getId() == 10
    assert ordonat[2].getId() == 9
    assert ordonat[3].getId() == 7

def assignproblemtest ():
    repo_for_students = Reposity_for_Students()
    repo_for_problems = Reposity_for_Problems()
    repo_for_assignments = Assignments_for_Students()
    serv_assignments = Service_for_Assignments(repo_for_assignments, repo_for_students, repo_for_problems)

    try:
        serv_assignments.assign_problem("7", "1", "2")
        assert False
    except RepositoryException as ex:
        assert str(ex) == "id - ul nu exista"
    
    stud1 = Student("7", "Stefan", "210")
    repo_for_students.store(stud1)
    try:
        serv_assignments.assign_problem("7", "1", "2")
        assert False
    except RepositoryException1 as ex:
        assert str(ex) == "numarul problemei nu exista"

    prob1 = Problema("1", "2", "Descriere1", "Deadline1")
    repo_for_problems.store(prob1)
    try:
        serv_assignments.assign_problem("7", "1", "2")
    except Exception:
        assert False
    prob_assignata = serv_assignments.get_problema_assignata("7", "1", "2")
    assert prob_assignata.getdescriere() == prob1.getdescriere()
    assert serv_assignments.get_size(str(stud1.getId())) == 1

    try:
        serv_assignments.assign_problem("7", "1", "2")
        assert False
    except AssignmentException as ex:
        assert str(ex) == "aceasta problema a fost deja atribuita studentului"

assignproblemtest()
ordoneaza_numetest()
toti_sub5test()
test_ordoneaza_dupa_nume()
test_ordoneaza_pentru_primi_10()