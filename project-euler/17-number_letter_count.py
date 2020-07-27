def number_letter_count():
    first_19 = [
        0,
        len("one"),
        len("two"),
        len("three"),
        len("four"),
        len("five"),
        len("six"),
        len("seven"),
        len("eight"),
        len("nine"),
        len("ten"),
        len("eleven"),
        len("twelve"),
        len("thirteen"),
        len("fourteen"),
        len("fifteen"),
        len("sixteen"),
        len("seventeen"),
        len("eighteen"),
        len("nineteen")
    ];
    tenth = [
        len("twenty"),
        len("thirty"),
        len("forty"),
        len("fifty"),
        len("sixty"),
        len("seventy"),
        len("eighty"),
        len("ninety")
    ];
    hundred = len("hundred")
    thousand = len("thousand")
    _and = len("and")
    total = sum(first_19)

    for i in range(0, 8):
        total += tenth[i]*10 + sum(first_19[:10])

    first_99 = total
    for k in range(1, 10):
        total += first_19[k]*100 + hundred*100 + first_99 + _and*99

    total += first_19[1] + thousand

    return total


print(number_letter_count())