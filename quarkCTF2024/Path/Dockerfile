FROM python:3.9-slim

WORKDIR /app

COPY src/. .

RUN pip install --no-cache-dir -r requirements.txt

RUN echo 'quarkCTF{fake_flag_for_testing}' > /flagULBLDSKF.txt

RUN chmod 555 /app
RUN chmod 444 /flagUTLSCS.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

