# library imports
import requests
import re
from scrapy.http import HtmlResponse

class WebDigger:
	def __init__(self):
		self.headers = {
			'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

		self.finalList = []
		self.weblinks = []

		self.searchTerm =''
		self.curChoice = ''

		self.search_result_link_xpath = "//div[@class='rc']/div[@class='r']/a/@href"
		self.url_extract_xpath = "//a[not (contains(text(), '../') or contains(text(), 'Parent Directory') or contains(text(), 'Size') or contains(text(), 'Name') or contains(text(), 'Last modified') or contains(text(), 'description'))]/@href"

		self.google_page_seach_url_format = "https://www.google.com/search?q={}%20%2B({})%20-inurl%3A(jsp%7Cpl%7Cphp%7Chtml%7Caspx%7Chtm%7Ccf%7Cshtml)%20intitle%3Aindex.of%20-inurl%3A(listen77%7Cmp3raid%7Cmp3toss%7Cmp3drug%7Cindex_of%7Cwallywashis)"

		# File valid extensions (file links should end with these extensions)
		self.ext1 = ['mkv', 'mov', 'avi', 'mp4', 'mpg', 'wmv']
		self.ext2 = ['mp3', 'wav', 'ac3', 'ogg', 'flac', 'wma', 'm4a']
		self.ext3 = ['mobi', 'pdf', 'rtf', 'doc', 'docx', 'txt']
		self.ext4 = ['exe', 'iso', 'tar', 'rar', 'zip', 'apk']
		self.ext5 = ['jpg', 'png', 'bmp', 'gif', 'tif', 'tiff', 'psd']

	def startFunc(self, searchTerm, contenttype):
		self.searchTerm = searchTerm

		if contenttype == '1':
			self.curChoice = self.ext1
		elif contenttype == '2':
			self.curChoice = self.ext2
		elif contenttype == '3':
			self.curChoice = self.ext3
		elif contenttype == '4':
			self.curChoice = self.ext4
		elif contenttype == '5':
			self.curChoice = self.ext5
		# elif contenttype == '6':
		# 	ext6 = input(
		# 		"\nEnter file extensions seperated by comma(,) -                 			For ex: txt,jpg,mp3\n\t")
		# 	ext6 = ext6.replace(',', ' ')
		# 	ext6 = ext6.split(' ')
		# 	ext6 = tuple(ext6)
		# 	ext = ext6

		try:
			self.start_search_list_parse(self.searchTerm, self.curChoice)
		except:
			pass

		return self.finalList

	# get every web link from google search results and store in 'weblinks' list
	def start_search_list_parse(self, searchTerm, ext):
		search_url = self.google_page_seach_url_format.format(searchTerm.lower(), '%7C'.join(ext))

		search_res = requests.get(search_url, headers=self.headers)
		resp = HtmlResponse(url=search_url, body=search_res.text, encoding='utf-8')	
		for res_url in resp.xpath(self.search_result_link_xpath):
			url = res_url.get().strip()
			self.weblinks.append(url)

		self.start_web_link_parse(self.weblinks)

	
	# get every matching result link from each web link from 'weblinks' list and store final result links in 'finalList' list
	def start_web_link_parse(self, web_links):
		for web_url in web_links:
			try:
				url_res = requests.get(web_url, headers=self.headers, timeout=90)
				if url_res.status_code != 200:
					raise ''
				resp = HtmlResponse(url=web_url, body=url_res.text, encoding='utf-8')
			except:
				resp = ''
				continue

			if resp != '':
				for res_url in resp.xpath(self.url_extract_xpath):
					url = res_url.get().strip()
					if url[-1] == '/':
						self.start_web_link_parse(url)
					
					if url[0] == '/' and url_res.url[-1] == '/':
						url = url[1:]
					url = url_res.url + url
					self.matcher(url)


	def matcher(self, url):
		temp_url = re.sub('[^a-zA-Z0-9]', ' ', url)
		temp_search_term = re.sub('[^a-zA-Z0-9]', ' ', self.searchTerm)

		temp_url = " ".join(temp_url.split())
		temp_search_term = " ".join(temp_search_term.split())

		temp_term_list = temp_search_term.split()
		num_of_words = len(temp_term_list)
		count = 0

		for word in temp_term_list:
			if word.lower() in temp_url.lower():
				count += 1

		if count == num_of_words:
			for ext in self.curChoice:
				if ext.lower() in temp_url.lower():
					print(url)
					self.finalList.append(url)

if __name__ == "__main__":
	dg = WebDigger()
	dg.startFunc()