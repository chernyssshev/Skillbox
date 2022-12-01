import ast
import operator as op

OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Pow: op.pow,
    ast.BitXor: op.xor,
    ast.USub: op.neg
}


def eval_(node):
    if isinstance(node, ast.Num):
        return node.n

    elif isinstance(node, ast.BinOp):
        try:
            return OPERATORS[type(node.op)](eval_(node.left), eval_(node.right))
        except Exception as err:
            return err

    elif isinstance(node, ast.UnaryOp):
        return OPERATORS[type(node.op)](eval_(node.operand))

    else:
        raise TypeError(node)


def eval_expr(expr):
    return eval_(ast.parse(expr, mode='eval').body)


def get_edit(row_number: str, str_formula: str, str_error: str, print_error: bool = False) -> bool:
    """
    Опрашиваем пользователя о необходимости исправлении не верной формулы
    :param row_number: Номер строки в исходном файле, где произошла ошибка
    :param str_formula: Формулы, в которой ошибка
    :param str_error: Тест сообщения ошибки
    :param print_error: Нужно ли выводить описание ошибки
    :return: True/False Нужно или нет исправлять формулу
    """
    msg = f'Обнаружена ошибка в строке: {row_number} с формулой {str_formula}.'
    if print_error:
        msg += f'\nОшибка: {str_error}'
    msg += '\n⁇ Хотите исправить (Да/Yes - для исправления)? '
    answer = input(msg).lower()
    if answer == 'да' or answer == 'yes':
        return True
    return False


all_sum = 0
row_number = 0
print_error = True

with open('calc.txt', 'r', encoding='utf-8') as f_calc:
    for line in f_calc:
        row_number += 1
        line = line.replace('\n', '')
        # arr = line.split()

        while True:
            try:
                all_sum += eval_expr(line)
                break
            except (SyntaxError, TypeError) as err:
                # msg = f'Обнаружена ошибка в строке: {row_number} с формулой {line}.'
                # if print_error:
                #     msg += f'\nОшибка: {err}'
                # msg += '\n⁇ Хотите исправить? '
                # answer = input(msg).lower()
                # if answer == 'да' or answer == 'yes':

                if get_edit(str(row_number), line, err, print_error):
                    line = input('Введите исправленную строку: ')
                    # new_line = input('Введите исправленную строку: ')
                    # all_sum += eval_expr(new_line)
                else:
                    break

print('Сумма результатов:', all_sum)
