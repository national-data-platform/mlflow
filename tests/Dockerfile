FROM python:3.7

WORKDIR /server
COPY oidc_mock_server.py oidc_mock_server.py
COPY response.json response.json

CMD ["python3", "oidc_mock_server.py"]