def calc_operation(a, operator, b):
    match operator:
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "/": return int (a / b)
