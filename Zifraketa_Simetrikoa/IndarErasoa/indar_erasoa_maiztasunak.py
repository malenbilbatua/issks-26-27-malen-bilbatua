from collections import Counter
import string

# Euskarazko letren maiztasunaren ordena
# Maiztasun handienetik txikienera
MAIZTASUNA_EUSKERA = "airetounkklzsdgbmphxfjcyvwq"

ALFABETO = string.ascii_lowercase


def kalkulatu_maiztasunak(testua):
    letrak = [
        letra.lower()
        for letra in testua
        if letra.lower() in ALFABETO
    ]
    return Counter(letrak)

def erakutsi_maiztasunak(maiztasunak):
    print("\n=== LETREN MAIZTASUNAK ===")

    guztira = sum(maiztasunak.values())

    for letra, kopurua in maiztasunak.most_common():
        ehunekoa = kopurua / guztira * 100
        print(
            f"{letra.upper()} -> "
            f"{kopurua:3} aldiz ({ehunekoa:.2f}%)"
        )


def sortu_hasierako_ordezkapena(maiztasunak):

    ordezkapena = {}

    letra_zifratuak = [
        letra for letra, kopurua in maiztasunak.most_common()
    ]

    for i in range(
        min(len(letra_zifratuak), len(MAIZTASUNA_EUSKERA))
    ):
        ordezkapena[letra_zifratuak[i]] = MAIZTASUNA_EUSKERA[i]

    return ordezkapena


def deszifratu(testua, ordezkapena):

    emaitza = ""

    for karakterea in testua:

        letra = karakterea.lower()

        if letra in ordezkapena:

            letra_berria = ordezkapena[letra]

            if karakterea.isupper():
                letra_berria = letra_berria.upper()

            emaitza += letra_berria

        else:
            emaitza += karakterea

    return emaitza


def erakutsi_ordezkapena(ordezkapena):

    print("\n=== UNEKO ORDEZKAPENA ===")

    if not ordezkapena:
        print("Oraindik ez dago ordezkapenik.")
        return

    for zifratu, garbi in sorted(ordezkapena.items()):
        print(f"{zifratu.upper()} -> {garbi.upper()}")


def aldatu_ordezkapena(ordezkapena, zifratu, garbi):

    zifratu = zifratu.lower()
    garbi = garbi.lower()

    if zifratu not in ALFABETO:
        print("Errorea: lehen letra ez da baliozko letra bat.")
        return

    if garbi not in ALFABETO:
        print("Errorea: bigarren letra ez da baliozko letra bat.")
        return

    ordezkapena[zifratu] = garbi

    print(
        f"\nAldaketa eginda: "
        f"{zifratu.upper()} -> {garbi.upper()}"
    )


def laguntza():

    print("""
=== LAGUNTZA ===

Letra baten ordezkapena aldatzeko:

    zifratu -> jatorrizkoa

Adibidez:

    x=e

Horrek esan nahi du testu zifratuan 'x' agertzen denean
'e' bezala deszifratu behar dela.

Komandoak:

    x=e          Ordezkapen bat aldatu
    erakutsi     Uneko ordezkapena erakutsi
    maiztasuna   Letren maiztasunak erakutsi
    laguntza     Laguntza erakutsi
    irten        Programa amaitu
""")


def programa():

    print("==============================================")
    print("  ORDEZKAPEN-ZIFRAKETA SINPLEA")
    print("  MAIZTASUNEN ANALISIA")
    print("==============================================")

    testua = input("\nSartu testu zifratua:\n> ")

    # Maiztasunak kalkulatu
    maiztasunak = kalkulatu_maiztasunak(testua)

    # Hasierako ordezkapena sortu
    ordezkapena = sortu_hasierako_ordezkapena(maiztasunak)

    # Maiztasunak erakutsi
    erakutsi_maiztasunak(maiztasunak)

    # Hasierako ordezkapena erakutsi
    erakutsi_ordezkapena(ordezkapena)

    print("\n=== HASIERAKO DESZIFRATZEA ===")
    print(deszifratu(testua, ordezkapena))

    laguntza()

    # Programa interaktiboa
    while True:

        print("\n----------------------------------------------")

        komandoa = input(
            "\nZer aldatu nahi duzu? "
            "(adib. x=e): "
        ).strip().lower()

        if komandoa == "irten":
            print("\nPrograma amaitzen.")
            break

        elif komandoa == "laguntza":
            laguntza()

        elif komandoa == "erakutsi":
            erakutsi_ordezkapena(ordezkapena)

        elif komandoa == "maiztasuna":
            erakutsi_maiztasunak(maiztasunak)

        elif len(komandoa) == 3 and komandoa[1] == "=":

            zifratu = komandoa[0]
            garbi = komandoa[2]

            aldatu_ordezkapena(
                ordezkapena,
                zifratu,
                garbi
            )

            print("\n=== TESTU DESZIFRATUA ===")
            print(deszifratu(testua, ordezkapena))

        else:
            print(
                "\nKomando ezezaguna. "
                "Idatzi 'laguntza' komandoak ikusteko."
            )


if __name__ == "__main__":
    programa()



