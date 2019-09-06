from anytree import Node, RenderTree

#Nivel 0
Madre = Node("Madre")

#Nivel 1 Programa
ADMI = Node("ADMI", parent=Madre)
ISIS = Node("ISIS", parent=Madre)
IMEC = Node("IMEC", parent=Madre)
IIND = Node("IEND", parent=Madre)
IQUI = Node("IQUI", parent=Madre)
IBIO = Node("IBIO", parent=Madre)
IELE = Node("IELE", parent=Madre)
ICYA = Node("ICYA", parent=Madre)
ARTE = Node("ARTE", parent=Madre)
CPOL = Node("CPOL", parent=Madre)
DISE = Node("DISE", parent=Madre)
FILO = Node("FILO", parent=Madre)
MATE = Node("MATE", parent=Madre)
FISI = Node("FISI", parent=Madre)
GEOC = Node("GEOC", parent=Madre)
QUIM = Node("QUIM", parent=Madre)
BIOG = Node("BIOG", parent=Madre)
LITE = Node("LITE", parent=Madre)
LENG = Node("LENG", parent=Madre)
MUSI = Node("MUSI", parent=Madre)
PSIC = Node("PSIC", parent=Madre)

#Nivel 2 Curso//Nombre 
1001 = Node("1001", parent=Madre)


#Nivel 3 Sección/Horario


