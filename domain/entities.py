class InitializareException(Exception):
    def __init__ (self, mesaj):
        self.__mesaj = mesaj

    def get_errors (self):
        return self.__mesaj

class Student:
    """
    Clasa pentru studenti
    Domain: studentId : int > 0
            nume : string nevid
            grup : int > 0
    Invariant: Id - ul unui student trebuie sa fie unic 
    """

    def __init__ (self, studentId, nume, grup):
        """
        Cream studentul
        Preconditii: studentId : string
                     nume : string
                     grup : string
        Postconditii un student cu Id - ul - studentId : string
                                   nume - nume : string
                                   grup - grup : int
        Raises: InitilizareException cu mesajul : string
                "id - ul nu este un numar intreg\n"
                "grupa nu este un numar intreg\n"
        """
        erori = ""
        try:
            self.__id = studentId
            studentId = int(studentId)
        except ValueError:
            erori += "id - ul nu este un numar intreg\n"
        self.__nume = nume
        try:
            self.__grup = int(grup)
        except ValueError:
            erori += "grupa nu este un numar intreg\n"
        if len(erori) > 0:
            raise InitializareException(erori)
        self.__medie = None
        

    def get_medie (self):
        return self.__medie

    def set_medie (self, val):
        self.__medie = val

    def getId (self):
        """
        Getter pentru Id
        """
        return int(self.__id)

    def getnume (self):
        """
        Getter pentru nume
        """
        return self.__nume

    def getgrupa (self):
        """
        Getter pentru grupa
        """
        return self.__grup
    


def testcreeazastudent ():
    student = Student("21", "Stefan", "10")
    assert student.getId() == 21
    assert student.getnume() == "Stefan"
    assert student.getgrupa() == 10
    try:
        student_bad = Student("ceva", "Stefan", "daca")
    except InitializareException as ex:
        assert str(ex) == "id - ul nu este un numar intreg\ngrupa nu este un numar intreg\n"

class Problema:
    """
    Clasa pentru probleme
    Domain: numar_lab : int > 0
            numar_problema : int > 0
            descriere : string nevid
            deadline : string nevid
    Invariant: Nu pot exista 2 probleme cu acelasi numar 
    """

    def __init__ (self, numar_lab, numar_prob, descriere, deadline):
        """
        Cream problema
        Preconditii: numar_lab : string
                     numar_prob : string
                     descriere : string
                     deadline : string
        Postconditii o problema cu numarul - numarul : int
                                   descriere - descriere : string
                                   deadline - deadline : string
        Raises: InitilizareException cu mesajul : string
                "numarul nu este un numar intreg\n"
        """
        erori = ""
        try:
            self.__num_lab = int(numar_lab)
            self.__num_prob = int(numar_prob)
        except ValueError:
            erori += "numarul nu este un numar intreg\n"
        self.__descriere = descriere
        self.__deadline = deadline
        if len(erori) > 0:
            raise InitializareException(erori)
        

    def getnumar_lab (self):
        """
        Getter pentru numar
        """
        return self.__num_lab

    def getnumar_prob (self):
        """
        Getter pentru numar
        """
        return self.__num_prob

    def getdescriere (self):
        """
        Getter pentru descriere
        """
        return self.__descriere

    def getdeadline (self):
        """
        Getter pentru deadline
        """
        return self.__deadline

def testcreeazaproblema ():
    prob = Problema("7", "8", "O descriere", "10 Mai")
    assert prob.getnumar_lab() == 7
    assert prob.getnumar_prob() == 8
    assert prob.getdescriere() == "O descriere"
    assert prob.getdeadline() == "10 Mai"
    try:
        prob_bad = Problema("ceva", "8", "Stefan", "daca")
    except InitializareException as ex:
        assert str(ex) == "numarul nu este un numar intreg\n"

def test ():
    testcreeazastudent()
    testcreeazaproblema()

test()


class Primi10Dto:
    def __init__ (self, id_stud, nume_stud, nota_stud):
        self.__id = id_stud
        self.__nume = nume_stud
        self.__nota = nota_stud

    def get_nota (self):
        return self.__nota

    def get_nume (self):
        return self.__nume

    def __str__ (self):
        return f"Student: {self.__nume} Nota: {self.__nota}"
