# Fetch all branches
git fetch --all

# Loop through each remote branch and create a corresponding local branch
for branch in $(git branch -r | grep -v '\->'); do
    local_branch=${branch#origin/}
    git checkout -b $local_branch $branch
done
