# MinimizacijaKonacnogAutomata-Python
Hopcroft algoritam

Kolegij: Interpretacija programa

Za bilo koji DKA moguće je izgraditi beskonačno mnogo drugih DKA koji prihvaćaju isti jezik. Učinkovito programsko ostvarenje zahtjeva gradnju DKA sa što manjim brojem stanja:

_Za regularni jezik L moguće je izgraditi DKA M koji ima manji ili jednak broj stanja od bilo kojeg drugog DKA M' koji prihvaća isti taj jezik L._

P := {F, Q \ F};
W := {F};
while (W is not empty) do
     choose and remove a set A from W
     for each c in Σ do
          let X be the set of states for which a transition on c leads to a state in A
          for each set Y in P for which X ∩ Y is nonempty and Y \ X is nonempty do
               replace Y in P by the two sets X ∩ Y and Y \ X
               if Y is in W
                    replace Y in W by the same two sets
               else
                    if |X ∩ Y| <= |Y \ X|
                         add X ∩ Y to W
                    else
                         add Y \ X to W
          end;
     end;
end;

