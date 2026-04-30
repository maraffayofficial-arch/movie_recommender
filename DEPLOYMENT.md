# Deployment Guide - Movie Recommender System

## Free Deployment Options

### Option 1: Streamlit Community Cloud (Recommended)

**Why:** Free, built for Streamlit apps, supports Git LFS natively.

**Steps:**

1. **Push to GitHub with Git LFS**
   ```bash
   git commit -m "Add pickle files with Git LFS"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `movie_recommender`
   - Main file path: `app.py`
   - Click "Deploy"

3. **Add Environment Variables**
   - In Streamlit Cloud dashboard, go to App settings
   - Add secret: `TMDB_API_KEY = your_api_key_here`

**Done!** Your app will be live at `https://your-app-name.streamlit.app`

---

### Option 2: Hugging Face Spaces

**Why:** Free, supports large files up to 500MB, good for ML apps.

**Steps:**

1. Create account at [huggingface.co](https://huggingface.co)
2. Create new Space → Select "Streamlit"
3. Upload files or connect GitHub repo
4. Add `TMDB_API_KEY` in Space settings → Secrets
5. Space will auto-deploy

**URL:** `https://huggingface.co/spaces/your-username/movie-recommender`

---

### Option 3: Google Drive + Render/Railway (Alternative)

If Git LFS doesn't work, use cloud storage:

1. **Upload pickle files to Google Drive**
   - Upload `similarities.pkl` and `movies.pkl`
   - Get shareable links
   - Extract file IDs from URLs

2. **Modify app.py to download files**
   ```python
   import gdown
   import os
   
   # Download if not exists
   if not os.path.exists("similarities.pkl"):
       gdown.download("https://drive.google.com/uc?id=YOUR_FILE_ID", 
                      "similarities.pkl", quiet=False)
   
   if not os.path.exists("movies.pkl"):
       gdown.download("https://drive.google.com/uc?id=YOUR_FILE_ID", 
                      "movies.pkl", quiet=False)
   ```

3. **Add gdown to requirements.txt**
   ```
   gdown==5.1.0
   ```

4. **Deploy to Render or Railway**
   - Connect GitHub repo
   - Add `TMDB_API_KEY` environment variable
   - Deploy

---

## Current Setup

✅ Git LFS configured for `*.pkl` files  
✅ Pickle files staged and ready to commit  
✅ `.gitignore` updated  
✅ Environment variables configured with `.env`

## Next Steps

1. Commit the changes:
   ```bash
   git commit -m "Add pickle files with Git LFS"
   ```

2. Push to GitHub:
   ```bash
   git push origin main
   ```

3. Deploy on Streamlit Community Cloud (easiest option)

## Troubleshooting

**Git LFS push fails?**
- Check GitHub LFS bandwidth limits (1GB/month free)
- Use Hugging Face Spaces instead (no LFS limits)

**App crashes on startup?**
- Check if pickle files downloaded correctly
- Verify `TMDB_API_KEY` is set in deployment platform

**Out of memory?**
- Streamlit Cloud free tier: 1GB RAM
- Hugging Face Spaces: 16GB RAM (better for large models)
