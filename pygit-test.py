from pygit2 import Repository, GIT_SORT_TOPOLOGICAL

repo = Repository("../emma-experimental-repo")
obj = repo.get("f63e33b27081f84d10c2835b4b75d8f7643d7c81")

for commit in repo.walk(repo.head.target):
   print(commit.hex)

tree = repo.revparse_single('main').tree
print([e.name for e in tree])

# print(repo.walk(repo.head.target))

# for i in repo.config.__iter__():
#    print(i.name)