# React
* Javascript Library , created by Meta, developing user interfaces
* Single page Application(SPAs)
* UI is broke down into small reusable components

# WebApplication
Browser--->ReactApp-->REST API--->Backend Server-->Database

# Vite--Build Tool:
    * smartHR-App
    * npm create vite@latest smartHR-App

# Application project Structure
   * components
    * common/Header
        * Header.jsx
        * Header.css

    * common/Footer
        * Footer.jsx
        * Footer.css

## creating Folder
mkdir src/components/common/Header
mkdir src/components/common/Footer

mkdir src/pages/Home

## Create Files
touch src/components/common/Header/Header.jsx
touch src/components/common/Header/Header.css
# touch Commands
touch src/components/common/Footer/Footer.jsx
touch src/components/common/Footer/Footer.css

touch src/pages/Home/Home.jsx
touch src/pages/Home/Home.css
## install touch package
* npm i -g touch-cli
* npm i touch-cli


# routing
* npm i react-router-dom

* import {BrowserRouter as Router,Routes,Route}from 'react-router-dom

## Props
* are used to pass data from Parent component to Child Component
* read only