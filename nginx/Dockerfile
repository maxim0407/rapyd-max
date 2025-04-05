# Use the official Nginx image from Docker Hub
FROM nginx:latest

# Copy custom configuration file, if needed
COPY nginx.conf /etc/nginx/nginx.conf
COPY certs /etc/nginx/certs
# Expose port 443
EXPOSE 443