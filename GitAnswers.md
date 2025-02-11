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

