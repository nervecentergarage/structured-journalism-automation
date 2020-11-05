
# 1. Deploying Node-RED into Heroku  [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/nervecentergarage/structured-journalism-automation)

# 2. Set Username and Password for your Flow Editor
* NODE_RED_a_USERNAME - Create a user name and password.
* NODE_RED_b_PASSWORD - 



# 3. Export all flows as "flows.json" file AFTER you create your flow and deploy it
* In Editor, click hamburger icon (top right), click Export, choose tab "all flows", then Download.

# 4. Fork this repo, Set your github as deploy source on Heroku setting, and enable Automatic Deployment
* Push downloaded "flows.json" file to your repo on github.
* Every time "flows.json" pushed to your repo, Heroku will rebuild node-red with updated "flows.json".
* So your node-red will always have latest pushed "flows.json" when Heroku restarted.


