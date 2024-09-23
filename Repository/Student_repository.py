from domain.entities import Student


class RepositoryException(Exception):
    def __init__(self, mesaj):
        self.__erori = mesaj

    def get_errors(self):
        return self.__erori


class Reposity_for_Students:
    """
    Repository pentru stundeti
    Domain: st : Student
    Invariant: Nu trebuie sa existe doi 2 studenti cu acelasi id (id ul este unic)
    """

    def __init__(self):
        """
        initializarea 
        """
        self._students = {}

    def store(self, st):
        """
        Functie care adauga studentul in repository
        Preconditii: st : Student Valid
        Postconditii: st a fost adaugat in repository
        Raises: RepositoryError cu mesaj : string 
                    "id - ul trebuie sa fie unic" daca id - ul apare de mai multe ori in repository
        """
        if str(st.getId()) in self._students:
            raise RepositoryException("id - ul trebuie sa fie unic")
        else:
            self._students[str(st.getId())] = st

    def delete(self, st_id):
        """
        Functie care elimina un student din reposit
        Preconditii: st_id : string - id - ul unui student
        Postconditii: studentul este eliminat din reposit
        Raises: RepositoryException cu mesaj : string
                    "studentul nu exista in reposit"
        """
        if st_id in self._students:
            self._students.pop(st_id)
        else:
            raise RepositoryException("studentul nu exista in reposit")

    def modify(self, st_id, st_nume, st_grupa):
        """
        Functie care modifica un student din repository dupa id (daca exista) stergandu-l si adaugandu-l cu acelasi id, noul nume si noua grupa
        Preconditii: st_id : string
                     st_nume : string
                     st_grupa : string
        Postconditii: studentul este modificat  st_id : string
                                                st_nume : string
                                                st_grupa : int
        Raises: RepositoyException cu mesaj : string
                    "id - ul nu exista"
        """
        if st_id in self._students:
            self._students.pop(st_id)
        else:
            raise RepositoryException("studentul nu exista in reposit")
        self._students[str(st_id)] = Student(st_id, st_nume, st_grupa)

    def getStudent(self, st_id):
        """
        st_id : string
        """
        if st_id in self._students:
            return self._students[st_id]
        else:
            raise RepositoryException("id - ul nu exista")

    def size(self):
        return len(self._students)

    def getStudents(self):
        """
        Getter pentru toti studentii
        """
        return list(self._students.values())


def testmodify():
    rep = Reposity_for_Students()
    stud1 = Student("7", "Stefan", "10")
    rep.store(stud1)
    stud2 = Student("10", "cineva", "11")
    rep.store(stud2)
    rep.modify("7", "Pintilie", "24")
    allstudents = rep.getStudents()
    assert allstudents[1].getnume() == "Pintilie"
    assert allstudents[1].getgrupa() == 24
    try:
        rep.modify("11", "nu", "3")
        assert False
    except RepositoryException as ex:
        assert str(ex) == "studentul nu exista in reposit"


def testdelete():
    rep = Reposity_for_Students()
    stud1 = Student("7", "Stefan", "10")
    rep.store(stud1)
    stud2 = Student("10", "cineva", "11")
    rep.store(stud2)
    rep.delete("7")
    allstuds = rep.getStudents()
    assert allstuds[0].getId() == stud2.getId()
    try:
        rep.delete("7")
        assert False
    except RepositoryException as ex:
        assert str(ex) == "studentul nu exista in reposit"


def teststore():
    rep = Reposity_for_Students()
    stud1 = Student("7", "Stefan", "10")
    rep.store(stud1)
    assert rep.size() == 1
    stud2 = Student("21", "Pintilie", "30")
    rep.store(stud2)
    assert rep.size() == 2
    try:
        stud3 = Student("7", "cineva", "89")
        rep.store(stud3)
    except RepositoryException as ex:
        assert str(ex) == "id - ul trebuie sa fie unic"


teststore()
testdelete()
testmodify()
