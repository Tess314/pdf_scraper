import tabula as tb #PDF tables to DataFrames
import pandas as pd
import re

file = 'bee_file.pdf'

data = tb.read_pdf(file, pages = '1')

print(data)
