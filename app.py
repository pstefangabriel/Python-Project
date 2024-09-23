from Repository.File_Problem_repository import FileProbRepo
from Repository.File_Student_repository import FileRepoStud
from domain.validator import StudentValidator
from domain.validator import ProblemaValidator
from Repository.Student_repository import Reposity_for_Students
from Repository.Problem_repository import Reposity_for_Problems
from Controller_sau_services.studentservice import StudentService
from Controller_sau_services.problemservice import ProblemService
from UI.console import Console


#pentru teste
from domain.entities import Problema
from domain.validator import ProblemaValidator
from Repository.Problem_repository import Reposity_for_Problems
from Controller_sau_services.problemservice import ProblemService
from Repository.Assignments import Assignments_for_Students
from Controller_sau_services.assignmentsservice import Service_for_Assignments

file_path = "C:\\Users\\stefan\\AppData\\Local\\Programs\\Python\\Python312\\Aplicatie_Lab_7-9\\students.txt"
rep_stud = FileRepoStud(file_path)
#rep_stud = Reposity_for_Students()
rep_prob = FileProbRepo("C:\\Users\\stefan\\AppData\\Local\\Programs\\Python\\Python312\\Aplicatie_Lab_7-9\\problems.txt")
#rep_prob = Reposity_for_Problems()
rep_assignments = Assignments_for_Students()
val_stud = StudentValidator()
val_prob = ProblemaValidator()
srv_student = StudentService(rep_stud, val_stud)
srv_problem = ProblemService(rep_prob, val_prob)
srv_assignments = Service_for_Assignments(rep_assignments, rep_stud, rep_prob)
application = Console(srv_student, srv_problem, srv_assignments)
application.UI()