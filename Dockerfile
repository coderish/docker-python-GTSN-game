FROM python:3.8
ADD songs.py .
ADD songs.csv .
# ADD main.py .
# RUN pip install requests beautifulsoup4
CMD ["python", "./songs.py"]