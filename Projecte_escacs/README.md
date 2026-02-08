Aquest projecte consisteix en un simulador d'escacs funcional en mode consola, desenvolupat seguint els principis de Clean Code, Modularitat i Proves Automatitzades. El projecte s'ha estructurat per complir amb els resultats d'aprenentatge del mòdul MP0487.

- Com executar el joc:
Per iniciar una partida, assegura't de tenir instal·lat Python 3. Des de l'arrel del projecte, executa el fitxer principal:

Bash
python src/main.py

- Com executar els tests:
Les proves unitàries s'han desenvolupat amb el framework pytest. Per verificar la lògica de moviments del Peó i el Cavall, executa la següent comanda:

Bash
pytest tests/test_escacs.py

- Estructura de carpetes:
El projecte s'ha dividit en mòduls segons la seva responsabilitat per garantir un codi sostenible i fàcil de mantenir:

/src: Conté el codi font del projecte.

main.py: Punt d'entrada, gestió de la UI de consola i bucle principal.

board.py: Lògica de gestió del tauler (creació, renderitzat i estat de les caselles).

pieces.py: Definició i regles de moviment de cada peça (Peó, Cavall, etc.).

validator.py: Validador centralitzat de moviments i gestió de regles del joc.

/tests: Conté el pla de proves automatitzades amb Pytest.

/docs: Documentació tècnica, incloent el diagrama UML de comportament.

README.md: Instruccions i documentació general del projecte.

- Decisions de disseny importants
Representació del Tauler: S'ha utilitzat una matriu com a taulell de 8x8. Cada casella conté un codi de text (ex: "PB" per Peó Blanc) per facilitar la visualització i la lògica de comparació.

- Gestió d'Errors: S'han implementat missatges d'error específics (no genèrics) que expliquen a l'usuari exactament per què un moviment no és vàlid (ex: "No pots capturar una peça pròpia" o "El peó no pot moure's enrere").

- Historial i Resum: El sistema emmagatzema una llista de moviments en cada partida per oferir un resum detallat en finalitzar, complint amb el requisit de seguiment del joc.

- Partides infinites: El sistema incorpora la opció d'un cop acabada la partida tornar a jugar una altra amb mateixos noms o uns de diferents

- Diagrama de Comportament
S'ha inclòs un diagrama de seqüència UML que detalla el flux de treball quan un jugador intenta realitzar un moviment il·legal. Aquest diagrama es pot trobar a: docs/diagrama_moviment_illegal.png