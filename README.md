# Bank Branch API Server

## Overview

This project is a Django-based API server that provides details about banks and their branches through both REST API endpoints and GraphQL. It efficiently handles bank-related data, offering both flexibility and ease of integration.

---

## Features

- **REST API Endpoints**:
  - Get the list of all banks.
  - Retrieve branch details for a specific bank.
  
- **GraphQL Support**:
  - Query bank details and branch information from the `/gql` endpoint.
  
- **Bonus Points**:
  - Clean and maintainable code.
  - Test cases to ensure the functionality works as expected.

---

## Technologies Used

- **Django**: A high-level Python Web framework that encourages rapid development.
- **Graphene-Django**: A library that integrates GraphQL with Django.
- **SQLite** (or any other database): For data storage.
- **Django Test Framework**: To implement test cases.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd bank-branch-api
