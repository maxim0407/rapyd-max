# Installation

1. **Clone the Repository**  
    ```bash
    git clone https://github.com/rapyd-max.git
    cd rapyd-max
    ```

2. **Create Certificates**  
    Inside the project directory, create a `certs` folder to store SSL certificates:
    ```bash
    mkdir nginx/certs
    cd nginx/certs
    ```
    Then create the certificates
    ```bash
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout myapp.key -out myapp.crt
    ```


3. **Build and Run Docker Containers**  
    Ensure you have [Docker](https://www.docker.com/) installed, then execute:
    ```bash
    docker-compose up --build
    ```

4. **Access the Application**  
    Open your browser and navigate to:

    [https://myapp.com/collect-cat-fact](https://myapp.com/collect-cat-fact)

    [https://myapp.com/cat-facts](https://myapp.com/cat-facts)
