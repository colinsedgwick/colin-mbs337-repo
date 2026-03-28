# Homework 8  
The purpose of this homework project is to practice topics in development operations such as automation, testing, and deployment. A dash app is run from a container that is created using ```make``` commands defined in a Makefile. These commands run ```docker compose``` commands when called to orchestrate the containers using a docker-compose file. Staging versions of the ```make``` commands are also defined to run a staging version of the dash app from containers orchestrated by a staging docker-compose file. YAML files are used to define GitHub Actions workflows for integration testing on every push to the GitHub repo and publishing of images to the GitHub Container Registry every time a new tag is pushed.      
## How to Run the Dashboard   
The following commands can be run using targets defined in the Makefile to run and stop the production version of the dashboard. Adding "-staging" to the end of each of these commands allows you to do the same actions for the staging version of the dashboard:   
```make compose-up``` allows you to rebuild the image and run the dashboard from the created container   
```make compose-down``` allows you to stop the containers and the dashboard   
```make compose``` allows you to stop any running containers (and dashboard), rebuild the image, and run the dashboard from the newly created container   
### Production vs Staging   
Produciton deployments are the version of the dashboard that is available to the public for use, whereas staging deployments are for developers to use in testing before release to the public. Staging deployments should be used when making changes to make sure they are ready for release, and then those changes can be updated and released in the production deployment.   
## GitHub Action Workflows   
Using YAML files that define workflows within the .github/workflows directory in the root of the repository:   
1. **integration-test.yml** On every push to the GitHub repo, an integration test using pytest is used to confirm the dash app successfully runs.   
2. **push-to-registry.yml** Every time a new tag is pushed to the GitHub repo, a container image is automatically built and pushed to the GitHub Container Registry.   