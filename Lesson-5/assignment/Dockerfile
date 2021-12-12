# using Ubuntu LTS version 
FROM python:3.10

ADD getUser.py .

# create and activate virtual environment
# using final folder name to avoid path issues with packages
RUN python3 -m venv /home/gil/venv
ENV PATH="/home/gil/venv/bin:$PATH"

# install requirements
RUN pip install --no-cache-dir getpass3
RUN pip install --no-cache-dir requests

RUN useradd --create-home gil

USER gil

# activate virtual environment
ENV VIRTUAL_ENV=/home/gil/venv
ENV PATH="/home/gil/venv/bin:$PATH"

COPY getUser.py /home/gil/venv

CMD [ "python", "/getUser.py" ]
