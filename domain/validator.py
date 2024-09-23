from domain.entities import Student, Problema

class ValidatorException(Exception):
    def __init__ (self, msg):
        self.__errors = msg

    def get_errors (self):
        return self.__errors

class StudentValidator:
    """
    Clasa care valideaza studentii
    """
    def validate (self, st):
        """
        Valideaza studentul
        Preconditii: st : Student cu initializarea corecta
        Postconditii: un student valid :
                                            stundetId : string valid (un numar intreg > 0)
                                            nume : string nevid
                                            grupa : int > 0
        Raises ValidatorException cu mesaj : string
                "id - ul nu este un numar intreg > 0\n"
                "numele este vid\n"
                "grupa nu este un numar intreg > 0\n"
        """
        erori = ""
        if st.getId() <= 0:
            erori += "id - ul nu este un numar intreg > 0\n"
        if st.getnume() == "":
            erori += "numele este vid\n"
        if st.getgrupa() <= 0:
            erori += "grupa nu este un numar intreg > 0\n"
        if len(erori) > 0:
            raise ValidatorException(erori)
        
def testStudentValidator ():
    st = Student (-1,"",-2)
    validator = StudentValidator()
    try:
        validator.validate(st)
    except ValidatorException as ex:
        assert str(ex) == "id - ul nu este un numar intreg > 0\nnumele este vid\ngrupa nu este un numar intreg > 0\n"

class ProblemaValidator:
    """
    Clasa care valideaza problemele
    Domain: prob - Problema object
    """
    def validate (self, prob):
        """
        Valideaza problema
        Preconditii: prob : Problema object cu initializarea corecta
        Postconditii: o problema valida :   numar_lab : int > 0
                                            numar_prob : int > 0
                                            descriere : string nevid
                                            deadline : string nevid
        Raises ValidatorException cu mesaj : string
                "numarul nu este un numar intreg > 0\n"
                "descriere este vida\n"
                "deadline - ul este vid\n"
        """
        erori = ""
        if prob.getnumar_lab() <= 0 or prob.getnumar_prob() <= 0:
            erori += "numarul nu este un numar intreg > 0\n"
        if prob.getdescriere() == "":
            erori += "descriere este vida\n"
        if prob.getdeadline() == "":
            erori += "deadline - ul este vid\n"
        if len(erori) > 0:
            raise ValidatorException(erori)
        
def testProblemaValidator ():
    prob = Problema ("-2", "0", "", "")
    validator = ProblemaValidator()
    try:
        validator.validate(prob)
    except ValidatorException as ex:
        assert str(ex) == "numarul nu este un numar intreg > 0\ndescriere este vida\ndeadline - ul este vid\n"

testStudentValidator()
testProblemaValidator()
        