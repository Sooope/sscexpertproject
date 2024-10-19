Get started by creating a new file or uploading an existing file. We recommend every repository include a `README`, `LICENSE`, and `.gitignore`.

…or create a new repository on the command line
```
echo "# myrepo" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/loretoparisi/myrepo.git
git push -u origin master
``` 

…or push an existing repository from the command line
```
git remote add origin https://github.com/loretoparisi/myrepo.git
git pull origin master --allow-unrelated-histories
git commit -a -m "merge"
git push -u origin master
```

…or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.