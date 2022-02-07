# Filmography matching

Creator matching between filmographic datasets.

## Method

This work is based on a suggestion made by Georg Eckes (Bundesarchiv, Berlin) in 2019 during a discussion around practical linked open data strategies for film archives, and possible linking methodologies.

The process involves working through creators from a first dataset, identifying a list of attached film titles, generating a list of possible matching creators from the second dataset based on name similarity, with a corresponding list of film titles for each. For every film title from the original creator, best match scores are collected from each candidate's filmography, with a median score of 100 being judged a successful match.  

Note that the term "creator" is used generally for anyone involved in the creation of a film.

## Examples

The test datasets provided are from the [ACMI Collection API](https://github.com/acmilabs/acmi-api) and [Wikidata](https://www.wikidata.org/), using the filmographies for ten creators from each. There is intentionally some overlap to demonstrate successful matching, some unmatched individuals, and also some matches which are not successful, selected for illustrative purposes.

~

ACMI list five films for Agnès Varda (34373):
```
VAGABOND (92856)
THE GLEANERS AND I (94941)
CLEO FROM 5 TO 7 (92708)
LES CREATURES (115910)
JACQUOT DE NANTES [WIDESCREEN] (92706)
```
There are many Wikidata creators with a "similar" name (judged as a Levenshtein score of 70 or over). Two have been selected to test matching: 

##### Agnès Godard (Q395096) has 30 film credits on Wikidata, printed below with both english label and title (where they are available and/or different).
```
35 RHUMS (Q2816310), 35 SHOTS OF RUM (Q2816310), AU PLUS PRES DU PARADIS (Q1185105), BACKSTAGE (Q2878435), 
BASTARDS (Q3235299), BEAU TRAVAIL (Q1193562), CHAMBRE 666 (Q2288599), ENSEMBLE,C'EST TOUT (Q230616), HOME (Q666600), 
HUNTING AND GATHERING (Q230616), I CAN'T SLEEP (Q3156595), J'AI PAS SOMMEIL (Q3156595), 
KACEY MOTTET KLEIN, NAISSANCE D'UN ACTEUR (Q54956954), L'ABSENCE (Q3201388), L'ENFANT D'EN HAUT (Q870091), 
L'INTRUS (Q3204273), LA LIGNE (Q110620537), LA REPETITION (Q112633), LA RITOURNELLE (Q17297839), 
LA VIE REVEE DES ANGES (Q1708290), LEAVING (Q1210944), LES EGARES (Q2605684), LES SALAUDS (Q3235299), 
LET THE SUNSHINE IN (Q28495869), LIGHTS OUT (Q2471731), LOS INSOLITOS PECES GATO (Q16827802), 
NEAREST TO HEAVEN (Q1185105), NENETTE ET BONI (Q3347054), NUOVOMONDO (Q113549), OU VA LA NUIT (Q967170), 
PARIS FOLLIES (Q17297839), REPLAY (Q112633), ROOM 666 (Q2288599), SIMON WERNER A DISPARU... (Q2471731), SISTER (Q870091), 
STRAYED (Q2605684), THE ABSENCE (Q3201388), THE AMAZING CATFISH (Q16827802), THE DREAMLIFE OF ANGELS (Q1708290), 
THE FALLING (Q18389665), THE INTRUDER (Q3204273), THE LINE (Q110620537), TRESOR (Q1199219), TROUBLE EVERY DAY (Q63991)
```
These are the scores when matched with the five films from the ACMI dataset:
```
VAGABOND ('NUOVOMONDO', 44)
THE GLEANERS AND I ('THE DREAMLIFE OF ANGELS', 54)
CLEO FROM 5 TO 7 ('35 SHOTS OF RUM', 45)
LES CREATURES ('LES EGARES', 78)
JACQUOT DE NANTES [WIDESCREEN] ('LA VIE REVEE DES ANGES', 44)
```
The final score is the median of those results:
```
median([44, 54, 45, 78, 44]) = 45
```
##### Agnès Varda (Q229990) has 31 film credits on Wikidata, printed below with both english label and title (where they are available and/or different).
```
7P., CUIS., S. DE B., ... A SAISIR (Q2818437), 7P., CUIS., S. DE B., ...A SAISIR (Q2818437), AGNES VARDA (Q105634920), 
AMERICANO (Q497308), BLACK PANTHERS (Q2905436), CLEO DE 5 A 7 (Q1199628), CLEO FROM 5 TO 7 (Q1199628), 
DOCUMENTEUR (Q3033632), FACES PLACES (Q29406094), FAR FROM VIETNAM (Q3258662), HAPPINESS (Q1168501), 
JACQUOT DE NANTES (Q3160388), JANE B. PAR AGNES V. (Q3161846), KUNG FU MASTER (Q1217734), KUNG-FU MASTER (Q1217734), 
L'UNE CHANTE, L'AUTRE PAS (Q3205011), L'UNIVERS DE JACQUES DEMY (Q3204825), LA POINTE COURTE (Q1503132), 
LAST TANGO IN PARIS (Q570567), LE BONHEUR (Q1168501), LES CENT ET UNE NUITS DE SIMON CINEMA (Q1547511), 
LES CREATURES (Q3231865), LES DEMOISELLES ONT EU 25 ANS (Q3236309), LES DITES CARIATIDES (Q3232133), 
LES FIANCES DU PONT MAC DONALD OU MEFIEZ-VOUS DES LUNETTES NOIRES (Q3232596), LES GLANEURS ET LA GLANEUSE (Q2493884), 
LES PLAGES D'AGNES (Q2709504), LIONS LOVE (Q3241992), LOIN DU VIETNAM (Q3258662), MUR MURS (Q3328223), 
MURAL MURALS (Q3328223), ONE HUNDRED AND ONE NIGHTS (Q1547511), ONE SINGS, THE OTHER DOESN'T (Q3205011), 
QUELQUES VEUVES DE NOIRMOUTIER (Q3414147), SANS TOIT NI LOI (Q2298257), THE BEACHES OF AGNES (Q2709504), 
THE FIANCES OF THE BRIDGE MAC DONALD (Q3232596), THE GLEANERS AND I (Q2493884), THE SO-CALLED CARYATIDS (Q3232133), 
THE TRUTH ABOUT CHARLIE (Q570780), THE WORLD OF JACQUES DEMY (Q3204825), THE YOUNG GIRLS TURN 25 (Q3236309), 
ULTIMO TANGO A PARIGI (Q570567), VAGABOND (Q2298257), VARDA BY AGNES (Q63993096), VARDA PAR AGNES (Q63993096), 
VISAGES, VILLAGES (Q29406094), WOMEN MAKE FILM (Q77855044), WOMEN MAKE FILM: A NEW ROAD MOVIE THROUGH CINEMA (Q77855044)
```
These are the scores when matched with the five films from the ACMI dataset:
```
VAGABOND ('VAGABOND', 100)
THE GLEANERS AND I ('THE GLEANERS AND I', 100)
CLEO FROM 5 TO 7 ('CLEO FROM 5 TO 7', 100)
LES CREATURES ('LES CREATURES', 100)
JACQUOT DE NANTES [WIDESCREEN] ('JACQUOT DE NANTES', 76)
```
The final score is the median of those results:
```
median([100, 100, 100, 100, 76]) = 100
```
This results in a successful match of Agnès Varda (ACMI 34373) and Agnès Varda (Wikidata Q229990).

~

ACMI list four films for Cate Shortland (ACMI 6829):
```
JOY (108403), PARA PARA PARADISE (109217), PENTUPHOUSE (90526), FLOWERGIRL (90523)
```
There are many Wikidata creators with a "similar" name (judged as a Levenshtein score of 70 or over). 
One has been selected to test matching:
##### Cate Shortland (Q441510) has 4 film credits on Wikidata, printed below with both english label and title (where they are available and/or different).
```
SOMERSAULT (Q1513503), LORE (Q421583), BLACK WIDOW (Q23894626), BERLIN SYNDROME (Q25212771)
```
These are the scores when matched with the four films from the ACMI dataset:
```
JOY ('LORE', 29)
PENTUPHOUSE ('BERLIN SYNDROME', 31)
FLOWERGIRL ('LORE', 43)
PARA PARA PARADISE ('BERLIN SYNDROME', 24)
```
The final score is the median of those results:
```
median([29, 31, 43, 24]) = 30
```
This results in an unsuccessful match due to ACMI containing only pre-feature shorts, and Wikidata only feature films, so there is no filmographic crossover.

## Further matching

Once creators have been matched, film title overlap could be identified with a general level of confidence, as it is rare that individual creators would have similarly named films (some notable exceptions, Abel Gance's two versions of "J'accuse" (1919 and 1938), Alfred Hitchcock's two versions of "The Man Who Knew Too Much" (1934 and 1956), Michael Haneke's two versions of "Funny Games" (1997 and 2007)). Also similarly named sequels would likely require manual intervention (eg Rocky II and Rocky III). Once films have been paired, a third pass could identify additional creator matches, as the chance of similarly named creators working on the same specific film should be tolerably low. In all of these processes, results may be accepted only if there is a single successful candidate.

## Known issues

- Matching depends on the initial dataset being less well populated than the second, as it loops through matches for each title in the first set. An example would be that if the first dataset contains twenty films for a creator and the second five, the best possible score is 25%[^1]. Wikidata has been used as the second matching dataset for most tests so far, as it is quite large and constantly growing. Another strategy would be to swap datasets, run A -> B and then B -> A, collecting matches from both.

- There is a statisically higher chance of being falsely matched with an individual with many credits, rather than someone with few. Consider that an individual with a single credit for a generically titled film and a name similar to someone with an unusually extensive filmography (eg [Natalie Kalmus](https://en.wikipedia.org/wiki/Natalie_Kalmus)) stands some chance of being falsely matched with her, if that individual is not present in the second dataset.

- There is a reasonable chance of confusion between organisations and indviduals with similar names and filmographies, eg Walt Disney and Walt Disney Studios.

[^1]: In this process the median number is used to score, so the actual resulting score would be 0.
