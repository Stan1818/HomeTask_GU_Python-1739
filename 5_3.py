from itertools import islice

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б']
while len(tutors) != len(klasses):
    if len(tutors) > len(klasses):
        klasses.append(None)
result = ((i, j) for i, j in zip(tutors, klasses))
for i in result:
    print(i)
print(list(islice(result, len(tutors))))
