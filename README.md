## Weather Task


### How to Run:


First Rename the header of all files (trimming the spaces in file columns name)
```commandline
python3 files_data_cleaner.py
```

> For Question 1:
```bash

python3 main.py /path-to-files -e {year}

ex: 
`python3 main.py /weatherfiles -e 2005`

```

> For Question 2:
```bash

python3 main.py /path-to-files -a {year}/{month_number}

ex: 
`python3 main.py /weatherfiles -a 2006/6`

```



> For Question 3:
```bash
python3 main.py /path-to-files -c {year}/{month_number}

ex: 
`python3 main.py /weatherfiles -c 2005/3`

```



> For Question 4:
```bash

python3 main.py /path-to-files -e {year} -a {year}/{month} -c {year}/{month}

ex: 
`python3 main.py /weatherfiles -c 2009/5 -e 2005 -a 2014/4`

```


> For Question 5:
```bash

python3 main.py /path-to-files -cs {year}/{month_number}

ex: 
`python3 main.py /weatherfiles -cs 2005/8`
# c --> charts, s --> single line
```







### Code Output:

#### 1- High Temperature, Low Temperature and Humidity

![Image of Question 1](./images/task1.png)

<br />

#### 2- Average Highest Temperature, Average Lowest Temperature and Average mean Humidity

![Image of Question 2](./images/task2.png)

<br />

#### 3- Charts for Highest Temperature and Lowest Temperature on Each day

![Image of Question 3](./images/task3.png)

<br />

#### 4- Multiple Reports

This task is long on terminal, so can't capture a image

<br />

#### 5- Charts for Highest Temperature and Lowest Temperature on Each day in One line

![Image of Question 5](./images/task4.png)

<br />

