# Line Chat Bot: Zero to Hero

## Overview
A comprehensive guide to building a Line Chat Bot from scratch, integrating various tools, databases, and analytics platforms, and deploying the bot to production.

---

### Table of Contents
1. [Line Developer 101](./line-dev-101/)
2. [Rich Menu and Line Message Types](#rich-menu-and-line-message-types)
3. [Storing Chat Data with MongoDB](#storing-chat-data-with-mongodb)
4. [Web Development 101](#web-development-101)
5. [Line LIFF and Continuations](#line-liff-and-continuations)
6. [Dialogflow 101](#dialogflow-101)
7. [Dialogflow with Generative AI](#dialogflow-with-generative-ai)
8. [Deploying to Production](#deploying-to-production)

---

### 1. Line Developer 101
- **Introduction to Line Messaging API, Events, and SDK**
- **Creating a Line Official Account (OA) and Generating Tokens**
- **Installing Required Libraries and Tools**
- **Building a Webhook with FastAPI**
- **Connecting Line OA to the Webhook**

### 2. Rich Menu and Line Message Types
- **Creating a Rich Menu**
- **Overview of Different Message Types**
- **Sending Various Message Types with Python**
- **Implementing Quick Reply**

### 3. Storing Chat Data with MongoDB
- **Introduction to MongoDB**
- **Setting up a Database on MongoDB**
- **Getting Started with pymongo**
- **Storing Message Events from the Line Bot in MongoDB**

### 4. Web Development 101
- **Understanding Basic Web Development Concepts**
- **Creating a Web Frontend with HTML and Tailwind CSS**
- **Building a Backend API with FastAPI**
- **Routing the Webhook, API, and Frontend Together**

### 5. Line LIFF and Continuations
- **Connecting the Frontend with Line LIFF**
- **Storing Data in MongoDB**
- **Basic Analytics with Power BI Desktop**
- **Querying Data for Broadcasts**

### 6. Dialogflow 101
- **Setting up Dialogflow**
- **Creating Basic Intents**
- **Connecting Python to Dialogflow**

### 7. Dialogflow with Generative AI
- **Creating Intents Connected to Gemini**
- **Setting up Document AI**
- **Creating Intents Linked to Document AI**

### 8. Deploying to Production
- **Introduction to Docker**
- **Creating a Docker Image**
- **Deploying Docker with Cloud Run**

---

## Prerequisites
- **MongoDB**
- **Python 3.13**
- **Line Developer Account**
- **Ngrok**
- **Postman**
- **GCP Account**
- **MongoDB Atlas**
- **GCP Account**
- **Docker**
- **Power BI Desktop**

## Installation

### Clone the Repository
1. Clone the repository:
   ```bash
   git clone https://github.com/falukelo/linedev-zero2hero.git
   ```

2. Navigate to the project directory:
   ```bash
   cd line-chat-bot-zero-to-hero
   ```

### Install required dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Installing ngrok

**ngrok** is essential for creating a secure tunnel to test the webhook locally with Line's platform.

#### Windows
1. Go to the [ngrok download page](https://ngrok.com/download).
2. Download the **Windows** version.
3. Extract the downloaded file and move `ngrok.exe` to a preferred location, such as `C:\ngrok`.
4. Add ngrok to your PATH:
   - Open the **Command Prompt** as an administrator.
   - Run the following command to add ngrok to the PATH:
     ```cmd
     setx PATH "%PATH%;C:\ngrok"
     ```
5. Verify the installation by running:
   ```cmd
   ngrok --version
   ```

#### macOS
1. Open your terminal.
2. Install ngrok using Homebrew (if Homebrew is not installed, follow the instructions [here](https://brew.sh/)):
   ```bash
   brew install ngrok/ngrok/ngrok
   ```
3. Verify the installation:
   ```bash
   ngrok --version
   ```

### Add your Ngrok authentication token
Run the following command to add your authtoken to the default ngrok.yml:
   ```bash
   ngrok config add-authtoken <Your_Ngrok_token>
   ```
