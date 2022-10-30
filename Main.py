import numpy as np
import matplotlib.pyplot as plt

from Consts import *
from Functions import *

# --------------------------------------------------------------------------------

e = EnumEmployment()
c = EnumCategories()

emp = e.permanent
cat = c.Python

step = 1000
salary_min = 0
salary_max = 100000

px = np.linspace(salary_min, salary_max, salary_max // step)
py = px * 0

# --------------------------------------------------------------------------------

px, py, py_j, py_m, py_s = prepare_data(px, py, emp, cat)

plt.plot(px, py, '-k', lw=1)
plt.plot(px, py_j, '-g', lw=1)
plt.plot(px, py_m, '-b', lw=1)
plt.plot(px, py_s, '-r', lw=1)

plt.xlim(0 - 1000, 50000 + 1000)
plt.ylim(0 - 0.1, 1 + 0.1)

plt.title(f'Technology ({cat})')
plt.xlabel('Salary (PLN)')
plt.ylabel('Offers (%)')

plt.legend(['sum', 'junior', 'mid', 'senior'], loc=1)

plt.grid(True)

plt.savefig(f'.\img\{cat}.png')
# plt.show()
