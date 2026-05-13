FROM python:3.10-slim

# Create non-root user with UID 1000 to comply with Hugging Face Spaces security constraints
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=user . /app

EXPOSE 7860

CMD ["python", "Guardian/main.py"]
