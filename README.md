#Git
[Download](https://git-scm.com/downloads)

##Setup

```bash
# Crear un repositorio local en el directorio actual
git init  

# Vincular el repositorio local con uno de remoto (Github, Gitlab, Atlassian...)
git remote add origin [repoURL]     
```
ó
```bash
# Clonar un repositorio a este directorio (clone crea un directorio)
git clone
```

## Branches

```bash
# Crear una nueva branch llamda [newBranchName] a partir del estado de la branch actual 
git checkout -b [newBranchName]

# Listado de todas las branch (locales y remotas)
git branch -a

# Cambiar a la branch [branchName] (debió ser previamente creada)
git checkout [branchName]

# Trae los cambios de la branch [branchToMerge] a la branch actual, es decir, la branch actual va a tener los cambios de [branchToMerge]
git merge [branchToMerge]
```

## Conocer el status actual del repositorio local
```bash
git status
```

## Prepare a commit
```bash
# Indicar cuales son los archivos a incluir en el commit
git add [path/fileName]

# Incluir todos los archivos modificados para este commit
git add --all

# Agregar una descripción general al commit
git commit -m'[Commit description]'
```

## Pull/push
```bash
# Obtener los cambios remotos a mi [branchName] local
git pull origin [branchName]

# Compartir mis cambios locales en la branch [branchName] al repositorio remoto
git push origin [branchName]
```


