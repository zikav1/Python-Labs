class ExamResult:

    def __init__(self,course_code, date, grade_limits):
        self._course_code = course_code
        self._date = date
        self._grade_limits = grade_limits
        self._results = {}
    
    #Returnerar vilket betyg poängen score motsvarar utifrån betygsgränserna.
    #Returvärdet är antingen strängen 'U', '3', '4', eller '5'
    def grade_from_score(self,score):
        if score < self._grade_limits[0]:
            return 'U'
        elif score >= self._grade_limits[0] and score < self._grade_limits[1]:
            return '3'
        
        elif score >= self._grade_limits[1] and score < self._grade_limits[2]:
            return '4'
        
        else:
            return '5'

    
    #Lägger till tentaresultatet för studenten student_id (sträng) med
    #poängen score (heltal). student_id antas vara unikt för en tenta
    def add_result(self,student_id, score):
        self._results[student_id] = score


    #Returnerar resultatet för studenten student_id som en tupel
    #bestående två av värden: poäng (heltal) och betyg (sträng).
    #Om inget resultat finns registrerat för studenten returneras None.
    def get_result(self,student_id):
        if student_id not in self._results:
            return None
        else:
            score = self._results[student_id]
            grade = self.grade_from_score(score)
            return (score, grade)
        

    #Returnerar en lista av studenter (deras id:n) sorterad i
    #bokstavsordning.
    def students(self):
        student_list = []

        for student in self._results:
            student_list.append(student)
        
        return sorted(student_list)

    #Returnerar en lista av den eller de studenter (deras id:n) som
    #fick högst poäng på tentan. Listan är sorterad i bokstavsordning.
    #Om inga resultat finns registrerade returneras en tom lista.
    def students_highest_score(self):
        highest_score_list = []
        for student in self._results:
            score = self._results[student]
            if score == self._grade_limits[2] or score > self._grade_limits[2]:
                highest_score_list.append(student)
        
        return sorted(highest_score_list)
    

    #Returnerar statistik i form av nyckel-värdetabell från betyg
    #(sträng) till en tupel bestående av antal och andel i decimalform
    #som fick det betyget. Den returnerade nyckel-värdetabellen är
    #ordnad från 'U' till '5'.
    #Exempel på returvärde (1 av 5 studenter fick betyget U osv):
    #{'U': (1, 0.2), '3': (2, 0.4), '4': (1, 0.2), '5': (1, 0.2)}
    def statistics(self):
        grades = {'U': (), '3': (), '4': (), '5': ()}

        

        return grades
            



    
    def __str__(self):
        return f'Course: {self._course_code}, Date: {self._date}, Grade limits: {self._grade_limits}'







#limits for the exam
limits = [30,40,50]

#course object
results = ExamResult('EDAA10','2020-08-30', limits)

#Student result added for the specified course
results.add_result('Hugo Rolf', 30)
results.add_result('Nils Randevik', 50)
results.add_result('Rasmus Ivarsson', 50)
results.add_result('Carl Waller', 35)
results.add_result('Carl Kjäll', 50)
results.add_result('David Petersson', 50)
results.add_result('Dafina Shehu', 30)
results.add_result('Alva Rolf', 25)

print(results.statistics())





