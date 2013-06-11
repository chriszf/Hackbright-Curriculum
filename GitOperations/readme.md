Exercise Git: Version Control
=======

First, make a Github account. I recommend using your twitter username if available. Next, go through:

http://try.github.com

After you've run through that, head over to the folder you used when completing Exercise01. If your code isn't in a folder called Exercise01 (or similar) already, do a `mkdir Exercise01`, move your files there with `mv` and then `cd` into that folder. Next, in your Exercise01 folder run the following commands. 

`git init`

This creates a new `git` _repository_, which is like a database that saves every change you make to a line in a file. It remembers what line and what characters you change, with what changes you make, so that if two people work on the same file it can easily merge the two files together. You don't have to run this command more than once in a folder, because the folder is now a repository. It's like the folder gains new commands, in addition to `ls`, `cd`, `pushd` and `popd` you can now run a multitude of commands beginning with the word `git`.

`git init` should only happen on a "project", not on all your folders. Never try to make a `git` repository in a folder above one that already has a `git` repo. Here's an example -
	~/src/exercises/exercise01 - if this folder has a repository in it (type `git status` to see)
	~/src/exercises - this folder should NOT have `git init` run in it, because your computer can become very confused.

A `git` repository is like a folder, it has individual settings and properties, all of which you can change. Each repository is different, and can have different settings. Let's try setting some now. 
	`git config user.name "Your Name Here"`
	`git config user.email "your_email@example.com"` -- Use the email you've associated with your github account.

If you leave this repository, these settings don't follow you up the directory tree. If you for instance create an Exercise02 folder, and do `git init` to create a repository there, you'll need to setup these settings again. Because the computer will change every day, this is something you'll need to get used to doing. On your laptop however, you can follow github's 'set up git' tutorial to make these settings global. The settings in your Exercise01 folder will still be there when you get back to that folder, however.

Next, `git` doesn't know what files you want it to track, so we're going to have to tell it. 
`touch readme.md` will create a file in this directory, but it will be blank. You'll need to put something in it with the `subl` command - so type `subl readme.md` and add some text. This will be visible to the world soon, so put something you're OK with people seeing. "First programming exercise at Hackbright!" is a good candidate.
Now on to adding files. 
`git add readme.md` will add the readme file you just made to `git`'s database, and tell it to save it next time you "commit". `git` now knows about the file, but you haven't told `git` to save the most recent copy. Let's do that now with `git commit -m'Initial Commit'`.

We need to break down that command, so let's look at the pieces.
`git` is the program we're using to keep track of versions of files.
`commit` saves a version of everything you've added to the commit as it is right now.
`-m''` is a flag that means "message". It takes an argument, which is what those '' are for. Inside the '' ("" is also fine) you put a message describing what you did to the file, or files. Something like "added sort function" or "fixing typos on homepage", which summarizes the task you were trying to accomplish. This helps when you need to go back and figure out what you did, or when you need to find an example of a time when you wrote something. It's essentially notes to yourself, or to your team.

This brings us to the next part, where you might have to actually share code - either with people, or just between computers. What we're going to do is create a "remote". The nice thing about keeping our changes line-by-line and character-by-character is that we can just send all of those changes to another computer, apply them in order, and reconstruct the whole file. Then, if you make a change, all you have to do is send the change. The way we send these changes is by establishing a remote. 

When we add a remote, much like when we do any other configuration, it only exists for that repository. Outside of the folder our repository is in, none of these settings exist. Let's try adding a remote to our repository:
`git remote add git remote add origin https://github.com/[your username goes here]/Exercise01.git`

Now we have a remote - this is like a portal that goes to whatever URL we point at. Let's break down that command.
`git remote` refers to the part of the git program that allows us to add a list of URLs that we can send and receive code from. This is kind of like a cross between a bookmark and an FTP server. 
`origin` This is a nickname for the remote. We can put ANY word here we want - Liz personally uses "github", but it's common on the Internet to see "origin" used for github.
`https://github.com/[your username goes here]/Exercise01.git' should reference a URL that is either a github repository you've already created, or one you haven't created yet under your username. That is to say, if you reference a repo that doesn't exist on Github but it's under your own user, then pushing to it as yourself will create it.

So, now that we've established a portal link, what do we do with it? Same thing you'd probably do if you actually opened a portal to the server room at Github. Push things through it and see what happens.

`git push origin master`

See how we referenced origin there? That's the nickname of the portal - it tells `git` what portal to mischievously push things through. You might wonder about what "master" means - that's the name of the branch. For now, we'll have only one branch, so we'll always type master there. In the Further Reading section, there's some information about branching.

Once you've typed `git push origin master` git will ask you for a username - this is the username you signed up with github under. Then, it will ask for a password. When you type, you may be used to seeing asterisks(*) appear, but nothing will show up instead of just displaying your password for the world to see - so don't worry about typing it in in front of your partner.

After this, head over to your Github profile. You should see your new repo has been created, and any files you've added should have been pushed to the server. This is the simplest way to back up your work to the cloud, share code between teams, and make sure you remember what you did, when you did it, with notes to yourself.


Further Reading
========

Information about Branching
http://pcottle.github.com/learnGitBranching/

Here's a very through overview of Git and how it works.
http://ftp.newartisans.com/pub/git.from.bottom.up.pdf

Even more through, is this book:
http://git-scm.com/book/en
