# Get cityflow package and ubntu op
FROM cityflowproject/cityflow

# Create a folder we'll work in 
WORKDIR /usr/python-code

# Upgrade installed packages
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Install vim to open & edit code\text files
RUN apt-get install -y vim

# Install all python code depentences
RUN pip install gym && \
    pip install numpy && \
    pip install IPython && \
    pip install torch && \
    python -m pip install python-dotenv

# Copy all file from current location - ignore files
COPY . .

# run the main function to create replay
# RUN python src/main.py
CMD ["python", "-u", "src/models/DRL/run_dqn.py" ]