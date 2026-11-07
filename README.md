# Forensique Numérique (FORN)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](FORN_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE LPI342** · Université de Garoua · Faculté des Sciences · Département de Mathématiques et Informatiques · Master Professionnel en Sécurité des Systèmes Informatiques et des Données · 30 heures
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel · contact : maletyon@proton.me · année académique 2026-2027

> *Tout contact laisse une trace ; encore faut-il savoir la recueillir sans l'altérer, et la rendre opposable.*

Ce cours enseigne l'investigation numérique de bout en bout : de la saisie d'un support à la preuve présentée devant un juge. Il couvre les fondements (principe de Locard, démarche d'enquête, éthique et impartialité de l'expert), le cadre juridique et la recevabilité (droit de la preuve, chaîne de possession, principes ACPO), l'acquisition sans altération (identification et préservation, duplication et hachage SHA-256, ordre de volatilité et acquisition à chaud), l'analyse par domaine (disque et systèmes de fichiers, fichiers supprimés et artefacts, mémoire, réseau, mobile, nuage), les défis de l'enquête (anti-forensique et chiffrement, reconstitution chronologique) et la restitution (rapport forensique, présentation au tribunal, mesure). Un fil théorique parcourt le cours : le Trilemme CRO (Confidentialité, Fiabilité, Opposabilité). L'ensemble s'appuie sur ISO/IEC 27037, 27042 et 27043, NIST SP 800-86 et 800-101, la RFC 3227, les principes ACPO, les lois camerounaises 2010/012 et 2024/017, et les Conventions de Malabo et de Budapest. Le fil rouge est l'Opération TSANAGA : une investigation judiciaire confiée au cabinet NYONG SÉCURITÉ, où un ancien employé est soupçonné d'avoir revendu un fichier client. Les noms, dates et montants sont fictifs ; les normes et les textes de loi sont cités d'après leur version officielle.

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`FORN_main.pdf`](FORN_main.pdf) | Traité complet (prologue, six parties, 20 chapitres, annexes) |
| Les présentations | [`Présentation/`](Présentation/) | 16 présentations : vision d'ensemble et 15 séances de 2 heures |
| Les fiches d'exercices | [`fiches/`](fiches/) | 21 fiches de 40 questions, une par chapitre (prologue compris) |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie6/`, `annexes/`, `bibliographie/`, [`Style_FORN.sty`](Style_FORN.sty) | Sources du livre |

## Organisation du cours (30 heures, 15 séances de 2 heures)

| Partie | Chapitres | Fichiers |
|---|---|---|
| **Prologue** | La scène numérique | [`partie0/`](partie0/) |
| **I. Fondements du forensique** | 1. Qu'est-ce que la forensique numérique · 2. La démarche d'enquête · 3. Éthique, neutralité, impartialité | [`partie1/`](partie1/) |
| **II. Le cadre juridique et la recevabilité** | 4. Le droit de la preuve numérique · 5. La chaîne de possession · 6. Recevabilité et admissibilité | [`partie2/`](partie2/) |
| **III. L'acquisition des preuves** | 7. Identifier et préserver les sources · 8. Duplication et hachage · 9. Ordre de volatilité et acquisition à chaud | [`partie3/`](partie3/) |
| **IV. L'analyse par domaine** | 10. Forensique disque et systèmes de fichiers · 11. Fichiers supprimés, fragments et artefacts · 12. Forensique mémoire · 13. Forensique réseau · 14. Forensique mobile · 15. Forensique du nuage et des applications | [`partie4/`](partie4/) |
| **V. Les défis de l'enquête** | 16. L'anti-forensique et le chiffrement · 17. Corrélation et reconstitution chronologique | [`partie5/`](partie5/) |
| **VI. Restituer l'enquête** | 18. Le rapport forensique · 19. La présentation devant un tribunal · 20. Mesurer et progresser | [`partie6/`](partie6/) |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles · D. Textes · E. Bibliographie commentée · F. Contacts | [`annexes/`](annexes/) |

Chaque chapitre compte dix exercices gradués ; leurs corrigés, et ceux des fiches, sont dans le livret de correction. Les fiches et les labs se font hors des 30 heures.

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement compagnon du cours : une fiche d'auto-évaluation de 40 questions par chapitre, corrigée automatiquement, des labs sur pièces et un tableau de bord de progression. Le code de cours est **LPI342**.

> **NDAP SUKULU en local.** La version téléchargeable et installable sur votre poste, avec un module autonome pour ce cours, est en cours de finalisation. En attendant, les fiches d'auto-évaluation de chaque chapitre (40 questions) sont fournies au format texte dans [`fiches/`](fiches/).

| Lab | Chapitre | Sujet |
|---|---|---|
| FORN-LAB-01 | 5 | Chaîne de possession et scellés |
| FORN-LAB-02 | 8 | Duplication et hachage |
| FORN-LAB-03 | 10 | Forensique disque : système de fichiers |
| FORN-LAB-04 | 11 | Fichiers supprimés et signatures |
| FORN-LAB-05 | 12 | Analyse d'une capture mémoire |
| FORN-LAB-06 | 13 | Forensique réseau : exfiltration |
| FORN-LAB-07 | 14 | Forensique mobile |
| FORN-LAB-08 | 6 | Recevabilité d'une preuve |
| FORN-LAB-09 | 17 | Reconstitution chronologique |
| FORN-LAB-10 | 18 | Rapport forensique |

Tous les labs se pratiquent sur pièces (journaux, images, condensats, extractions) en environnement fermé.

## Compiler le livre

Avec une distribution LaTeX : `pdflatex FORN_main`, `biber FORN_main`, `makeindex FORN_main`, puis deux fois `pdflatex FORN_main`.
Les présentations se régénèrent avec `python Présentation/_sources/gen_specs.py` puis `python Présentation/_sources/run.py FORN all` (Python 3 et python-pptx).

## Les trois cours de l'Université de Garoua

Ce cours fait partie d'un corpus de trois UE du Master SSID : Supervision, Analyse Forensique et Gestion des Incidents ([SIS589](https://github.com/maletyon/cours-safi)), Forensique Numérique (LPI342), Systèmes de Gestion de la Sécurité Informatique ([IS498](https://github.com/maletyon/cours-sgsi)).
