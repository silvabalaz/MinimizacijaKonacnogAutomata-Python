
class PartiticijaError(object): pass

class ProfinjavanjeParticije:


    def __init__(klasa,elementi):

        S = set(elementi)
        klasa._indeksiSkupova = {id(S):S}
        klasa._particija = {x:S for x in S}

    def __getitem__(klasa,element):

        return klasa._particija[element]

    def __len__(klasa):

        return len(klasa._indeksiSkupova)

    def __iter__(klasa):
          return iter(klasa._indeksiSkupova.values())

    def dodaj(klasa,element,skup):

        if id(skup) not in klasa._indeksiSkupova:
            raise PartiticijaError("Skup ne pripada particiji")
        if element in klasa._particija:
            raise PartiticijaError("Element već pripada particiji")
        skup.add(element)
        klasa._particija[element] = skup

    def ukloni(klasa,element):

        klasa._particija[element].remove(element)
        del klasa._particija[element]