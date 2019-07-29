FROM python
ADD ./ /opt/
WORKDIR /opt/cicd
RUN pip install -r /opt/requirements.txt
ENV PORT 80
EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
