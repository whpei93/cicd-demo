FROM python
ADD ./ /opt/
WORKDIR /opt
RUN pip install -r requirements.txt
ENV PORT 80
EXPOSE 80

CMD ["python", "hello.py"]
