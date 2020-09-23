### Lab on Version Control

This repository is an implementation of very simple storage based on Python dictionary.

The storage supports four operations:
* **add**: adds `<key,value>` into storage,
* **get**: returns a `value` for a given `key` or `None` if no such `key`,
* **remove**: removes `<key,value>` pair based on `key`,
* **set**: sets a new `value` for a given `key` if the `key` is present

**get** is already implemented

Your task is to finish this implementation collaboratively using `git`. Also it is needed to provide a unittest for each method implemented in `Storage` class.

### What we expect

1. You are divided into several teams. One member of each team should `fork` this repository. Add your teammates as `contributors`
1. Team members decide on which functionality they will implement (i.e. method under `storage.py` and a corresponding test under `tests.py`)
1. After that, members clone forked repository, create a `branch` with a name `feature/add` (or `remove`, or `set`), implement this functionality under that branch
1. When the functionality is implemented and tested locally push it to the `remote` and open `pull request` to the `master` branch
1. Other teammates not involved in realization of this very feature are asked to review `pull request` and give a positive feedback under the comments if it's OK. After that, owner of `master` branch merges all these features into `master`

As a result there should be completed functionality that evidently built in parallel.

### QA

**Q**: If I am the owner of the `master` branch should I create `feature` branch or it is possible for me to push it directly to the `master`

**A**: Ownership of the `master` branch doesn't provide you rights to push there directly if you're working on a project with a team. Each feature should be accepted with other members of the project. There's also an option in GitHub repo settings that won't give a possibility to push in `origin/master` directly



