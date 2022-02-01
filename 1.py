from collections import Counter

company_counter = Counter()
total_rev = 0

count_company = input("Введите количество компаний: ")
for i in range(int(count_company)):
    company = input("Введите название компании: ")
    revenues = input("Введите выручку за каждый квартал через пробел: ").split(' ')
    for rev in revenues:
        rev = float(rev)
        company_counter[company] += rev
        total_rev += rev
avg_rev = total_rev / (int(count_company))

print(f'Средняя годовая прибыль {count_company} компаний {avg_rev}')
print(
    f'Компании с выручкой выше среднего: {" ".join(filter(lambda n: company_counter[n] > avg_rev, company_counter.keys()))}')
print(
    f'Компании с выручкой ниже среднего: {" ".join(filter(lambda n: company_counter[n] < avg_rev, company_counter.keys()))}')
