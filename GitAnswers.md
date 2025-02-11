1. What is the difference between git and GitLab?

Git is a system for version control, while GitLab is a web-based platform that provides repository hosting.

2. What is the difference between GitLab, GitHub, and BitBucket?

GitHub is the most popular Git repository services. GitLab provides more integrated DevOps tools. BitBucket is more specialized and well integrated with Jira, Confluence, Trello, and other Atlassian products.

3. Why would I ever want to use git, but not GitLab?

If I am working along instead of collaborative work, Git is sufficient for local-only version control.

4. What are the steps to update the GitLab server with some changes I made on my computer?

(1) [Check the status] git status
(2) [Add the changed file] git add filename.txt
(3) [Commit the change] git commit -m "(Describe the change made)"
(4) [Push the change to GitLab] git push origin main


5: What is a branch and why would I use one?  

A branch is a separate workspace, where changes can be made outside of the main "project". Then it can be merged into the main project or main branch afterwards.
It is both good because it is safer to test new code outside of the main branch, and because it can be better for collaboration, if each person writes in their own branch and merges later. 

6: How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?

o---o---o  (main branch)
     \
      o  (feature branch)

The o's are commits. The first lines represent af timeline with commits, where another branch breaks off after the second commit. 

7: Give an example of a set of git commands that would result in a merge conflict.  

A merge conflict could happen if two people/branches are modifying the same part of a file, but in different ways. When they both push, a merge conflict will happen. 

8: Is Git suitable for latex documents?  

Yes, it is suitable. And apparently good.

9.	Should I from now on version my word and powerpoint slides using git? Why/why not?

Depends on the scope and length of the file. It can be useful for version control if the file is long. If it short, the tracking can be an inconvenience.


10.	What could happen when I push my latest commit to the remote repository without pulling first?

•  If someone else has pushed new commits after your last pull, Git will reject your push to prevent overwriting those changes.
•  You’ll see an error like:
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'origin/main'
hint: Updates were rejected because the remote contains work that you do not have locally.

11.	What happens when I pull without commiting my local changes first?

When Pulling (git pull) Without Committing Local Changes
•	If you pull updates from GitHub while having uncommitted changes, and both your local changes and the remote changes edit the same lines of a file, Git can’t decide which version to keep.
•	Example:
o	You change line 10 of index.html locally.
o	A teammate also changed line 10 and pushed their changes to GitHub.
o	When you git pull, Git detects the conflict and stops the merge.

12.	What is the difference between branching and forking?

Both branching and forking help you work on code separately, but they are used in different situations. 
Branching (Within the Same Repository)
•	A branch is a separate line of development within a single Git repository.
•	All branches share the same remote repository (e.g., origin/main).
•	Used for feature development, bug fixes, or experiments without affecting the main branch.

Forking (Creating a Separate Repository)
•	A fork is a complete copy of someone else’s GitHub repository into your own GitHub account.
•	Used when you don’t have direct access to the original repo (e.g., open-source projects).
•	Changes in the fork do not affect the original repository.

