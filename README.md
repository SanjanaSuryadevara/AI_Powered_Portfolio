# AI-Powered Portfolio Website Generator

An intelligent web application that automatically generates a modern, responsive portfolio website from a user’s resume using Google Gemini (Generative AI).
The tool extracts resume content and produces HTML, CSS, and JavaScript files, packaged into a downloadable ZIP for instant deployment.

## Features

Resume Parsing
Supports PDF resumes using PyPDF2
Supports DOCX resumes using python-docx
AI-Powered Website Generation

Automatically generates:
index.html
style.css
script.js

Produces a visually appealing, responsive portfolio with modern UI design
User-Friendly Interface
Built with Streamlit

Simple workflow: upload → generate → download
Instant Deployment
Downloads a ZIP file containing the complete website
Ready for GitHub Pages, Netlify, or Vercel

## How It Works

1.Upload Resume
The user uploads a resume in PDF or DOCX format.

2.Text Extraction
The application extracts key details such as:

Name
Skills
Experience
Projects
Education
Contact information

3.AI Code Generation
Google Gemini processes the extracted text and generates structured HTML, CSS, and JavaScript for a portfolio website.

4.Download & Deploy
All files are packaged into a ZIP file for easy download and deployment.

## Technologies Used
Streamlit	- Web application interface
Google Generative AI (Gemini SDK)	- AI-based content & code generation
PyPDF2 - PDF resume parsing
python-docx	- DOCX resume parsing
zipfile	- Packaging website files
python-dotenv	- Secure API key management
