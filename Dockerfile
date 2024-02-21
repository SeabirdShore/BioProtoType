FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["main.py"]