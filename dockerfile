# Use the official Python 3.11 image.
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the image
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# # Download the tiktoken encoding file by invoking tiktoken directly
# RUN python -c "import tiktoken; tiktoken.encoding_for_model('gpt-3.5-turbo'); tiktoken.get_encoding('cl100k_base')"

# # Download the Hugging Face and Sentence Transformer models and save them in the TRANSFORMERS_CACHE directory
# RUN python -c "from transformers import AutoTokenizer, BertModel, BertTokenizer; \
#     from sentence_transformers import SentenceTransformer; \
#     AutoTokenizer.from_pretrained('gpt2'); \
#     BertTokenizer.from_pretrained('bert-base-multilingual-uncased'); \
#     BertModel.from_pretrained('bert-base-multilingual-uncased'); \
#     SentenceTransformer('all-MiniLM-L6-v2')"

# Copy the rest of the application code
COPY . /app/

# # Copy the .env file to the working directory
# COPY .env /app/

# Make the start_app.sh script executable
RUN chmod +x /app/start_app.sh

# Expose the port the app runs on
EXPOSE 30005

# Command to run the app
# CMD ["gunicorn", "-k", "gevent", "-b", "0.0.0.0:10000", "--timeout", "30", "api:app"]

# Command to run the bash script
CMD ["./start_app.sh"]
