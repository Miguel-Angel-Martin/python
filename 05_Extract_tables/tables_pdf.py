import camelot

table = camelot.read_pdf('05_Extract_tables/table.pdf', pages='1')
print(table)

table.export('05_Extract_tables/table.csv', f='csv', compress=False)
