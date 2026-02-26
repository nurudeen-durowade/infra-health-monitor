# 1.  your base Image (Official python Image)
FROM python:3.12-slim


# 2. Set your working directory
WORKDIR /app

# 3. Install dependencies

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt


# 4. Copy all project files

COPY . .



# command to run when container start

CMD [ "python3", "main.py" ]







