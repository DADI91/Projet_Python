from PySide2 import QtWidgets
import currency_converter

class App(QtWidgets.QWidget) :
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Convertisser de devises")
        self.setup_ui()
        self.set_default_values()
        self.setuo_connections()
    

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_devisesFrom = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("inverser devises")

        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)
        
        
    def set_default_values(self):
        self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesFrom.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("EUR")
        
        self.spn_montant.setRange(1, 1000000)
        self.spn_montantConverti.setRange(1, 1000000)
        
        self.spn_montant.setValue(100 )
        self.spn_montantConverti.setValue(100)
        

    def setuo_connections(self):
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.spn_montantConverti.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devises)
    
    def compute(self):
        montant = self.spn_montant.value()
        devises_From = self.cbb_devisesFrom.currentText()
        devises_To = self.cbb_devisesTo.currentText()
        try:
            resultat = self.c.convert(montant, devises_From, devises_To)
        except currency_converter.currency_converter.RateNotFoundError:
            print("la convertion n'a pas fonctionné")
        else:
            self.spn_montantConverti.setValue(resultat)
         
    def inverser_devises(self): 
        print("Inverser divises")

app = QtWidgets.QApplication([])
win = App()
win.show()  
app.exec_() 