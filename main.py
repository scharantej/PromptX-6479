
from flask import Flask, render_template, request
import openai

# Initialize the Flask app
app = Flask(__name__)

# Set the OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Main page route
@app.route("/")
def index():
    return render_template("index.html")

# Results page route
@app.route("/results", methods=["POST"])
def results():
    # Get the user's prompt
    prompt = request.form.get("prompt")

    # Get the selected LLM type
    llm_type = request.form.get("llm_type")

    # Set the LLM model to use
    model = openai.Model(llm_type)

    # Generate the LLM's response
    response = model.generate(
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7,
    )

    # Render the results page with the LLM's response
    return render_template("results.html", response=response["candidates"][0]["output"])

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
