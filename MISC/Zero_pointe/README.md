**Introduction**

L’objectif de challenge est de trouver un moyen de lire le contenu du fichier « flag.txt » en exploitant les limites des long en C.

**Résolution**

On nous fourni un programme écrit en C dont l’objectif est d’afficher le contenu du fichier « flag.txt ». Cependant, la fonction flag qui lit et affiche le contenu de « flag.txt » n’est appelée que lorsqu’un signal SIGFPE est capturé. Le signal SIGFPE est généralement envoyé lorsqu’une erreur arithmétique se produit, comme une division par zéro.

Le programme lit deux nombres a et b et effectue une division (a / b). Si b est zéro, la division n’est pas effectuée et le signal SIGFPE n’est pas généré. Pour déclencher le signal et appeler la fonction flag, on doit provoquer une division par zéro.

Une façon de le faire est de fournir des valeurs spécifiques pour a et b qui provoqueront une division par zéro malgré la vérification (c = b ? a / b : 0;). On peut donc exploiter un comportement indéfini en C en utilisant des nombres très grands pour provoquer un dépassement de capacité lors de la division.

Pour rappel, en C, la valeur max d’un long est ***9223372036854775807***. On envoie donc au serveur les inputs suivants:

* a = 9223372036854775807
* b = 1

Après une division de a par b, le résultat est égal à la valeur maximum d’un long ce qui crée une erreur SIGFPE et nous renvoie le flag.

**FCSC{0366ff5c59934da7301c0fc6cf7d617c99ad6f758831b1dc70378e59d1e060bf}**
