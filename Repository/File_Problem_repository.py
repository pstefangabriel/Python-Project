from Repository.Problem_repository import Reposity_for_Problems
from domain.entities import Problema


class FileProbRepo(Reposity_for_Problems):
    def __init__ (self, file_path):
        Reposity_for_Problems.__init__(self)
        self.__file_path = file_path
        self.__read_all_from_file()

    def __read_all_from_file(self):
        with open(self.__file_path, "r") as f:
            self._problems.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    numar_lab = parts[0]
                    numar_prob = parts[1]
                    descriere = parts[2]
                    deadline = parts[3]
                    prob = Problema(numar_lab, numar_prob, descriere, deadline)
                    Reposity_for_Problems.store(self, prob)

    def __write_all_to_file (self):
        with open(self.__file_path, "w") as f:
            nr_labs = self.getlabs()
            if len(nr_labs) != 0:
                for nr_lab in nr_labs:
                    probleme = self.getProblems(nr_lab)
                    for problem in probleme:
                        argument = str(problem.getnumar_lab()) + "," + str(problem.getnumar_prob()) + "," + str(problem.getdescriere()) + "," + str(problem.getdeadline()) + "\n"
                        f.write(argument)

    def store (self, prob):
        self.__read_all_from_file()
        Reposity_for_Problems.store(self, prob)
        self.__write_all_to_file()

    def delete (self, prob_lab, prob_num):
        self.__read_all_from_file()
        Reposity_for_Problems.delete(self, prob_lab, prob_num)
        self.__write_all_to_file()

    def modify (self, prob_lab, prob_num, descriere, deadline):
        self.__read_all_from_file()
        Reposity_for_Problems.modify(self, prob_lab, prob_num, descriere, deadline)
        self.__write_all_to_file()

    def getlabs(self):
        #self.__read_all_from_file()
        return Reposity_for_Problems.getLabs(self)

    def getProblems(self, nr_lab):
        #self.__read_all_from_file()
        return Reposity_for_Problems.getProblems(self, nr_lab)

    def clear (self):
        f = open(self.__file_path, "w")
        f.close()

def teste ():
    file_path = "C:\\Users\\stefan\\AppData\\Local\\Programs\\Python\\Python312\\Aplicatie_Lab_7-9\\Repository\\test_problems.txt"
    repo = FileProbRepo(file_path)
    repo.clear()
    prob = Problema("1", "2", "Ceva", "10 Mai")
    repo.store(prob)
    probleme = repo.getProblems("1")
    assert len(probleme) == 1
    assert probleme[0].getnumar_prob() == 2
    repo.delete("1", "2")
    assert len(repo.getProblems("1")) == 0
    repo.store(prob)
    repo.modify("1", "2", "Ceva nou", "12 Decembrie")
    probleme = repo.getProblems("1")
    assert probleme[0].getdescriere() == "Ceva nou"
    assert probleme[0].getdeadline() == "12 Decembrie"


teste()