# File Uploader and Tracker - Documentation

## How to Set Up and Run This Project

### What You Need Before Starting
- Python 3.8 or higher installed on your computer
- pip (comes with Python)

### Steps to Get It Running

1. Download the project:
```bash
git clone https://github.com/shrivastava03/File-Uploader
cd File_Uploader
```

2. Set up a virtual environment (this keeps the project isolated):
```bash
python -m venv venv
# If you're on Windows:
venv\Scripts\activate
# If you're on Mac or Linux:
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Database Setup:
Don't worry about creating a database manually! It gets created automatically when you first run the app. You'll see a new file called `filedata.db` appear in your project folder.

5. Start the backend server:
```bash
uvicorn backend.main:app --reload
```
This will start your backend on `http://127.0.0.1:8000`

6. Start the frontend:
I used VS Code's Live Server extension, but you can also use Python's built-in server:
```bash
Open Upload.html in frontend folder and Open with Live Server.


### How I Organized the Files
```
File_Uploader/
├── backend/
│   ├── routes/
│   │   ├── upload.py      # Handles file uploads
│   │   └── files.py       # Gets list of uploaded files
│   ├── uploaded_files/    # Where uploaded files are stored
│   ├── database.py        # Database connection setup
│   ├── models.py          # Database table structure
│   ├── schemas.py         # Data validation
│   └── main.py           # Main app file that starts everything
├── frontend/
│   ├── upload.html       # Upload page
│   ├── history.html      # Shows all uploaded files
│   └── style.css         # Makes things look nice
├── requirements.txt      # List of packages needed
└── DOCUMENTATION.md      # This file!
```

## My Design Decisions

### Why I Organized It This Way
I split everything into `backend` and `frontend` folders to keep things clean and separate. The backend has different files for different jobs - one for database stuff, one for file uploads, etc. This makes it easier to find and fix things later.

### Important Choices I Made

#### 1. How I Make Sure File Names Don't Clash
**What I did:** 
I add a random UUID to the front of every filename.

**Why I did this:**
Think about it - if two people upload files named "resume.pdf", they'd overwrite each other! So I add a unique ID to each one. For example, if you upload "document.pdf", it gets saved as something like "a1b2c3d4-5678-90ab-cdef-1234567890ab_document.pdf". This way, no two files ever have the same name.

#### 2. Saving Files vs Saving Database Info
**What I did:**
I save the actual file to the hard drive first, then I save the information about it in the database.

**Why I chose this order:**
I wanted to make sure the file actually gets saved before I tell the database about it. If I did it the other way around and the file failed to save, I'd have a database entry pointing to a file that doesn't exist. That would be confusing! This way, even if the database fails, at least the file is safely stored.

**Here's what happens:**
1. File gets saved to the `backend/uploaded_files/` folder
2. I check how big the file is using `os.path.getsize()`
3. I create a database entry with all the info (original name, new name, size, time)
4. I save everything to the database

#### 3. Why SQLite and SQLAlchemy?
**What I used:**
SQLite for the database and SQLAlchemy to talk to it.

**Why these choices:**
SQLite is perfect for a small project like this because it doesn't need a separate database server running - it's just a file! SQLAlchemy makes working with the database easier because I can write Python code instead of raw SQL queries. Plus, if this project ever needs to grow bigger, I can easily switch to PostgreSQL or MySQL without rewriting much code.

### Problems I Ran Into and How I Fixed Them

#### Problem 1: CORS Errors
**What went wrong:** 
When I first tried to upload files from the frontend, the browser blocked the request. It said something about CORS policy.

**How I fixed it:** 
I added CORS middleware to my FastAPI app that tells the browser "hey, it's okay for the frontend to talk to this backend." This let the frontend and backend communicate properly.

#### Problem 2: Getting the Right File Size
**What went wrong:** 
I wasn't sure whether to trust the file size from the upload request or measure it myself.

**How I fixed it:** 
I decided to measure the file size after saving it using `os.path.getsize()`. This way, I know I'm getting the actual size of the file that's stored on disk, not just what the browser said it was.

#### Problem 3: History Page Was Empty
**What went wrong:** 
When I first opened the history page, it was completely blank even though I had uploaded files.

**How I fixed it:** 
Turns out the database was empty! I checked my endpoints and added better error messages in the JavaScript code. Once I uploaded a test file and refreshed the history page, everything worked. I also learned to check the browser console for errors - it helped me debug faster.

## What Packages This Project Needs

Everything is listed in `requirements.txt`:
- `fastapi` - The web framework I used for the backend
- `uvicorn` - Runs the FastAPI server
- `python-multipart` - Lets FastAPI handle file uploads
- `sqlalchemy` - Helps me work with the database

## AI Tools I Used

I used Claude AI to help me with:
- Setting up the initial FastAPI structure
- Fixing some CSS styling issues
- Understanding CORS and how to fix it
- Updating my code to work with Pydantic V2

But I wrote all the main logic myself, made all the design decisions, and wrote this documentation without AI help.
