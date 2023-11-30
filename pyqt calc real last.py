import sys
from PyQt5.QtWidgets import *
from math import *
from numpy import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.tmp = 0
        self.operator = ""

    def init_ui(self):
        main_layout = QGridLayout()

        layout_button = QGridLayout()
        layout_equation_solution = QGridLayout()

        label_equation_solution = QLabel("")
        self.equation_solution = QLineEdit("")

        layout_equation_solution.addWidget(self.equation_solution)

        #사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        #추가 버튼
        button_mod = QPushButton("%")
        button_rv = QPushButton("1/x")
        button_sq = QPushButton("x^2")
        button_rt = QPushButton("x^(1/2)")

        # =, CLR, BackSpace
        button_equal = QPushButton("=")
        button_c = QPushButton("C")
        button_ce = QPushButton("CE")
        button_backspace = QPushButton("Backspace")

        #사칙 연산 클릭 시 시그널
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        # 추가 버튼 클릭 시 시그널 설정
        button_mod.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_rv.clicked.connect(lambda state, operation = "**(-1)":self.button_unary_operation_clicked(operation))
        button_sq.clicked.connect(lambda state, operation = "**2":self.button_unary_operation_clicked(operation))
        button_rt.clicked.connect(lambda state, operation = "**(1/2)":self.button_unary_operation_clicked(operation))

        button_c.clicked.connect(self.button_c_clicked)
        button_ce.clicked.connect(self.button_ce_clicked)

        # =, clr, backspace 클릭 시 시그널
        button_equal.clicked.connect(self.button_equal_clicked)
        button_c.clicked.connect(self.button_c_clicked)
        button_ce.clicked.connect(self.button_ce_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        #layout 추가
        button = [[button_mod, button_ce, button_c, button_backspace], [button_rv, button_sq, button_rt, button_division]]
        for i in range(2):
            for j in range(4):
                layout_button.addWidget(button[i][j], i, j)

        ASMD = [button_product, button_minus, button_plus, button_equal]
        for i in range(4):
            x, y = i+2, 3
            layout_button.addWidget(ASMD[i], x, y)

        #숫자 버튼 생성
        number_button_dict = {}
        for number in range(0,10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))

            if number>0:
                x, y = divmod(15-number, 3)
                layout_button.addWidget(number_button_dict[number], x, abs(2-y))
            elif number == 0:
                layout_button.addWidget(number_button_dict[number], 5, 1)

        #  소수점 버튼, 00 버튼
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_button.addWidget(button_dot, 5, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_button.addWidget(button_double_zero, 5, 0)

                                        
        main_layout.addLayout(layout_equation_solution, 0, 0, 1, 4)
        main_layout.addLayout(layout_button, 1, 0, 6, 4)

        self.setLayout(main_layout)
        self.show()


    #function

    def number_button_clicked(self, num):
        equation = self.equation_solution.text()
        equation += str(num)
        self.equation_solution.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation_solution.text()
        self.operator = operation
        self.tmp = float(equation)
        self.equation_solution.setText("")

    def binary_operate(self, equation):
        if self.operator == "%":
            self.operator == ""
            return self.tmp%equation
        elif self.operator == "/":
            self.operator = ""
            return self.tmp/equation
        elif self.operator == "*":
            self.operator = ""
            return self.tmp*equation
        elif self.operator == "-":
            self.operator = ""
            return self.tmp-equation
        elif self.operator == "+":
            self.opreator = ""
            return self.tmp + equation
        
    def button_unary_operation_clicked(self, operation):
        equation = self.equation_solution.text()
        equation = float(equation)
        if operation == "**(-1)":solution = 1/equation
        elif operation == "**2":solution = equation**2
        elif operation == "**(1/2)":solution = equation**(1/2)
        self.equation_solution.setText(str(solution))
        
    def button_equal_clicked(self):
        equation = float(self.equation_solution.text())
        solution = self.binary_operate(equation)
        self.equation_solution.setText(str(solution))

    def button_backspace_clicked(self):
        equation = self.equation_solution.text()
        equation = equation[:-1]
        self.equation_solution.setText(equation)

    def button_c_clicked(self):
        self.tmp = 0
        self.operator = ""
        self.equation.setText("")

    def button_ce_clicked(self):
        self.equation.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
