
def xor_zifratzea(mezua, gakoa):

    kriptograma = bytearray()

    for i in range(len(mezua)):
        kriptograma.append(mezua[i] ^ gakoa[i])

    return bytes(kriptograma)


# ==========================================
# PROGRAMA NAGUSIA
# ==========================================

mezua = input("Sartu mezua: ").encode()
gakoa = input("Sartu gakoa: ").encode()

# Luzerak egiaztatu
if len(mezua) != len(gakoa):
    print("\nErrorea: mezuak eta gakoak luzera bera izan behar dute.")
    print(f"Mezuaren luzera: {len(mezua)} byte")
    print(f"Gakoaren luzera: {len(gakoa)} byte")

else:

    # Zifratzea
    kriptograma = xor_zifratzea(mezua, gakoa)

    # Deszifratzea
    mezua_berreskuratua = xor_zifratzea(kriptograma, gakoa)

    print("\n=== EMAITZAK ===")

    print("Jatorrizko mezua:")
    print(mezua.decode())

    print("\nGakoa:")
    print(gakoa.decode())

    print("\nMezua HEX:")
    print(mezua.hex())

    print("\nGakoa HEX:")
    print(gakoa.hex())

    print("\nKriptograma HEX:")
    print(kriptograma.hex())

    print("\nDeszifratutako mezua:")
    print(mezua_berreskuratua.decode())

    # Egiaztapena
    if mezua_berreskuratua == mezua:
        print("\n✓ Deszifratzea zuzena da.")
    else:
        print("\n✗ Deszifratzea EZ da zuzena.")


