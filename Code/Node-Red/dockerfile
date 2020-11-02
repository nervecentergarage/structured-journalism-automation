FROM nodered/node-red

WORKDIR /src/node-red

# Copy package.json to the WORKDIR so npm builds all of your added nodes modules for Node-RED
COPY package.json .

RUN npm install --unsafe-perm --no-update-notifier --no-fund --only=production
RUN npm install node-red-contrib-finite-statemachine
RUN npm install node-red-contrib-dashboard

# Copy _your_ Node-RED project files into place
#COPY settings.js settings.js
#COPY flows_cred.json /data/flows_cred.json
COPY FSM_Journalist_Editor.json .

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 8080

# Run the specified command within the container.
CMD [ "npm" ]

# You should add extra nodes via your package.json file but you can also add them here:
#WORKDIR /usr/src/node-red
