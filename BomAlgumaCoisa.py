from os import replace


def hora(H):
    return f"{H:.2f}".replace(".", ":")


while True:
    try:
        h = input("Quantas horas[23:59]: ").replace(':', ".").strip()
        if 0 <= float(h) < 24:
            h = float(h)
            if 0 <= h <= 11:
                print(f" Bom dia! Agora são {hora(h)}")
                break
            elif 12 <= h <= 17:
                print(f"Boa tarde! Agora são {hora(h)}")
                break
            elif 18 <= h <= 23:
                print(f"Boa noite! Agora são {hora(h)}")
                break
            else:
                print(f"Horário {h} inválido")
        else:
            print(f"Horário {h} inválido")
    except(ValueError, TypeError, KeyboardInterrupt):
        print(f"Valor Digitando {h} é invalido")
