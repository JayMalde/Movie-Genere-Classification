from django.shortcuts import render
import pickle
from bs4 import BeautifulSoup
import re
from bs4 import BeautifulSoup
from requests import get

def predict(request):
	filename = 'movie-genre-mnb-model.pkl'
	classifier = pickle.load(open(filename, 'rb'))
	cv = pickle.load(open('cv-transform.pkl','rb'))
	message = request.POST.get('message')
	data = [message]
	vect = cv.transform(data).toarray()
	my_prediction = classifier.predict(vect)
	prediction=int(my_prediction)
	predictionSTR=""
	if prediction==0:
		predictionSTR="Miscellaneous"
	elif prediction==1:
		predictionSTR="Action"
	elif prediction==2:
		predictionSTR="Adventure"
	elif prediction==3:
		predictionSTR="Comedy"
	elif prediction==4:
		predictionSTR="Drama"
	elif prediction==5:
		predictionSTR="Horror"
	elif prediction==6:
		predictionSTR="Romance"
	elif prediction==7:
		predictionSTR="Sci-Fi"
	elif prediction==8:
		predictionSTR="Thriller"
	context={"predictionSTR":predictionSTR}
	return render(request,'results.html',context)

def mainpage(request):
	if request.method == "POST":
		title = request.POST.get('web_link', None)
		title = title.replace(" ","+")
		websiteLink = "https://www.imdb.com/search/title/?title="+title
		url = websiteLink
		source = get(url)
		soup = BeautifulSoup(source.content, 'html.parser')
		content = soup.find(id='main')
		articleTitle = soup.find("h1", class_="header").text.replace("\n", "")
		content = soup.find(id="main")
		articleTitle = soup.find("h1", class_="header").text.replace("\n", "")
		movieFrame = content.find_all("div", class_="lister-item mode-advanced")
		movieFirstLine = movieFrame[0].find("h3", class_="lister-item-header")
		movieTitle = movieFirstLine.find("a").text
		movieYear = re.sub(r"[()]", "", movieFirstLine.find_all("span")[-1].text)
		movieRuntime = movieFrame[0].find("span", class_="runtime").text[:-4]
		movieGenre = movieFrame[0].find("span", class_="genre").text
		movieRating = movieFrame[0].find("strong").text
		movieDesc = movieFrame[0].find_all("p", class_="text-muted")[-1].text.lstrip()
		movieCast = movieFrame[0].find("p", class_="").text
		context={'movieTitle': movieTitle, 'movieYear': movieYear, 'movieRuntime': movieRuntime, 'movieGenre': movieGenre,'movieRating': movieRating, 'movieDesc': movieDesc, 'movieCast': movieCast}
		return render(request, 'index.html',context)
	return render(request, 'index.html')

