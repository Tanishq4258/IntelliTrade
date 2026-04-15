import google.generativeai as genai
import os

def summarize_news(articles):
    """
    Summarizes a list of news articles using Google Gemini API.
    Expects a list of dictionaries with a 'title' key.
    """
    api_key = os.environ.get('GEMINI_API_KEY')
    
    # Fallback/Instruction if no API key is provided
    if not api_key or api_key == "YOUR_GEMINI_API_KEY":
        return "AI Summary: Please configure GEMINI_API_KEY in your environment to see automated market insights."
    
    try:
        genai.configure(api_key=api_key)
        # Use flash model for speed and efficiency
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Combine titles for context
        bullet_points = "\n".join([f"- {a['title']}" for a in articles])
        prompt = f"Act as a professional financial analyst. Summarize the following news headlines into exactly two punchy, insightful sentences for a long-term investor:\n\n{bullet_points}"
        
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"AI Summary currently unavailable: {str(e)}"
