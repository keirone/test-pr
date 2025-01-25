class Control :
    # UI에서 입력되는 이벤트 처리, 동작제어 관련
    def __init__(self, view) :
        self.view = view
        self.connectSignals()

    def calculate(self) :
        num1 = float(self.view.le1.text()) # 첫번째 LineEdit에 입력된 text를 읽어들이고 부동소수점으로 변환
        num2 = float(self.view.le2.text())
        operator = self.view.cb.currentText()  # Combobox에 선택된 연산자

        if operator == "+" :
            return f"{num1} + {num2} = {self.sum(num1, num2)}"
        elif operator == "-" :
            return f"{num1} - {num2} = {self.sub(num1, num2)}"
        elif operator == "*" :
            return f"{num1} * {num2} = {self.mul(num1, num2)}"
        elif operator == "/" :
            return f"{num1} / {num2} = {self.div(num1, num2)}"
        
        else :
            return "Calculation Error"

    def connectSignals(self) :
        self.view.btn1.clicked.connect(lambda : self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a,b) :
        return str(a+b)
        # 예외 처리는 앞으로 calculate함수에서 수행한다.

    def sub(self, a, b) :
        return a-b
    
    def mul(self, a, b) :
        return a * b
    
    def div(self, a, b) :
        try :
            if b == 0 :
                raise Exception("Divisor Error")
        except Exception as e :
            return e
        
        return a / b
