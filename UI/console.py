#from domain.entities import Student
#from Controller_sau_services.studentservice import StudentService
from Repository.Problem_repository import RepositoryException1
from Repository.Student_repository import RepositoryException
from domain.validator import ValidatorException
from domain.entities import InitializareException
from Repository.Assignments import AssignmentException
import random
from Utilities.random_string import generate_random_string
from Utilities.random_string import generate_random_number

class Console:
    """
    Clasa pentr UI (user interface)
    Domain: service_student : StudentService object
            service_problem : ProblemService object
    """
    def __init__ (self, service_student, service_problem, service_assignment):
        """
        Initializarea clasei
        Parametri: service_student : StudentService object care coordoneaza adauga studentului in reposit
                   service_problem : ProblemService object care coordoneaza adaugarea problemei in reposit
        """
        self.__srv_student = service_student
        self.__srv_problem = service_problem
        self.__srv_assignments = service_assignment

    def __showstudents (self):
        studenti = self.__srv_student.getAllStudents()
        if len(studenti) == 0:
            print("There are no students")
        else:
            for student in studenti:
                print("Id:", student.getId(), "Nume:", student.getnume(), "Grup:", student.getgrupa())

    def __showproblems (self):
        nr_labs = self.__srv_problem.getlabs()
        if len(nr_labs) == 0:
            print("There are no problems")
        else:
            for nr_lab in nr_labs:
                probleme = self.__srv_problem.getAllProblems(nr_lab)
                for problem in probleme:
                    print("Lab:", problem.getnumar_lab(), "Numar:", problem.getnumar_prob(), "Descriere:", problem.getdescriere(), "Deadline:", problem.getdeadline())
    
    def __optiuni (self):
        print()
        self.__showstudents()
        self.__showproblems()
        print()
        print("1). Adauga un student")
        print("2). Sterge un student")
        print("3). Modifica un student")
        print("4). Cauta student")
        print("5). Adauga o problema")
        print("6). Sterge o problema")
        print("7). Modifica o problema")
        print("8). Cauta o problema")
        print("9). Asigneaza o problema unui student")
        print("10). Noteaza un student")
        print("11). Vizualizeaza assignmenturile unui student")
        print("12). Genereaza un student random")
        print("13). Genereaza o problema random")
        print("14). Ordoneaza studentii alfabetic la o problema data")
        print("15). Toti studentii cu media notelor unui laborator sub 5")
        print("16). Quit")
        print()

    def __adstudent (self):
        id = input("Introducei id - ul studentului: ")
        nume = input("Intoduceti numele studentului: ")
        grup = input("Introduceti grupa studentului: ")
        try:
            self.__srv_student.CreateStudent(id, nume, grup)
        except InitializareException as ex:   #incearca doar print(ex)
            print()
            print(ex)
        except RepositoryException as ex:
            print()
            print(ex)
        except ValidatorException as ex:
            print()
            print(ex) 

    def __adproblem (self):
        numar_lab = input("Introducei numarul labului: ")
        numar_prob = input("Introduceti numarul problemei: ")
        descriere = input("Intoduceti descrierea problemei: ")
        deadline = input("Introduceti deadlineul problemei: ")
        try:
            self.__srv_problem.CreateProblem(numar_lab, numar_prob, descriere, deadline)
        except InitializareException as ex:   #incearca doar print(ex)
            print()
            print(ex)
        except RepositoryException1 as ex:
            print()
            print(ex)
        except ValidatorException as ex:
            print()
            print(ex) 

    def __delstudent (self):
        id = input("Introduceti id - ul studentului pe care doriti sa il eliminati: ")
        try:
            self.__srv_student.DeleteStudent(id)
        except RepositoryException as ex:
            print()
            print(ex)

    def __delproblem (self):
        numar_lab = input("Introduceti numarul labului a problemei pe care doriti sa o eliminati: ")
        numar_prob = input("Introduceti numarul problemei pe care doriti sa o eliminati: ")
        try:
            self.__srv_problem.DeleteProblem(numar_lab, numar_prob)
        except RepositoryException1 as ex:
            print()
            print(ex)

    def __modifystudent (self):
        id = input("Introduceti id - ul studentului pe care doriti sa il modificati: ")
        nume = input("Introduceti noul nume: ")
        grupa = input("Introduceti noua grupa: ")
        try:
            self.__srv_student.ModifyStudent(id, nume, grupa)
        except InitializareException as ex:
            print(ex)
        except ValidatorException as ex:
            print(ex)
        except RepositoryException as ex:
            print(ex)

    def __modifyproblem (self):
        numar_lab = input("Introduceti numarul labului a problemei pe care doriti sa o modificati: ")
        numar_prob = input("Introduceti numarul problemei pe care doriti sa o modificati: ")
        descriere = input("Introduceti noua descriere: ")
        deadline = input("Introduceti noul deadline: ")
        try:
            self.__srv_problem.ModifyProblem(numar_lab, numar_prob, descriere, deadline)
        except InitializareException as ex:
            print(ex)
        except ValidatorException as ex:
            print(ex)
        except RepositoryException1 as ex:
            print(ex)

    def __findstudent (self):
        id = input("Introduceti id - ul studentului pe care doriti sa il cautati: ")
        try:
            nume, grupa = self.__srv_student.getstudent(id)
            print("Nume:",nume,"Grupa:",grupa)
            input("Press enter to go back")
        except RepositoryException as ex:
            print()
            print(ex)

    def __findproblem (self):
        numar_lab = input("Introduceti numarul labului a problemei pe care doriti sa o cautati: ")
        numar_prob = input("Introduceti numarul problemei pe care doriti sa o cautati: ")
        try:
            descriere, deadline = self.__srv_problem.getproblema(numar_lab, numar_prob)
            print("Descriere:",descriere,"Deadline:",deadline)
            input("Press enter to go back")
        except RepositoryException1 as ex:
            print()
            print(ex)

    def __assignstudent (self):
        stud_id = input("Introduceti id - ul studentului pe care doriti sa ii dati o problema: ")
        prob_lab = input("Introduceti numarul laboratorului de la care doriti sa dati problema: ")
        prob_num = input("Introduceti numarul problemei pe care doriti sa o dati: ")
        try:
            self.__srv_assignments.assign_problem(stud_id, prob_lab, prob_num)
        except RepositoryException as ex:
            print()
            print(ex)
        except RepositoryException1 as ex:
            print()
            print(ex)
        except AssignmentException as ex:
            print()
            print(ex)

    def __evaluatestudent (self):
        stud_id = input("Introduceti id - ul studentului caruia doriti sa ii dati o nota: ")
        prob_lab = input("Introduceti numarul laboratorului de la care doriti sa dati nota problemei: ")
        prob_num = input("Introduceti numarul problemei careia doriti sa ii dati nota: ")
        nota = int(input("Introduceti nota pe care doriti sa o dati: "))
        try:
            self.__srv_assignments.evaluate_problem(stud_id, prob_lab, prob_num, nota)
        except AssignmentException as ex:
            print()
            print(ex)

    def __viewassignmentsstudent (self):
        stud_id = input("Introduceti id - ul studentului pe care doriti sa ii vedeti assignmenturile: ")
        try:
            print("Studentul are problemele si notele:")
            probleme, note = self.__srv_assignments.view_assignments(stud_id)
            for problema, nota in zip(probleme, note):
                print("Labul:", problema.getnumar_lab(), "Numarul problemei:", problema.getnumar_prob(), "Nota:", nota)
            input("Press enter to go back")
        except AssignmentException as ex:
            print()
            print(ex)

    def __generaterandomstudent (self):
        stud_id = generate_random_number(2)
        nume = generate_random_string(5)
        grupa = generate_random_number(3)
        try:
            self.__srv_student.CreateStudent(stud_id, nume, grupa)
        except InitializareException as ex:   #incearca doar print(ex)
            print()
            print(ex)
        except RepositoryException as ex:
            print()
            print(ex)
        except ValidatorException as ex:
            print()
            print(ex)

    def __generaterandomproblem (self):
        numar_lab = generate_random_number(1)
        numar_prob = generate_random_number(2)
        descriere = generate_random_string(5)
        deadline = generate_random_string(5)
        try:
            self.__srv_problem.CreateProblem(numar_lab, numar_prob, descriere, deadline)
        except InitializareException as ex:   #incearca doar print(ex)
            print()
            print(ex)
        except RepositoryException1 as ex:
            print()
            print(ex)
        except ValidatorException as ex:
            print()
            print(ex)

    def __ordoneazaalfabetic (self):
        prob_lab = input("Introduceti numarul laboratului ai problemei: ")
        prob_num = input("Introduceti numarul problemei: ")
        try:
            ordonati = self.__srv_assignments.ordoneaza_nume(prob_lab, prob_num)
            for student in ordonati:
                print("Nume:",student.getnume(), "Nota:", self.__srv_assignments.get_nota(str(student.getId()), prob_lab, prob_num))
            input("Press enter to go back")
        except AssignmentException as ex:
            print()
            print(ex)

    def __afiseazatotisub5 (self):
        prob_lab = input("Introduceti numarul laboratului ai problemei: ")
        try:
            ordonati = self.__srv_assignments.toti_sub5(prob_lab)
            for student in ordonati:
                print("Nume:",student.getnume(), "Medie:", student.get_medie())
            input("Press enter to go back")
        except AssignmentException as ex:
            print()
            print(ex)

    def UI (self):
        """
        Coordoneaza UI - ul
        """
        while True:
            self.__optiuni()
            try:
                valoare = int(input("Selectati o optiune: ").strip())
                if valoare == 1:
                    self.__adstudent()
                elif valoare == 2:
                    self.__delstudent()
                elif valoare == 3:
                    self.__modifystudent()
                elif valoare == 4:
                    self.__findstudent()
                elif valoare == 5:
                    self.__adproblem()
                elif valoare == 6:
                    self.__delproblem()
                elif valoare == 7:
                    self.__modifyproblem()
                elif valoare == 8:
                    self.__findproblem()
                elif valoare == 9:
                    self.__assignstudent()
                elif valoare == 10:
                    self.__evaluatestudent()
                elif valoare == 11:
                    self.__viewassignmentsstudent()
                elif valoare == 12:
                    self.__generaterandomstudent()
                elif valoare == 13:
                    self.__generaterandomproblem()
                elif valoare == 14:
                    self.__ordoneazaalfabetic()
                elif valoare == 15:
                    self.__afiseazatotisub5()
                elif valoare == 16:
                    break
            except ValueError:
                print("Nu ati introdus o optiune valida")