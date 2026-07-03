from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def racine_carree_entiere(n):
    if n <= 0:
        return 0
    i=1
    while i*i <= n:
        i += 1
    return i-1

def est_premier(n):
    if n < 2:
        return False
    for i in range(2, racine_carree_entiere(n)+1):
        if n % i == 0:
            return False
    return True

def semi_premier(n):
    for k in range(2,n):
        if n%k==0:
            j=n//k
            if est_premier(k) and est_premier(j):
                return True
            else:
                return False
    return False

def play():
    n=int(windows.entree.text())
    if n <= 2:
        msg = "Veuillez introduire un nombre > 2"
    elif semi_premier(n):
        msg = str(n) + " est semi-premier"
    else:
        msg = str(n) + " n'est pas semi-premier"
    windows.label_res.setText(msg)
    
app = QApplication([])
windows = loadUi("InterfaceSemiPremier.ui")
windows.show()
windows.bouton_verif.clicked.connect(play)
app.exec_()