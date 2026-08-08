# Portfolio — Amine El Mahlali

Cinq pages HTML autonomes, bilingues FR/EN, prêtes à héberger.

## Contenu

```
index.html                    accueil : hero, expertise, 4 cartes projet, parcours, contact
projet-atlasbox.html          page dédiée Atlas BOX
projet-fluviatlas.html        page dédiée FluviAtlas
projet-piezoatlas.html        page dédiée PiezoAtlas
projet-trekxi.html            page dédiée Trekxi
assets/
  CV_Amine_EL_MAHLALI.pdf     seul fichier externe, servi par le lien de téléchargement
  qr.png                      QR code source (également embarqué dans index.html)
  logos/  img/  video/        images sources
make_qr.py                    regénération du QR code
_src/                         sources de génération (voir plus bas)
```

**Chaque page HTML embarque ses propres images en base64.** Aucune image ne peut donc
casser, même si la page est ouverte seule, envoyée par mail ou déplacée. Le seul fichier
externe est le PDF du CV.

## Tester en local

Double-cliquer sur `index.html`. Tout s'affiche, y compris les logos et les schémas animés.
Seules les polices Google Fonts nécessitent une connexion ; sans réseau la page reste lisible.

## Mettre en ligne sur GitHub Pages

1. Créer un dépôt **public** nommé `portfolio`.
2. Téléverser les cinq fichiers `.html`, le dossier `assets/` et `make_qr.py` à la racine.
   Le dossier `_src/` peut être téléversé ou non, il ne sert qu'à la régénération.
3. **Settings → Pages** → *Deploy from a branch* → branche `main`, dossier `/ (root)`.
4. Après une à deux minutes : `https://<identifiant>.github.io/portfolio/`

## Regénérer le QR code

Le QR livré pointe vers une adresse provisoire. Une fois l'URL réelle connue :

```bash
pip install qrcode pillow
python make_qr.py "https://<identifiant>.github.io/portfolio/"
cd _src && python build.py     # réintègre le nouveau QR dans index.html
```

## Ajouter des captures et des vidéos

Chaque page projet contient un bloc « emplacement disponible » qui marque l'endroit prévu.

**Méthode simple** — éditer directement le HTML. Placer le fichier dans `assets/img/`
et remplacer le bloc `<div class="slot">…</div>` par :

```html
<figure class="fig rv">
  <img src="assets/img/mon-fichier.png" alt="Description" loading="lazy">
  <figcaption>Légende courte et factuelle</figcaption>
</figure>
```

Attention : une image référencée ainsi n'est plus embarquée, elle doit donc rester à côté
du HTML. Pour la ré-embarquer, passer par la méthode ci-dessous.

**Méthode propre** — modifier `_src/build.py`, puis regénérer :

```bash
pip install pillow
cd _src && python build.py
```

Pour une vidéo, format MP4, moins de 20 secondes, sans son :

```html
<figure class="fig rv">
  <video src="assets/video/mon-fichier.mp4" autoplay muted loop playsinline></video>
  <figcaption>Légende</figcaption>
</figure>
```

## Les deux éléments interactifs

**Accueil — colonne stratigraphique.** Chaque strate est un lien : survol = soulèvement,
clic = navigation vers la section. La dernière tuile télécharge le CV. Le code vit dans
`_src/figures2.py`, constante `NAV_LOG` ; les couleurs et libellés sont les arguments de
`_slab(...)`.

**FluviAtlas — bloc de bassin versant.** Cinq couches activables : relief, précipitations
et ruissellement, limite du bassin, réseau hydrographique, exutoire. Chaque bouton bascule
une classe `off-<couche>` sur le conteneur, ce qui estompe le groupe SVG correspondant.
Constante `FA_BLOCK` dans `_src/figures2.py`, styles et script dans la variable `extra_fa`
de `build.py`. Pour ajouter une couche : un groupe `<g class="l-macouche">` dans le SVG,
un bouton `data-layer="macouche"`, et la règle `#wsb.off-macouche .l-macouche` dans le CSS.

## Modifier les textes

Le français est écrit dans `_src/build.py`, l'anglais dans le dictionnaire `en` de chaque
fonction `build_*`, indexé par les mêmes clés `data-i18n`. **Le script refuse de générer
une page dont une clé française n'a pas de traduction anglaise** — l'incohérence entre les
deux versions est donc impossible.

Les schémas animés vivent dans `_src/figures.py`, un `<svg>` par constante.

## Note de sécurité

Ne téléverser dans le dépôt public que le contenu de ce dossier. Les fichiers `CLAUDE.md`,
`primer.md`, `lessons.md` et `next-session-prompt.md` de tes projets d'origine contiennent
des empreintes de keystore, des adresses administrateur, des politiques d'accès base de
données et des chemins de clés privées. Ils n'ont rien à faire en ligne.
