import ast


def read_lines(filepath):
    """ file to lines """
    with open(filepath, "r") as f:
        lines = f.readlines()

    return lines


def count_lines_of_code(filepath):
    """ Count number of lines in code"""
    lines = read_lines(filepath)

    return len(lines)


def count_blank(filepath):
    """ Count number of blanks in file """
    num_blank = 0
    lines = read_lines(filepath)

    for aline in lines:
        if aline.strip() == '':
            num_blank += 1

    return num_blank


def count_comment(filepath):
    """ Count number of comments in file """
    num_comment = 0
    lines = read_lines(filepath)
    # num_comment = hash(#) comment + quote(""") comment


def count_hash(stripped_line):
    """ Count number of hash(#) comment """
    num_hash = 0
    first = stripped_line[:1]

    if '#' in stripped_line:
        if first == ['#']:
            num_hash = 0
        elif hash_in_string(stripped_line, '"'):
            num_hash = 0
        elif hash_in_string(stripped_line, "'"):
            num_hash = 0
        else:
            num_hash = 1

    return num_hash


def hash_in_string(stripped_line, quote):
    """ Check whether hash(#) is in string """
    quote_is_open = False
    hash_in_str = False
    quote_can_in_str = False

    compare_quote = ""
    if quote == '"':
        compare_quote = '"'
    if quote == "'":
        compare_quote = "'"

    for item in stripped_line:
        if item == '\\' and quote_is_open and not quote_can_in_str:
            quote_can_in_str = True
            continue
        elif quote_is_open and quote_can_in_str:
            quote_can_in_str = False
            continue

        if item == compare_quote:
            if not quote_is_open:
                quote_is_open = True
            else:
                quote_is_open = False

        if item == '#':
            if quote_is_open:
                hash_in_str = True
            else:
                hash_in_str = False

    return hash_in_str


def count_three_quotes(stripped_line, quote_is_open, double_quote_is_open):
    """ Count number of quotes comment """
    num_quotes = 0

    quotes_pair = check_three_quotes(stripped_line, "'", quote_is_open)
    double_quotes_pair = check_three_quotes(stripped_line, '"', double_quote_is_open)

    """ single quote """
    if quotes_pair == 2 and not quote_is_open:
        num_quotes += 1
    elif quotes_pair == 1:
        if not quote_is_open:
            quote_is_open = True
        else:
            quote_is_open = False
        num_quotes += 1
    else:
        if quote_is_open and quotes_pair != -1:
            num_quotes += 1

    """ double quote """
    if double_quotes_pair == 2 and not double_quote_is_open:
        num_quotes += 1
    elif double_quotes_pair == 1:
        if not double_quote_is_open:
            double_quote_is_open = True
        else:
            double_quote_is_open = False
        num_quotes += 1
    else:
        if double_quote_is_open and double_quotes_pair != -1:
            num_quotes += 1

    return num_quotes, quote_is_open, double_quote_is_open


def check_three_quotes(aline, quote, quote_open):
    """ Check whether three quote comment is exist """
    stripped_line = list(aline.strip())

    if not stripped_line:
        return -1

    compare_quote = ''
    encase_quote = ''

    if quote == '"':
        compare_quote = '"'
        encase_quote = "'"
    elif quote == "'":
        compare_quote = "'"
        encase_quote = '"'

    stack_open = []
    stack_close = []
    full = 3

    is_encase_open = False
    encase_stack = 0
    encase_full = 2

    paren_is_open = [False, False, False]

    for item in stripped_line:
        if item == '#' and not quote_open:
            # when quotes are in hash(#) comment
            return 0
        if item == '=' and not quote_open:
            # when quotes assign to some variable
            return 0

        # when quote is in parentheses
        if item == '(' and stack_open != full:
            paren_is_open[0] = True
        elif item == ')':
            paren_is_open[0] = False
        elif item == '{' and stack_open != full:
            paren_is_open[1] = True
        elif item == '}':
            paren_is_open[1] = False
        elif item == '[' and stack_open != full:
            paren_is_open[2] = True
        elif item == ']':
            paren_is_open[2] = False

        if not paren_is_open[0] and not paren_is_open[1] and not paren_is_open[2]:
            if item == compare_quote:
                if len(stack_open) < full and len(stack_close) < full:
                    stack_open.append(item)
                elif len(stack_open) == full:
                    stack_close.append(item)
                else:
                    continue
            elif item == encase_quote:
                # if quotes are in the other quotes
                # Example: '"""' or "'''"
                if not is_encase_open:
                    encase_stack += 1
                    is_encase_open = True
                elif is_encase_open:
                    encase_stack += 1
                    if encase_stack > encase_full:
                        encase_stack = 0
                        is_encase_open = False
            else:
                if len(stack_open) != full:
                    stack_open.clear()
                if len(stack_close) != full:
                    stack_close.clear()

    if len(stack_open) == full and len(stack_close) == full:
        return 2  # a quote comment is open and close
    elif len(stack_open) == full:
        return 1  # a quote comment is just open or close
    else:
        return 0


def parse_file(filepath):
    """ Parsing file to AST """
    with open(filepath, "r") as f:
        return ast.parse(f.read(), filename=filepath)


def count_function(filepath):
    """ Count number of functions in file with AST """
    ptree = parse_file(filepath)
    num_func = 0

    for item in ast.walk(ptree):
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            num_func += 1

    return num_func
