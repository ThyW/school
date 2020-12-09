# About
Zbierka private poznamok, uloh a hovadin za skolsky rok 2020-21

# Building pdfs
Poznamky su vo formate **Rmarkdown**:

Subor .rmd vyzere nejako takto:
```rmd
---
title: ...
author: ...
output: ...
---

# Sample heading
- stuff
- more stuff
```

Na kovertovanie vieme pouzit online konvertor, napriklad `https://cloudconvert.com/md-to-pdf`

Subor .rmd si treba stiahnut, zmenit mu meno z `menosuboru.rmd` na `menosuboru.md` a dat z neho prec cast:
```rmd
---
title: ...
author: ...
output: ...
---
```
tak, aby nam ostalo len:

```md
# Sample heading
- stuff 
- morestuff
```

Toto potom vieme dat do online converteru a mal by nam vediet urobit pdf.

***Pozor, poznamky z fyziky ktore obsahuju LaTeX syntax, sa vam mozno neprekonvertuju, preto to treba upravit tak, aby tam ziadny LaTeX nebol***
