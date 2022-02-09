import csv

list_ = []
with open("my_file.csv", encoding='utf-8') as file:

    tsv_file = csv.reader(file, delimiter="\t")
    for line in tsv_file:
        list_.append(line)
        print(line)

file.close()


with open('result_file.csv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for line in list_:
        tsv_writer.writerow([line])

out_file.close()

