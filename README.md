STEMbox is an open-source Python library for solving STEM (Science, Technology, 
Engineering & Math) problems step by step.

# Git workflow

When adding a new feature, you should create a new branch that branches off the 
`develop` branch. The name of the new branch should start with `feat-`, e.g.  
`feat-polynom-deriv`. After implementing the feature, you should create a pull 
request to merge back into the `develop`branch. Once the pull request is 
accepted, the feature branch should be deleted.

The commit messages are formatted using 
[commitizen](http://commitizen.github.io/cz-cli/). The node package is included 
in `package.json`, so running `npm install` in the repo directory should 
suffice to get the necessary tools. Feel free to read the 
[docs](http://commitizen.github.io/cz-cli/) to learn more about commitizen.
