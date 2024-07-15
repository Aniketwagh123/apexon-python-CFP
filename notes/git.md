# Git Cheat Sheet and Theory

## Introduction to Git

Git is a distributed version control system that allows multiple people to work on a project simultaneously without interfering with each other's changes. It tracks changes to files and coordinates work on those files among multiple people.

## Key Concepts

- **Repository (repo):** A directory which contains your project work, along with all the files Git uses to track your revisions.
- **Commit:** A snapshot of your repository at a specific point in time.
- **Branch:** A movable pointer to a commit. The default branch name in Git is `main`.
- **Merge:** The action of integrating changes from different branches.
- **Rebase:** Reapply commits on top of another base tip.
- **Clone:** A copy of a repository.
- **Pull:** Fetch and merge changes from a remote repository to your local repository.
- **Push:** Send your committed changes to a remote repository.

## Git Commands and Their Uses

| Command                           | Flag/Option             | Description                                               |
|-----------------------------------|-------------------------|-----------------------------------------------------------|
| `git init`                        |                         | Initialize a new Git repository.                          |
| `git clone <repo>`                |                         | Clone a repository into a new directory.                  |
| `git status`                      |                         | Show the working tree status.                             |
| `git add <file>`                  |                         | Add file contents to the index (staging area).            |
| `git commit -m "<message>"`       |                         | Record changes to the repository with a message.          |
| `git log`                         |                         | Show commit logs.                                         |
| `git branch`                      |                         | List, create, or delete branches.                         |
| `git checkout <branch>`           |                         | Switch to another branch.                                 |
| `git merge <branch>`              |                         | Merge a branch into the current branch.                   |
| `git pull`                        |                         | Fetch and integrate changes from the remote repository.   |
| `git push`                        |                         | Update the remote repository with local commits.          |
| `git remote -v`                   |                         | Show the remote connections.                              |
| `git fetch`                       |                         | Download objects and refs from another repository.        |
| `git reset --hard <commit>`       |                         | Reset the index and working tree to a specific commit.    |
| `git rm <file>`                   |                         | Remove files from the working tree and from the index.    |
| `git stash`                       |                         | Stash the changes in a dirty working directory away.      |
| `git stash apply`                 |                         | Apply the stashed changes to the working directory.       |
| `git tag <tagname>`               |                         | Create a tag for a specific commit.                       |
| `git diff`                        |                         | Show changes between commits, commit and working tree, etc.|
| `git rebase <branch>`             |                         | Reapply commits on top of another base tip.               |
| `git cherry-pick <commit>`        |                         | Apply the changes introduced by some existing commits.    |
| `git bisect`                      |                         | Use binary search to find the commit that introduced a bug.|

### Commonly Used Git Flags

| Command                | Flag/Option | Description                                 |
|------------------------|-------------|---------------------------------------------|
| `git commit`           | `-a`        | Automatically stage files that have been modified and deleted, but new files are not staged. |
| `git commit`           | `--amend`   | Modify the most recent commit.              |
| `git push`             | `-u`        | Set upstream for the branch.                |
| `git log`              | `--oneline` | Show commits in a compact format.           |
| `git log`              | `--graph`   | Show a graph of the commit history.         |
| `git diff`             | `--staged`  | Show changes between the index and the last commit. |
| `git branch`           | `-d`        | Delete a branch.                            |
| `git remote`           | `add`       | Add a new remote repository.                |
| `git rebase`           | `--interactive` | Rebase interactively, allowing to edit, reorder, and squash commits. |

## Git Commit Message Conventions

Clear commit messages help in understanding the history of a project. Here are some conventional types of commit messages that indicate the nature of the changes made to the code:

- **Feat:** Adds a new feature to an application or library.
- **Fix:** Resolves a bug.
- **Refactor:** Changes code without adding a feature or fixing a bug.
- **Style:** Changes that don't affect the code's meaning, such as formatting or white space.
- **Docs:** Updates documentation, such as a README or other markdown files.
- **Test:** Adds or corrects tests.
- **Perf:** Enhances code performance.
- **Build:** Changes related to the build system or dependencies.
- **CI:** Changes to CI configuration files and scripts.
- **Chore:** Other changes that don't modify source or test files, such as upgrading libraries or performing maintenance tasks.

## Example Commit Messages

```plaintext
feat: add user authentication module
fix: resolve null pointer exception in UserService
refactor: simplify logic in PaymentProcessor
style: reformat code to comply with PEP 8
docs: update installation guide in README
test: add unit tests for the OrderService class
perf: improve query performance by adding indexes
build: update Gradle to version 6.8.3
ci: add CircleCI configuration for continuous integration
chore: upgrade dependencies to latest versions