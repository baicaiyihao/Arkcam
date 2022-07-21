# from calery_tasks.moules import WebUrls
# from calery_tasks.main import app
# import requests
#
#
#
# @app.task(bind=True,default_retry_delay=5)
# def url_alive(self,urls):
#     url = []
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
#     }
#     try:
#         a = WebUrls.objects.all()
#         for i in a:
#             url.append('http://' + i.urls)
#             url.append('https://' + i.urls)
#
#
#     except:
#         raise self.retry(exc=Exception('重新扫描'), max_retries=5)