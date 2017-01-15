# MinimizacijaKonacnogAutomata-Python
Hopcroft algoritam </br>
https://en.wikipedia.org/wiki/DFA_minimization </br>
https://en.wikipedia.org/wiki/Partition_refinement </br>

Kolegij: Interpretacija programa

Za bilo koji DKA moguće je izgraditi beskonačno mnogo drugih DKA koji prihvaćaju isti jezik. Učinkovito programsko ostvarenje zahtjeva gradnju DKA sa što manjim brojem stanja:

_Za regularni jezik L moguće je izgraditi DKA M koji ima manji ili jednak broj stanja od bilo kojeg drugog DKA M' koji prihvaća isti taj jezik L._ </br></br>

Σ - abeceda </br>
_P := {F, Q \ F};<br />
W := {F};<br />
**while** (W is not empty) do<br />
           &nbsp;&nbsp; choose and remove a set A from W <br />
     **for** each c in Σ do <br />
            &nbsp;&nbsp; let X be the set of states for which a transition on c leads to a state in A <br />
          **for** each set Y in P for which X ∩ Y is nonempty and Y \ X is nonempty **do** <br />
                      &nbsp;&nbsp;   replace Y in P by the two sets X ∩ Y and Y \ X <br />
               **if** Y is in W <br />
                      &nbsp;&nbsp;   replace Y in W by the same two sets <br />
               **else**
                  &nbsp;&nbsp;  if |X ∩ Y| <= |Y \ X| </br>
                  &nbsp;&nbsp;&nbsp;&nbsp; add X ∩ Y to W <br />
                    **else**
                    &nbsp;&nbsp;&nbsp;&nbsp; add Y \ X to W <br />
          **end**;<br />
     **end**;<br />
**end**;_<br />

**Intuitivno** </br>
&nbsp;&nbsp;Pogledaj stanja koja se međusobno mogu razlikovati (za isti ulazni znak prelaze u različita stanja) </br>
**Algoritam** </br>
Konstruiraj inicijalnu particiju </br>
&nbsp;&nbsp;(stanja prihvaćanja/neprihvaćanja)</br>
Iterativno profinjuj particiju (sve dok particije ne postanu fiksne) </br>
&nbsp;&nbsp;Podijeli particiju ako članovi u particiji imaju prijelaze u različite particije za isti ulazni string </br> </br>

_Dva stanja x i y pripadaju istoj particiji **ako i samo ako** za sve simbole u Σ prelaze u istu particiju._

**Implementacija** </br>
_**KA.py**_</br>
Konačan automat koji se može zadati preko definicije (_def definicija_) ili kao string koji je potrebno parsirati (_def iz_tablice_) </br>
&nbsp;&nbsp;definicija:</br>
stanja, abeceda, prijelaz, početno, završna </br>
&nbsp;&nbsp;&nbsp;&nbsp; abeceda koja je konačan neprazan skup, početno stanje koje je element skupa stanja, završna stanja koja su &nbsp;&nbsp;&nbsp;&nbsp;podskup skupa stanja</br>

_**ProfinjenjeParticije.py**_


