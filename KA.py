# Kod preuzet sa: https://github.com/vedgar/ip/blob/master/KA.py

import random, itertools, operator, types, pprint


Kartezijev_produkt = lambda *skupovi: set(itertools.product(*skupovi))
funkcija = lambda f, A, B: f.keys() == A and set(f.values()) <= B
petorka = operator.attrgetter(
    'stanja', 'abeceda', 'prijelaz', 'početno', 'završna')


class KonačniAutomat(types.SimpleNamespace):
    @classmethod
    def definicija(klasa, stanja, abeceda, prijelaz, početno, završna):
        assert abeceda and početno in stanja and završna <= stanja
        assert funkcija(prijelaz, Kartezijev_produkt(stanja, abeceda), stanja)
        return klasa(**locals())

    @classmethod
    def iz_tablice(klasa, tablica):
        prva, *ostale = tablica.strip().splitlines()
        znakovi = prva.split()
        assert all(len(znak) == 1 for znak in znakovi)
        abeceda = set(znakovi)
        stanja, završna = set(), set()
        prijelaz, početno = {}, None
        for linija in ostale:
            stanje, *dolazna = linija.split()
            if početno is None: početno = stanje
            extra = len(dolazna) - len(znakovi)
            assert extra in {0, 1}
            if extra == 1:
                assert dolazna.pop() == '#'
                završna.add(stanje)
            for znak, dolazno in zip(znakovi, dolazna):
                prijelaz[stanje, znak] = dolazno
            stanja.add(stanje)
        return klasa.definicija(stanja, abeceda, prijelaz, početno, završna)

    ispiši = lambda automat: pprint.pprint(petorka(automat))

    def prihvaća(automat, ulaz):
        stanje = automat.početno
        for znak in ulaz: stanje = automat.prijelaz[stanje, znak]
        return stanje in automat.završna

    def slučajni_testovi(automat, koliko=None, maxduljina=None):
        znakovi = list(automat.abeceda)
        yield ''
        yield from znakovi
        if maxduljina is None: maxduljina = max(len(automat.stanja), 3)
        if koliko is None: koliko = max(len(znakovi) ** maxduljina, 99)
        for _ in range(koliko):
            duljina = random.randint(2, maxduljina)
            yield ''.join(random.choice(znakovi) for _ in range(duljina))

    def provjeri(automat, specifikacija, koliko=None, maxduljina=None):
        for test in automat.slučajni_testovi(koliko, maxduljina):
            lijevo = automat.prihvaća(test)
            desno = specifikacija(test)
            if lijevo != bool(desno):
                print('!!Kontraprimjer', repr(test), lijevo, desno)
                break
        return specifikacija

    def log(automat, ulazi):
        ulazi = ulazi.split()
        najduljina = max(map(len, ulazi))
        for ulaz in ulazi:
            print(ulaz.ljust(najduljina), automat.prihvaća(ulaz))
        print('END'.rjust(najduljina + 6, '-'))

    def debug(automat, ulaz):
        stanje = automat.početno
        for znak in ulaz:
            print(stanje, znak, end=' ')
            stanje = automat.prijelaz[stanje, znak]
        print(stanje, stanje in automat.završna)


def primjeri1():
    M1 = KonačniAutomat.iz_tablice(
    '''0  1
    q1 q1 q2
    q2 q3 q2 #
    q3 q2 q2   ''')  # page 34 figure 1.4  # page 36 figure 1.6
    M1.log('1 01 11 0101010101 100 0100 110000 0101000000 0 10 101000')

if __name__ == '__main__':
    primjeri1()
