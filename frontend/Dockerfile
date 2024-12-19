# Use the official Node.js 14 image as the base image for the frontend build stage
FROM node:14.17.0 as frontend

# Set the working directory inside the container to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the dependencies specified in package.json
npm install

# Copy the rest of the application code to the working directory
COPY . .

# Build the application and output the result to the dist directory
RUN npm run build --output-path=dist

# Use the official Nginx image as the base image for the final stage
FROM nginx:1.21.6-alpine

# Copy the built application from the frontend build stage to the Nginx html directory
COPY --from=frontend /app/dist /usr/share/nginx/html

# Expose port 80 to allow external access to the application
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]