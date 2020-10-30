# Steps to install “Docker”

Install docker from https://www.docker.com/products/docker-desktop

Follow the installation steps mentioned in the link https://nodered.org/docs/getting-started/docker
The node-red is deployed in the docker.
Deploy the Docker in the Heroku.
 
# Steps to install “Heroku”
Click on the link and sign-up http://heroku.com/
Click on the “Create new app”, under “New” button, and create an application in the Heroku.
Open the terminal window/command prompt
Login to the “Heroku” using the command and follow the below steps 

	$ heroku login
	$ docker tag nodered/node-red registry.heroku.com/nerve-center-automation/web
	$ heroku container:login
	$ docker push registry.heroku.com/nerve-center-automation/web
	$ heroku container:release web --app nerve-center-automation
	$ heroku logs --app nerve-center-automation

Go back to the Heroku web, and launch the application by clicking the “Open app”
The node red will be launched and below is the url to access 
https://nerve-center-automation.herokuapp.com/

# Steps to install “node red”
Node-red installed in the system. Installation of Node-red locally https://nodered.org/docs/getting-started/local

Upon Node-red installation, the required nodes shall be available by  navigating to “Manage Palette->Palette” option found on top-right in the Node-red window.

## The Node-red flow consist of:
Timestamp node(Inject node)- to trigger the flow

			Module : node-red : inject (Core node)

			Description: Will inject the message into the flow at regular intervals.

finite-state-machine - A finite state machine implementation for node red
	Module: node-red-contrib-finite-statemachine : finite-state-machine
	Description: This node will have the transition from different states.

msg payload node - to debug and display in the sidebar

			Module : node-red : debug (Core node)

			Description : It displays the message property in the sidebar, and through msg.payload we get to see the full message of the JSON expression.

## Steps to display the transition of different states:
	•	Trigger the node timestamp upon each different transition state.

