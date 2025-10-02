# Deploy to Render.com

## Steps to Deploy Your Stock Analyzer AI

### 1. Create a GitHub Repository
1. Go to [GitHub.com](https://github.com) and create a new repository
2. Upload your project files to the repository
3. Make sure all files are committed and pushed

### 2. Deploy to Render
1. Go to [Render.com](https://render.com) and sign up/login
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `stock-analyzer-ai`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && python main.py`
   - **Plan**: Free

### 3. Set Environment Variables
In the Render dashboard, go to Environment Variables and add:
- **Key**: `GEMINI_API_KEY`
- **Value**: `AIzaSyD2Kx9FgTyHpTX5ZUOsCpy6DaC4fTqYGU8`

### 4. Deploy
Click "Create Web Service" and Render will automatically deploy your app!

### 5. Access Your Live App
Once deployed, you'll get a URL like: `https://stock-analyzer-ai.onrender.com`

## Features Included
- ✅ Google Gemini AI integration
- ✅ Real-time stock analysis
- ✅ Beautiful responsive UI
- ✅ Free hosting on Render
- ✅ Automatic deployments from GitHub

## File Structure
```
HW2/
├── backend/
│   ├── main.py          # Flask backend
│   └── requirements.txt # Python dependencies
├── index.html           # Frontend
├── render.yaml         # Render configuration
└── deploy.md           # This file
```
