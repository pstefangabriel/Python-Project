from Repository.Student_repository import Reposity_for_Students
from domain.entities import Student
from domain.validator import StudentValidator
from domain.entities import InitializareException
from domain.validator import ValidatorException
from Repository.Student_repository import RepositoryException

class StudentService:
    """
    Servcie pentru studenti
    Domain: repositary : Reposity_for_Studemts
            validator : StudentValidator
    """
    
    def __init__ (self, repositary, validator):
        """
        Initializarea service
        repository : object that stores the students
        validator : object that validates the students
        """
        self.__rep = repositary
        self.__val = validator

    def CreateStudent (self, id, nume, grup):
        """
        Coordoneaza creearea studentului si il returneaza
        Preconditii: id - string
                     nume - string
                     grup - string
        Postconditii: un student valid pus introdus in repository
        Raises: InitializareException
                ValidatorException
                RepositoryException
        """
        st = Student(id, nume, grup)
        self.__val.validate(st)
        self.__rep.store(st)

        return st
    
    def DeleteStudent (self, id):
        """
        Coordoneaza stergerea unui student
        Preconditii: id - string
        postconditii: daca exista id - ul atunci studentul este sters
        Raises: RepositoryException daca nu exista un student cu acel id
        """
        self.__rep.delete(id)

    def ModifyStudent (self, id, nume, grupa):
        """
        Coordoneaza modificarea unui student
        Preconditii: id - string
                     nume - string
                     grupa - string
        Posconditii: daca id ul exista atunci userul a fost modificat id : string valid (este un numar intreg > 0)
                                                                      nume : string nevid
                                                                      grupa int > 0
        Raises: RepositoryException cu mesaj : string
                    "id - ul nu exista"
                IntializareException
                ValidatorException
        """
        st = Student(id, nume, grupa)
        self.__val.validate(st)
        self.__rep.modify(id, nume, grupa)

    def getstudent (self, id):
        """
        id - string
        """
        stud = self.__rep.getStudent(id)
        return stud.getnume(), stud.getgrupa()


    def getAllStudents (self):
        return self.__rep.getStudents()

def testmodifystudent ():
    rep = Reposity_for_Students()
    val = StudentValidator()
    service = StudentService(rep, val)
    
    student1 = service.CreateStudent("1","Ion","3")
    student2 = service.CreateStudent("10", "Stefan", "2")
    service.ModifyStudent("1", "Pintilie", "11")
    allstudents = service.getAllStudents()
    assert allstudents[1].getId() == 1
    assert allstudents[1].getnume() == "Pintilie"
    assert allstudents[1].getgrupa() == 11
    try:
        service.ModifyStudent("1", "ceva", "-5")
        assert False
    except ValidatorException as ex:
        assert str(ex) == "grupa nu este un numar intreg > 0\n"

def testDeleteStudent ():
    rep = Reposity_for_Students()
    val = StudentValidator()
    service = StudentService(rep, val)
    
    student1 = service.CreateStudent("1","Ion","3")
    student2 = service.CreateStudent("10", "Stefan", "2")
    service.DeleteStudent("10")
    allstudents = service.getAllStudents()
    assert allstudents[0].getId() == student1.getId()
    assert len(allstudents) == 1
    try:
        service.DeleteStudent("10")
        assert False
    except RepositoryException as ex:
        assert str(ex) == "studentul nu exista in reposit"

def testCreateStudent ():
    rep = Reposity_for_Students()
    val = StudentValidator()
    service = StudentService(rep, val)
    
    student = service.CreateStudent("1","Ion","3")
    allstudents = service.getAllStudents()
    assert student.getId() == allstudents[0].getId()
    assert len(allstudents) == 1
    try:
        student_bad = service.CreateStudent("1","Ion","3te")
        assert False
    except InitializareException as ex:
        assert str(ex) == "grupa nu este un numar intreg\n"
    try:
        student_bad = service.CreateStudent("1", "cineva", "45")
        assert False
    except RepositoryException as ex:
        assert str(ex.get_errors()) == "id - ul trebuie sa fie unic"

testCreateStudent()
testDeleteStudent()
testmodifystudent()