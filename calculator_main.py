import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_button = QGridLayout()
        layout_equation_solution = QGridLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation_solution = QLabel("")
        self.equation_solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addWidget(self.equation_solution)

        ## 버튼 생성 및 시그널 설정(숫자 제외)
        
        ### 사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### =, clear, backspace 버튼 생성 + ce 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")
        button_backspace = QPushButton("Backspace")
        button_ce = QPushButton("CE")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정 + ce 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        button_ce.clicked.connect(self.button_clear_clicked)

        ### 추가 버튼 생성
        button_mod = QPushButton("%")
        button_rv = QPushButton("1/x")
        button_sq = QPushButton("x²")
        button_rt = QPushButton("√x")

        ### 추가 버튼 클릭 시 시그널 설정
        button_mod.clicked.connect(lambda state, operation = "%":self.button_operation_clicked(operation))
        button_rv.clicked.connect(lambda state, operation = "**(-1)":self.button_operation_clicked(operation))
        button_sq.clicked.connect(lambda state, operation = "**2":self.button_operation_clicked(operation))
        button_rt.clicked.connect(lambda state, operation = "**(1/2)":self.button_operation_clicked(operation))

        ## 레이아웃에 추가(숫자 제외)
        
        ### 오른쪽 사이드의 버튼들을 레이아웃에 추가
        right_side_button = [button_backspace, button_division, button_product, button_minus, button_plus, button_equal]
        for i in range(6):
            layout_button.addWidget(right_side_button[i], i, 3)

        ### 나머지 버튼들을 레이아웃에 추가
        others = [[button_mod, button_ce, button_clear], [button_rv, button_sq, button_rt]]
        for i in range(2):
            for j in range(3):
                layout_button.addWidget(others[i][j], i, j)

        
        ### 숫자 버튼 생성하고, layout_button 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(15-number, 3)
                layout_button.addWidget(number_button_dict[number], x, abs(2-y))
            elif number==0:
                layout_button.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_button.addWidget(button_dot, 5, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_button.addWidget(button_double_zero, 5, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가(**행, 열, 행크기, 열크기)
        main_layout.addLayout(layout_equation_solution, 0, 0, 1, 4)
        main_layout.addLayout(layout_button, 1, 0, 6, 4)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
