FROM tomcat:10.1.28-jre21-temurin-noble

# Copy your WAR file to the Tomcat webapps directory
COPY target/app.war /usr/local/tomcat/webapps/

# Set the entrypoint to start Tomcat
ENTRYPOINT ["catalina.sh", "run"]
