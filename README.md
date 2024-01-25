
# Property  API

##  Descripción


Property Management API is a solution designed to seamlessly integrate with the AVM-API, an Automatic Valuation service based on Machine Learning models to predict the selling price of properties. This API provides a flexible interface that simplifies the management and retrieval of key real estate information.

Developed using the Python web framework, FastAPI, Property Management API offers a robust and efficient architecture following SOLID principles and good software development practices, with modular classes that allow easy code extension and maintenance.

## Contenido

1. [Access to the Application](#access-to-the-application)
2. [Installation](#installation)
3. [How to Use](#how-to-use)
4. [Project Structure](#project-structure)
5. [Authors and Contact](#authors-and-contact)
6. [Project Architecture](#project-architecture)

## Access to the Application

You can access the deployed application through the following link: [Property Management API - Access to the Application](https://property-management-api.onrender.com/docs)

In addition, interactive API documentation is available at:

- [Swagger UI (ReDoc)](https://property-management-api.onrender.com/redoc): Swagger's interactive user interface.
- [Swagger UI](https://property-management-api.onrender.com/docs): Swagger's interactive user interface.

## Installation

Follow the instructions in the README.md file to install and run the project locally. API documentation will be available at http://localhost:5001/docs after execution.

1. **Clone the Repository:**

```bash
git clone https://github.com/danielcinome/property-management-api.git
cd property-management-api
```

2. **Virtual Environment Configuration (Optional, but recommended):**

```bash
python -m venv venv
source venv/bin/activate   # For Unix-based systems (Linux/Mac)
```

3. **Installs Units:**

```bash
pip install -r requirements.txt
```

4. **Environment Variables Configuration:**

```
SECRET_KEY
ALGORITHM                       # Use case -> HS256
SQLALCHEMY_DATABASE_URL
```

* To generate the SECRET_KEY you can use:
    ```bash
    openssl rand -hex 32
    ```

5. **Initialize the Database:**


```bash
alembic upgrade head
```

6. **(Optinal):**

If you want to make use of docker, run the following command

```bash
docker-compose up --build
```

## How to Use

To execute the project use the command:

```bash
# Example of command or code
python runner.py # You can use or
make dev
```

![F1-1](https://aluhsxarndfgmqdktmrx.supabase.co/storage/v1/object/public/property-management-api/docs-api.png)

If you do not have your own user, you must generate a registration from `/user/create`.

- Then **click** on **Authorize** and enter your authentication credentials, once authenticated you will be able to use the mentioned services.

    ![F2-2](https://i.ibb.co/rt7FsgL/Captura-de-pantalla-2023-12-17-a-la-s-7-47-50-p-m.png)


## Project Structure

The current structure of the project is organized as follows:

```plaintext
│── alembic/
│── app/
    │── api/
    │   │── avm/
    │   │── city/
    │   │── core/
    │   │── crud/
    │   │── login/
    │   │── property/
    │   │── user/
    │── db/
    │   │── postgres/
    │       │── engine.py
    │   │── testing/
    │       │── engine.py
    │── integration/
    │       │── avm-api-adapter.py
    │── models/
    │   │── models.py
    │── tests/   
    │── main.py
│── requirements.txt
│── docker-compose.yaml
│── Dockerfile
│── Makefile
│── README.md
│── runner.py
```

- **alembic/**: Contains files related to Alembic, a database migration tool for SQLAlchemy. It is used to manage changes in the database schema.
- **app/**: Main directory of the application source code.
  - **api/**: Contains modules that define the API paths.
  - **db/**: It contains modules related to **database session** management for both **production** and **testing**.
  - **integration/**: Contains the adaptive design pattern for the handling of project-specific data.
  - **models/**: Contains `models.py`, where the data models used in the application are defined.

  - `main.py`: Main entry point of the application.

- **requirements.txt**: File that lists the project dependencies.
- **docker-compose.yaml**: Configuration for Docker Compose.
- **Dockerfile**: File to build the Docker image.
- **README.md**: Main documentation of the project.
- `runner.py`: File to run or start the application.

## Project Architecture

The project architecture is based on a backend application developed in Python using the FastAPI framework. The authentication is done through JSON Web Tokens (JWT) using OAuth2PasswordBearer. The design is oriented to provide a RESTful API that allows the management of process elements  and users.

![F1-1](https://aluhsxarndfgmqdktmrx.supabase.co/storage/v1/object/public/property-management-api/diagram-api.png?t=2024-01-24T21%3A40%3A06.599Z)

## Property Management API UML Diagram (Extended)

The UML diagram shows the class structure implemented in the Property Management API. Some of the key classes are described below:

#### **CRUDBase**

The `CRUDBase` class is a generic class that serves as the basis for the implementation of CRUD operations in other specialized classes, such as `CRUDUser`, `CRUDCity` and `CRUDProperty`.

#### **CRUDUser**

The `CRUDUser` class inherits from `CRUDBase` and focuses on user management. It provides functions for creating and obtaining users in the database.

-   **Methods:**
    -   `create`: Creates a new user in the database.
    -   `get_by_username`: Gets the information of a user by username.

#### **CRUDCity**

The `CRUDCity` class inherits from `CRUDBase` and focuses on city management. It provides CRUD operations to create and retrieve information about cities in the database.

-   **Methods:**
    -   `create`: Create a new city in the database.
    -   `get_city_by_name`: Gets information about a city by name.

#### **CRUDProperty**

La clase `CRUDProperty` hereda de `CRUDBase` y se especializa en la gestión de propiedades. Proporciona operaciones CRUD para crear, obtener, actualizar y eliminar propiedades en la base de datos.

-   **Methods:**
    -   `get_properties_by_city`: Gets properties by city name.
    -   `get_properties_by_area`: Gets properties by area value (zip code).

#### **PropertyStats**

La clase `PropertyStats` hereda de `CRUDProperty` y se encarga de calcular estadísticas relacionadas con las propiedades, especialmente el precio promedio por metro cuadrado en una ciudad o área específica.

-   **Methods:**

    -   `get_average_price_per_square_meter_by_city`: Calculates the average price per square meter for a given city.
    
    -   `get_average_price_per_square_meter_by_area`: Calculates the average price per square meter for a specific area.
    
    -   `_calculate_average_price`: Private method used to calculate the average price per square meter based on a list of properties.

This class adds statistical functionalities to property management, allowing for more advanced analysis of the data stored in the database.

![F1-2](https://aluhsxarndfgmqdktmrx.supabase.co/storage/v1/object/public/property-management-api/uml-project.png?t=2024-01-24T23%3A24%3A45.992Z)

### **Design Patterns Implemented in the Property Management API**
The development of Property Management API follows the principles of Object Oriented Programming (OOP), applying some design patterns to improve the structure, flexibility and maintainability of the code. The main design patterns implemented are:

-   **Singleton:**
    
    -   **Description:** Used in the `SingletonCRUDUser` class to ensure that only one instance of `CRUDUser` exists in the application. This avoids the creation of multiple instances, promoting efficiency and consistency in user management.
 
-   **Adapter:**

    -   **Description:** Implemented in the `AvmApiAdapter` class, the Adapter pattern allows the Property Management API to easily integrate with the external `AVM-API` service. The adapter (`AvmApiAdapter`) translates and adapts the data received from the external service to match the format and structure expected by the Property Management API.
    

## Authors and Contact
- Daniel Chinome
- Contact: danielchinomedev@gmail.com
- [LinkedIn](https://www.linkedin.com/in/danielchinome/)