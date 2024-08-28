FROM tomcat:9.0-jdk11-openjdk

# Copy your WAR file to the Tomcat webapps directory
COPY target/app.war /usr/local/tomcat/webapps/

# Set the entrypoint to start Tomcat
ENTRYPOINT ["catalina.sh", "run"]
