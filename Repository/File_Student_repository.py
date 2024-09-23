from Repository.Student_repository import Reposity_for_Students
from domain.entities import Student


class FileRepoStud(Reposity_for_Students):
    def __init__ (self, file_path):
        Reposity_for_Students.__init__(self)
        self.__file_path = file_path
        self.__read_all_from_file()

    def __read_all_from_file (self):
        with open(self.__file_path, "r") as f:
            self._students.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split()
                    id = parts[0]
                    nume = parts[1]
                    grupa = parts[2]
                    stud = Student(id, nume, grupa)
                    self._students[str(id)] = stud

    def get_all (self):
        self.__read_all_from_file()

        return Reposity_for_Students.getStudents(self)

    def store (self, st):
        self.__read_all_from_file()
        Reposity_for_Students.store(self, st)
        self.__write_all_to_file()

    def delete (self, id):
        self.__read_all_from_file()
        Reposity_for_Students.delete(self, id)
        self.__write_all_to_file()

    def modify (self, id, nume, grupa):
        self.__read_all_from_file()
        Reposity_for_Students.modify(self, id, nume, grupa)
        self.__write_all_to_file()
    def __write_all_to_file(self):
        with open(self.__file_path, "w") as f:
            studenti = Reposity_for_Students.getStudents(self)
            for student in studenti:
                f.write(f"{str(student.getId())} {student.getnume()} {student.getgrupa()} \n")

    def clear (self):
        f = open(self.__file_path, "w")
        f.close()


def teste ():
    file_path = "C:\\Users\\stefan\\AppData\\Local\\Programs\\Python\\Python312\\Aplicatie_Lab_7-9\\Repository\\test_student.txt"
    repo = FileRepoStud(file_path)
    repo.clear()
    stud = Student("7", "Stefan", "215")
    repo.store(stud)
    assert len(repo.get_all()) == 1
    repo.delete("7")
    assert len(repo.get_all()) == 0
    repo.store(stud)
    repo.modify("7", "Pintilie", "216")
    assert repo.getStudent("7").getnume() == "Pintilie"
    assert repo.getStudent("7").getgrupa() == 216


teste()