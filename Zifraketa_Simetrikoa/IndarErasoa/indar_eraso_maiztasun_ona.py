from collections import Counter


# Euskarazko letren maiztasunak
# Laborategian emandako taulan oinarrituta
maiztasun_euskara = {
    "a": 27829,
    "i": 19649,
    "r": 16598,
    "e": 16372,
    "t": 15087,
    "o": 12941,
    "u": 11173,
    "n": 10033,
    "k": 8476,
    "l": 8103,
    "z": 6938,
    "s": 6927,
    "d": 5225,
    "g": 5206,
    "b": 4797,
    "m": 3846,
    "p": 3455,
    "h": 2223,
    "x": 1244,
    "f": 1168,
    "j": 675,
    "c": 54,
    "y": 40,
    "w": 26,
    "q": 7
}


def maiztasunak_kontatu(testua):
    """
    Testu zifratuan letra bakoitza zenbat aldiz agertzen den kontatzen du.
    """
    zenbaketak = Counter()

    for c in testua.lower():
        if c in maiztasun_euskara:
            zenbaketak[c] += 1

    return zenbaketak


def erakutsi_maiztasunak(zenbaketak):
    """
    Testu zifratuaren letren maiztasunak erakusten ditu,
    handienetik txikienera.
    """
    print("\nTESTU ZIFRATUAREN MAIZTASUNAK:")
    print("--------------------------------")

    for letra, kopurua in sorted(
        zenbaketak.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"{letra} -> {kopurua}")


def sortu_hasierako_ordezkapena(zenbaketak):
    """
    Maiztasunen arabera hasierako ordezkapen-proposamen bat sortzen du.

    Testuko letra ohikoenak euskarazko letra ohikoenekin
    lotzen ditu.
    """
    letra_zifratuak = sorted(
        zenbaketak,
        key=zenbaketak.get,
        reverse=True
    )

    letra_euskara = sorted(
        maiztasun_euskara,
        key=maiztasun_euskara.get,
        reverse=True
    )

    ordezkapena = {}

    kopurua = min(len(letra_zifratuak), len(letra_euskara))

    for i in range(kopurua):
        ordezkapena[letra_zifratuak[i]] = letra_euskara[i]

    return ordezkapena


def deszifratu_ordezkapenarekin(testua, ordezkapena):
    """
    Ordezkapen-taula erabiliz testua deszifratzen du.
    Oraindik mapatu gabeko letrak '_' bezala erakusten ditu.
    """
    emaitza = ""

    for c in testua:

        if c.isalpha():

            letra = c.lower()

            if letra in ordezkapena:
                berria = ordezkapena[letra]

                if c.isupper():
                    emaitza += berria.upper()
                else:
                    emaitza += berria
            else:
                emaitza += "_"

        else:
            # Espazioak eta puntuazio-markak mantendu
            emaitza += c

    return emaitza


def erakutsi_ordezkapena(ordezkapena):
    """
    Une honetan dagoen ordezkapen-taula erakusten du.
    """
    print("\nORDEZKAPEN-TAULA:")
    print("------------------")

    if not ordezkapena:
        print("Oraindik ez dago ordezkapenik.")
        return

    for zifratu, jatorrizko in sorted(ordezkapena.items()):
        print(f"{zifratu} -> {jatorrizko}")


def aldatu_ordezkapena(ordezkapena, zifratu, jatorrizko):
    """
    Ordezkapen berri bat gehitzen du.
    Substituzio sinple batean letra bakoitzak letra bakarra
    ordezka dezakeenez, gatazkak ezabatzen dira.
    """

    zifratu = zifratu.lower()
    jatorrizko = jatorrizko.lower()

    # Zifratu hori aurretik beste letra batekin lotuta bazegoen,
    # lotura hori ezabatu.
    if zifratu in ordezkapena:
        del ordezkapena[zifratu]

    # Jatorrizko letra beste zifratu batekin lotuta badago,
    # lotura hori ezabatu.
    ezabatzeko = []

    for letra, balioa in ordezkapena.items():
        if balioa == jatorrizko:
            ezabatzeko.append(letra)

    for letra in ezabatzeko:
        del ordezkapena[letra]

    # Ordezkapen berria gorde
    ordezkapena[zifratu] = jatorrizko


def programa():
    print("ORDEZKAPEN SINPLEAREN AURKAKO INDAR ERASOA")
    print("============================================\n")

    # Erabiltzaileak testu zifratua sartzen du
    mezu_zifratua = input("Sartu testu zifratua:\n")

    # Frekuentziak kalkulatu
    zenbaketak = maiztasunak_kontatu(mezu_zifratua)

    # Frekuentziak erakutsi
    erakutsi_maiztasunak(zenbaketak)

    # Hasierako proposamena sortu
    ordezkapena = sortu_hasierako_ordezkapena(zenbaketak)

    print("\nHASIERAKO ORDEZKAPEN-PROPOSAMENA:")
    print("----------------------------------")
    erakutsi_ordezkapena(ordezkapena)

    print("\nHASIERAKO DESZIFRATZEA:")
    print("------------------------")
    print(deszifratu_ordezkapenarekin(mezu_zifratua, ordezkapena))

    while True:

        print("\n-----------------------------------")
        print("\nKOMANDOAK:")
        print("  p=a       -> 'p' letra zifratuak 'a' esan nahi du")
        print("  maiztasunak -> maiztasunak berriro erakutsi")
        print("  ordezkapena -> uneko ordezkapena erakutsi")
        print("  garbitu   -> ordezkapen guztiak ezabatu")
        print("  irten     -> programa amaitu")
        
        aukera = input(
            "Sartu ordezkapena (adib. p=a) edo komando bat: "
        ).strip().lower()

        # Programa amaitu
        if aukera == "irten":
            print("Programa amaitu da.")
            break

        # Maiztasunak berriro erakutsi
        if aukera == "maiztasunak":
            erakutsi_maiztasunak(zenbaketak)
            continue

        # Ordezkapena erakutsi
        if aukera == "ordezkapena":
            erakutsi_ordezkapena(ordezkapena)
            continue

        # Ordezkapen guztiak ezabatu
        if aukera == "garbitu":
            ordezkapena.clear()
            print("Ordezkapen guztiak ezabatu dira.")
            print(
                deszifratu_ordezkapenarekin(
                    mezu_zifratua,
                    ordezkapena
                )
            )
            continue

        # "p=a" formatua egiaztatu
        if "=" not in aukera:
            print("Formatua okerra da. Adibidea: p=a")
            continue

        zatiak = aukera.split("=")

        if len(zatiak) != 2:
            print("Formatua okerra da. Adibidea: p=a")
            continue

        zifratu = zatiak[0].strip()
        jatorrizko = zatiak[1].strip()

        # Letra bakarra izan behar da bi aldeetan
        if len(zifratu) != 1 or len(jatorrizko) != 1:
            print("Letra bakarra sartu behar duzu alde bakoitzean.")
            continue

        if not zifratu.isalpha() or not jatorrizko.isalpha():
            print("Letra alfabetikoak bakarrik erabil daitezke.")
            continue

        # Ordezkapena aldatu
        aldatu_ordezkapena(
            ordezkapena,
            zifratu,
            jatorrizko
        )

        # Emaitza erakutsi
        print("\nDESZIFRATUTAKO TESTUA:")
        print("-----------------------")
        print(
            deszifratu_ordezkapenarekin(
                mezu_zifratua,
                ordezkapena
            )
        )


programa()
