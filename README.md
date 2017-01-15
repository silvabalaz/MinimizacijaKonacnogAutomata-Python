# MinimizacijaKonacnogAutomata-Python
Hopcroft algoritam

Kolegij: Interpretacija programa

Za bilo koji DKA moguće je izgraditi beskonačno mnogo drugih DKA koji prihvaćaju isti jezik. Učinkovito programsko ostvarenje zahtjeva gradnju DKA sa što manjim brojem stanja:

_Za regularni jezik L moguće je izgraditi DKA M koji ima manji ili jednak broj stanja od bilo kojeg drugog DKA M' koji prihvaća isti taj jezik L._

<br />
_P := {F, Q \ F};<br />
W := {F};<br />
**while** (W is not empty) do<br />
            choose and remove a set A from W <br />
     **for** each c in Σ do <br />
             let X be the set of states for which a transition on c leads to a state in A <br />
          **for** each set Y in P for which X ∩ Y is nonempty and Y \ X is nonempty **do** <br />
                         replace Y in P by the two sets X ∩ Y and Y \ X <br />
               **if** Y is in W <br />
                         replace Y in W by the same two sets <br />
               **else**
                    if |X ∩ Y| <= |Y \ X| <br />
                         add X ∩ Y to W <br />
                    **else**
                         add Y \ X to W <br />
          **end**;<br />
     **end**;<br />
**end**;_<br />

