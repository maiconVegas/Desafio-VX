# DESAFIO ONLINE | PROCESSO SELETIVO
# ESTÁGIO EM ANÁLISE DADOS | VEXPENSES

# Candidato: Maicon Edson

## OBSERVAÇÕES: Com ao arquivo bataset em .csv, foi utilizado Python para a consulta junto com a biblioteca pandas.
## Desse desafio consiste em responder as perguntas para testar minhas habilidades além do curriculo

###################################################################################################
##  Você deverá analisá-la e responder às perguntas abaixo:
##  1 - Quais colunas estão presentes no dataset?
##  2 - Quantos filmes estão disponíveis na Netflix?
##  3 - Quem são os 5 diretores com mais filmes e séries na plataforma?
##  4 - Quais diretores também atuaram como atores em suas próprias produções?
##  5 - Explore o dataset e compartilhe um insight ou número que você considere interessante.
###################################################################################################

###################################################################################################
#                                     RESPOSTAS
###################################################################################################

# Importando biblioteca pandas e carregando dataset
import pandas as pd
dataset = pd.read_csv('netflix_titles.csv')

###################################################################################################

##  1 - Quais colunas estão presentes no dataset?

## R: Realizando a consulta das colunas usando .columns do pandas e usando método tolist() do python
## podemos analisar as seguintes colunas:
## show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in,description

print(dataset.columns.tolist())

## SAIDA
## ['show_id', 'type', 'title', 'director', 'cast', 'country',
## 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']

###################################################################################################

##  2 - Quantos filmes estão disponíveis na Netflix?

## R: Realizando a consulta da coluna "type" que indica o tipo de conteúdo (Movie ou TV Show)
## para retornar a condição de tipo Movie ou Filmes, e usando shape[0] para retornar
## quantidades de linhas, ou seja, quantidades de filmes são:
## 6.131 Filmes que estão disponíveis na Netflix

print(dataset[dataset['type'] == 'Movie'].shape[0])

## SAIDA
## 6131

###################################################################################################

##  3 - Quem são os 5 diretores com mais filmes e séries na plataforma?

## R: Realizando a consulta da coluna "director" que indica o Diretor de um determinado filme ou série,
## com o método value_counts() do pandas para retornar os valores repetidos em ordem decrescente, e também 
## com o método head(5) do python para exibir os 5 primeiros diretores com mais séries ou filmes são:
## Rajiv Chilaka; Raúl Campos, Jan Suter; Marcus Raboy, Suhas Kadav e Jay Karas

print(dataset['director'].value_counts().head(5))

## SAIDA
## director
## Rajiv Chilaka             19
## Raúl Campos, Jan Suter    18
## Marcus Raboy              16
## Suhas Kadav               16
## Jay Karas                 14
## Name: count, dtype: int64

###################################################################################################

##  4 - Quais diretores também atuaram como atores em suas próprias produções?

## R: Realizando a consulta das colunas "director" e "cast", removendo as linhas que tenham valores 
## nulos (NaN) nessas colunas usando método dropna(). Depois, percorremos cada linha do DataFrame com iterrows() e
## verificamos se o nome do diretor aparece na lista de elenco (cast). Se o nome do diretor estiver no elenco,
## ele será adicionado a uma lista de diretores que também atuaram em suas próprias produções.

# Removendo linhas com dados ausentes e declarando lista de diretores atuantes
datasetAtuantes = dataset.dropna(subset=['director', 'cast'])
diretoresAtuantes = []
# Analisando cada linha e verificando se o nome do diretor está na lista de elenco
for index, row in datasetAtuantes.iterrows():
    if row['director'] in row['cast']:
        diretoresAtuantes.append(row['director'])
print(diretoresAtuantes)

## OS DIRETORES QUE ATUARAM EM SUAS PRODUÇÕES SÃO: SAIDA:
# ['David de Vos', 'Spike Lee', 'Ramzy Bedia, Éric Judor', 'David Oyelowo', 'Clint Eastwood',
# 'Trey Parker', 'Tommy Chong', 'Alessandra de Rossi', 'Pascal Atuma', 'Rano Karno', 'Malik Nejer',
# 'Lynn Shelton', 'Max Jabs', 'Myriam Fares', 'Clint Eastwood', 'Michael Jai White', 'Alan Alda',
# 'Barbra Streisand', 'Clint Eastwood', 'Bo Burnham', 'Jennifer Brea', 'Edward James Olmos', 'Aamir Khan',
# 'TT The Artist', 'Muharrem Gülmez', 'Mahsun Kırmızıgül', 'Amy Poehler', 'Kevin Costner',
# 'Hamisha Daryani Ahuja', 'Peter Facinelli', 'James Toback', 'Chris Rock', 'Maïwenn', 'George Clooney',
# 'Vir Das', 'Detlev Buck', 'Jon Favreau', 'Otoja Abit', 'Antonio Díaz', 'Philippe Aractingi', 'Rana Eid',
# 'Radha Blank', 'Rajat Kapoor', 'Chandra Liow', 'Isabel Sandoval', 'Steven Rinella', 'Axelle Laffont',
# 'Funke Akindele', 'Cem Yılmaz', 'Cem Yılmaz', 'Musthafa', 'Youssef Chahine', 'Youssef Chahine',
# 'Kanika Batra', 'James Franco', 'Rano Karno', 'Ramsey Nouah', 'Fouad El-Mohandes', 'He Xiaofeng',
# 'Rano Karno', 'Yılmaz Erdoğan', 'Omoni Oboli', 'Sermiyan Midyat', 'Yılmaz Erdoğan', 'Yılmaz Erdoğan',
# 'Müfit Can Saçıntı', 'Omoni Oboli', 'Malik Nejer', 'Stephanie Turner', 'Toyin Abraham', 'Cristi Puiu',
# 'Lucas Margutti', 'Angelina Jolie', 'Robert Krantz', 'David Lynch', 'Tyler Perry', 'Numa Perrier',
# 'Ravi Babu', 'Emir Kusturica', 'Odunlade Adekola', 'Omoni Oboli', 'Falz', 'Omoni Oboli', 'Omoni Oboli',
# 'Omoni Oboli', 'Mike Ezuruonye', 'Sergio Pablos', 'Parthiban', 'Gupse Özay', 'Camille Shooshani',
# 'Vijay Kumar', 'Jerry Seinfeld', 'Hepi Mita', 'Amy Poehler', 'Syamsul Yusof', 'Yılmaz Erdoğan',
# 'Alan Rickman', 'Beyoncé Knowles-Carter', 'Brie Larson', 'Amy Schumer', 'Chiwetel Ejiofor',
# 'Parambrata Chatterjee', 'Genevieve Nnaji', 'Terry Gilliam, Terry Jones', 'Kheiron', 'Rarecho',
# 'Andy Serkis', 'Nam Ron', 'Dhanush', 'Raditya Dika', 'Rana Ranbir', 'Gaurav Narayanan', 'Eric Idle',
# 'Terry Jones', 'Deep Joshi', 'Smeep Kang', 'Peter Ho', 'Felix Starck', 'Tig Notaro', 'Kagiso Lediga',
# 'Yoo Byung-jae', 'Mike Smith, John Paul Tremblay, Robb Wells', 'Mike Smith, John Paul Tremblay, Robb Wells',
# 'Mike Smith, John Paul Tremblay, Robb Wells', 'Selima Taibi', 'Noël Wells', 'Shreyas Talpade',
# 'Judah Friedlander', 'Reem Kherici', 'Mahmoud al Massad', 'Shammi Kapoor', 'Bryan Fogel', 'Maz Jobrani',
# 'Harry Chaskin', 'Stefan Brogren', 'Pat Healy', 'Arun Chidambaram', 'Cal Seville', 'Jayaprakash Radhakrishnan',
# 'Jeff Garlin', 'Lucien Jean-Baptiste', 'Jalil Lespert', 'Louis C.K.', 'Lonny Price', 'Yılmaz Erdoğan',
# 'Amy Schumer', 'Nishikant Kamat', 'Ricky Gervais', 'Chester Tam', 'Neal Brennan', 'Rohit Mittal',
# 'Ralph Macchio', 'Linas Phillips', 'Werner Herzog', 'Yvan Attal', 'Clovis Cornillac', 'Christopher Guest',
# 'Louis C.K.', 'Louis C.K.', 'Ricky Gervais', 'Sophie Robinson, Lotje Sodderland', 'Patrick Brice',
# 'Aziz Ansari', 'David Sampliner', 'Wyatt Cenac', 'Kunle Afolayan', 'Sam Upton', 'Nagesh Kukunoor',
# 'Tom Fassaert', 'Natalie Portman', 'Martin Lawrence', 'Nagesh Kukunoor', 'Mahsun Kırmızıgül',
# 'Castille Landon', 'J. Michael Long', 'Sean McNamara', 'Jerry G. Angelo', 'Tim Blake Nelson',
# 'Sarah Smith', 'Zoe Lister-Jones', 'Mike Judge', 'Joey Kern', 'Scott Martin', 'Nick Broomfield',
# 'Marianna Palka', 'Alê Abreu', 'Sridhar Rangayan', 'Simon Baker', 'David McCracken', 'Wong Jing',
# 'Kevin Smith', 'Anuranjan Premji', 'Corbin Bernsen', 'Demetri Martin', 'Chia-Liang Liu', 'Todd Standing',
# 'Charles Martin Smith', 'Mike Birbiglia', 'Nagraj Manjule', 'Luke Jurevicius', 'Asri Bendacha',
# 'George Clooney', 'Justin Chon', 'Clint Eastwood', 'Sermiyan Midyat', 'Sermiyan Midyat', 'Satish Kaushik',
# 'Ilya Naishuller', 'Kelly Noonan', 'Corey Yuen', 'Note Chern-Yim', 'Note Chern-Yim', 'Drew Casson',
# 'Sachin', 'Jonathan Baker', 'Eugenio Derbez', 'Dustin Nguyen', 'Kevin Smith', 'Trey Edward Shults',
# 'William H. Macy', 'Stephen Chow', 'M. Night Shyamalan', 'Chia-Liang Liu', 'Jenna Laurenzo', 'Werner Herzog',
# 'Stephen Chow', 'Keanu Reeves', "Tom O'Brien", 'Rahat Kazmi', 'Sachin', 'Dennis Bartok', 'Natalia Valdebenito',
# 'Oliver Stone', 'Chia Tang', 'Subhash Ghai', 'Satish Rajwade', 'Christopher Nolen', 'Michael James Regan',
# 'René Pérez Joglar', 'Pierfrancesco Diliberto', 'Sylvester Stallone', 'Sylvester Stallone',
# 'Sylvester Stallone', 'Raj Kapoor', 'Keenen Ivory Wayans', 'Jay Chou', 'Max Martini', 'Raditya Dika',
# 'Billy Bob Thornton', 'Raj B. Shetty', 'James Sweeney', 'Tommy Avallone', 'Olivier Loustau', 'Kunle Afolayan',
# 'Jenée LaMarque', 'Kunle Afolayan', 'Note Chern-Yim', 'Brad Bird', 'Giancarlo Esposito', 'Errol Morris',
# 'Russell Crowe', 'Taika Waititi', 'Chris Burkard', 'Yılmaz Erdoğan', 'Alejandro Agresti', 'Huang Lei',
# 'Zach Braff', 'Adrian Murray']

###################################################################################################

##  5 - Explore o dataset e compartilhe um insight ou número que você considere interessante.

## Um fato interessante é saber o ano que mais teve lançamentos classificados como "Dramas".
## R: Para isso, usamos o dataset para classificar os conteúdos como "Dramas". Ao filtrar a coluna
## listed_in com o método str para analisar as Strings com método contains do pandas para filtrar, 
## conseguimos analisar quais anos foram mais produtivos para este gênero. Usando value_counts(),
## dará para identificar os 10 anos com mais lançamentos de dramas, que são:
##  2018, 2019, 2017, 2016, 2020, 2015, 2021, 2014, 2013, 2012
 
# Classificando conteúdos que contém dramas
datasetDramas = dataset[dataset['listed_in'].str.contains('Dramas')]
# Analisando e retornando quantidades de dramas por ano
dramasANO = datasetDramas['release_year'].value_counts().head(10)
print(dramasANO)

## SAIDA
## 2018    413
## 2019    376
## 2017    362
## 2016    338
## 2020    322
## 2015    230
## 2021    175
## 2014    126
## 2013    101
## 2012     83

###################################################################################################