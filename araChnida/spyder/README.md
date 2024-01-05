# Web-crawler

Le but est du projet est de faire un scraper qui va dowloader toutes les images avec un certain degré de récursions.
Afin d'éviter les chemins faciles, nous allons faire ce programme en C.  

Une solution de choix (afin de gagner du temps) est d'utiliser la `libcurl`.  

## libcurl
Libcurl est une librairie "client-side URL de transfert", elle supporte de nombreux protocoles web et elle est écrite en C.  
Il est inutile de dire qu'elle est liée à `curl`...  

Voici quelques sources pour apprendre a s'en servir :  
- [La doc officielle](https://curl.se/libcurl/): Normalement toutes est dessus.
- [ ] [Mise en place rapide grace à Jacob Sorber](https://www.youtube.com/watch?v=daA-KBKfJ_o)
- [ ] [How to Get started with libcURL de wolfSSL](https://www.youtube.com/watch?v=g83kYIQNRwU) 


## Gestion d'arguments

Il y a plusieurs librairies standard en C pour gérer les arguments en CLI:
- Getopt. Dans `unistd.h` de la POSIX C Lib.
- Argp . Cette dernière semble être base sur Getopt et avec quelques optimisation.
