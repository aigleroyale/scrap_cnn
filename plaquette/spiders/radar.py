import scrapy
from pydispatch import dispatcher
from scrapy import signals
import urllib
import urllib.request, urllib.parse, urllib.error 
import pandas as pd
from scrapy.utils.trackref import NoneType






class RadarSpider(scrapy.Spider):
    # France(fr) = [0,100], Belgique(be) = [,] ,Espagne(es)= [,], Monaco(mc)=[,],Luxembourg(lu),USA(us) = [,]

    pays = ['us']
    for i in pays :
        baseUrl = f'http://platesmania.com/{i}/gallery-'
        name = 'radar'
        allowed_domains = ['platesmania.com']
        start_urls = [f'http://platesmania.com/{i}/gallery'] # sous domaine 
        
        
        page = 0
        page_max = 100 
       
        DIRECTORY_IMG_PLATE = '/Users/aristotemutombo/Desktop/DeeplearningProjet/PAYS/USA_Plate/'
        DIRECTORY_IMG_GLOBAL = '/Users/aristotemutombo/Desktop/DeeplearningProjet/PAYS/USA_Global/'

        
        

        
         

        def parse(self, response):
        # J'utilise des selecteurs HTML pour atteindre mes images souhaités sur le site distant
        # Mais vous pouvez utiliser aussi des selecteurs CSS
        # Je récupère ici 6 images par page
            imgContenerAll = response.xpath('.//div[@class="panel panel-grey"]')

            # Pour mes 10 images par page :
            for imgContener in imgContenerAll:
                # J'utilise de nouveaux selecteur
                panelBody = imgContener.xpath('div[@class="panel-body"]')
                
                # Je récupère les champs de texte voulu (attribut text())
                carType = panelBody.xpath('.//h4/a/text()').get().split(' ')
                dateType = panelBody.xpath('.//p/small/text()').get().split(' ')

                voitureMarque = carType[0]
                voitureModele = carType[1]

                # car l'arg 0 est un espace
                dateAjout = dateType[1]
                heureAjout = dateType[2]

                subContenerImgGlobal = imgContener.xpath('.//div[@class="row"]')[1]
                subContenerImgPlate = imgContener.xpath('.//div[@class="row"]')[2]

                # Je récupère les urls vers les images (via attribut @src)
                urlImgGlobal = subContenerImgGlobal.xpath('.//a//img/@src').get()
                urlImgPlate = subContenerImgPlate.xpath('.//a//img/@src').get()
                plateNumber = subContenerImgPlate.xpath('.//a//img/@alt').get()

                imgGlobalName = urlImgGlobal.split('/')[-1]
                imgPlateName = urlImgPlate.split('/')[-1]

                # Déstination ou sauvegarder nos images, on prends les folder de base et on ajout le nom de l'image
                destinationFolderImgPlate = self.DIRECTORY_IMG_PLATE + imgPlateName
                destinationFolderImgGlobal = self.DIRECTORY_IMG_GLOBAL + imgGlobalName

                
                # On créer un n-uplet de donnée, selon notre image en cours de scraping
                data = {
                        'date': dateAjout,
                        'heure': heureAjout,
                        'voitureMarque': voitureMarque,
                        'voitureModele': voitureModele,
                        'imgGlobalName':urlImgGlobal,
                        'imgPlaqueName': urlImgPlate,
                        'plateNumber': plateNumber
               }
                
                
                 
    


                
                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0')]
                urllib.request.install_opener(opener)

                urllib.request.urlretrieve(urlImgGlobal, destinationFolderImgGlobal)
                urllib.request.urlretrieve(urlImgPlate, destinationFolderImgPlate)

                                
               



            self.page += 1
            
            # On demande à Scrapy d'aller scrap la page suivante souhaité
            if self.page < self.page_max:
                yield scrapy.Request(url=self.baseUrl+str(self.page), callback=self.parse)
        



        # on ajoute la comande suivante scrapy runspider radar.py -o data.csv
        # en suite pour le fichier jsaon on ajoute : FEED_ EXPORT_ENCODING = 'utf-8'dans settings
                    
                    

                
                
                    
                
                

                