
import numpy as np
data = {
    'Job': ['Data Mining', 'CEO', 'Lawyer', 'Lawyer', 'Data Mining', 'CEO'],
    'Labouring': ['Immanuel', 'Jeff', 'Olivia', 'Maria', 'Walker', 'Obi-Wan'],
    'Salary': [4500, 30000, 6000, 5250, 5000, 35000]
}

df = pd.DataFrame(data)
gruplama = df.groupby('Salary')
for salary , group in gruplama:
    print(f"salary : {salary}")
    print(group)
