---
title: How to push changes from local git repo to GitHub with Finegrained Personal Access Token (PAT)
tags: [git, github]
---

# How to push changes from local git repo to GitHub with Finegrained Personal Access Token (PAT)

Make sure your .env file is loaded in the shell:

```bash
export $(grep -v '^#' .env | xargs)
```

This sets GH_TOKEN as an environment variable.

Configure Git to use the token for HTTPS:

```bash
git remote set-url origin https://github.com/<username>/<repo-name>.git
```

Push using the token without embedding it in the URL:

```bash
git -c http.extraheader="AUTHORIZATION: bearer $GH_TOKEN" push origin main
```

`-c http.extraheader="AUTHORIZATION: bearer $GH_TOKEN"` tells Git to use the token for authentication just for this command. This way your token is never saved in Git config or remote URLs.
