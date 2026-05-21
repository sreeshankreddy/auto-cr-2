import os
import openai
from dotenv import load_dotenv

# Load API Key (In production, use secure vault)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class AIReviewer:
    def __init__(self, model="gpt-4"):
        self.model = model

    def analyze_code(self, code_content, language, static_analysis_results):
        """
        Sends code and static analysis results to the LLM for deep analysis.
        """
        prompt = f"""
        Act as a senior software engineer. Perform a comprehensive code review on the following {language} code.
        
        Static analysis findings: {static_analysis_results}
        
        Code:
        {code_content}
        
        Provide a JSON response with:
        - issue_description
        - severity (Critical, High, Medium, Low)
        - suggested_fix
        - improved_code
        - explanation
        """
        
        try:
            # Note: This requires an active OpenAI API key or replacement with another LLM provider
            if not openai.api_key:
                return {"error": "OpenAI API key not configured"}
                
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "system", "content": "You are a code review expert."},
                          {"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return {"error": str(e)}

    def chunk_code(self, code, max_tokens=2000):
        """Simple chunking mechanism."""
        # For demonstration, simple split by lines
        lines = code.splitlines()
        chunks = []
        current_chunk = ""
        for line in lines:
            if len(current_chunk) + len(line) < max_tokens:
                current_chunk += line + "\n"
            else:
                chunks.append(current_chunk)
                current_chunk = line + "\n"
        chunks.append(current_chunk)
        return chunks
