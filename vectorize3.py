# coding: utf-8
from stemming import *
import numpy as np
np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from nltk.corpus import stopwords


corpus=['Rendez vous au Boogie Spirit Festival ce weekend a Illkirch',
        'Samedi 6 Fevrier, a la ComedieFr pour voir La Double inconstance de Marivaux',
        'Toujours personne pour le 104paris ce soir  Une piece pleine humour qui mele theatre et danse, ca ne vous dit pas ?'
        ,'Pour les fans de reecritures de contes, ne manquez pas The Forbidden Wish le 23 fevrier prochain',
        'a ne pas manquer : le 18e Printemps des Poetes du 5 au 20 mars',
        'Votre nouvelle serie inedite debarque dans 17 jours !',
        ' AmirOff : son 1er album en francais AuCoeurDeMoi sortira le 29 Avril 2016 !',
         'On vous dit tout mardi 1er mars sur le prochain evenement de FondationAvec soutenu par Nagui ! ca va etre fou ! ',
         ' inauguration de lAudencia Alumni Corner le nouvel espace dedie diplomes audencia en image !' 
         ,'Rendez vous ce dimanche 28 fevrier pour Aubagne1895 !',
         'Retrouvez ce soir humouriste Thomas Ngijol au circle royale 20h00'
         ,'Un Salon qui annonce riche pour le monde du droit !!!'
         , 'Avec les potos on est en spectacle le 9 et 10 mars au theatre de Cambrai !! Venez'
         'Au tour de Caroline et Frank  de nous entretenir des tendances en technologie evenementielle.'
         ,'Rencontre debat -Ville post-carbone Enjeux et Adaptations ',
         'Vous organisez un evenement prochainement ? Dites le nous',
         'Marasme dans les grands evnements et festivals'
         ,'En avril, Prestige Prod propose un weekend humour et chansons'
         ,'Conference sur le film Lumumba a Universite Anvers'
         ,'ibrahimovic a ete decisif en ligue des champions'
         ,'Festival de la musique et de la danse contre la guerre au Kivu ']

corpus_stemmed=corpus_stemmed(corpus)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
M,P=X.shape

print("taille du corpus origin : ",M)
print("taille du vocabulaire avant optimisation : ",P)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus_stemmed)
M,P=X.shape

print("taille du corpus : ",M)
print("taille du vocabulaire apres optimisation (stemming): ",P)

stwf=stopwords.words('french')
stwf.append('les')
vectorizer=CountVectorizer(stop_words=stwf)
X = vectorizer.fit_transform(corpus_stemmed)
M,P=X.shape

print("taille du corpus : ",M)
print("taille du vocabulaire apres optimisation (stemming) et suppression des stopwords: ",P)
print("Mon vocabulaire")
print(vectorizer.vocabulary_)
print("Mes vecteurs")
print (X.toarray())
