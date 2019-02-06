

def huehue():
    print("Ala")


def card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}"\
             " Flight: {1}"\
             " Seadt: {2}"\
             " Aircraft {3}"\
             " |".format(passenger, flight_number, seat, aircraft)
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)