Projet 4 : Analyser les données d'une grande chaîne de librairie
Par Amina BOUBLENZA YOUCEF
----------------------------------------------------------------------------------------
Fichiers et dossiers existants :
	- P4_01_scriptdonnées.ipynb : Contient le script pour nettoyer les données 
	- P4_02_scriptanalyse.ipynb : Contient le script pour analyser les données
	- P4_03_MyFunctions.py : Contient différentes fonctions (importé par P4_02_scriptanalyseipynb)
	- dataset_P4 : Contient les trois fichiers csv téléchargés pour la mission 
	- new_data : Contient les nouveaux fichiers CSV générés par P4_01_scriptdonnées.ipynb 
----------------------------------------------------------------------------------------	
Mise en oeuvre du projet :
	- Décomresser le dossier
	- Vérifier l'intégralité des fichiers et dossiers ci-dessus 
	- Pour afficher les résultats de ce projet, pas besoin de l'exécuter, il suffit de l'ouvrir avec Jupyter Notebook
		- P4_01_scriptdonnées.ipynb contient le nettoyage des données tout au long des missions
		Quand on exécute ce fichier, il va enregistrer les dataframes suivantes dans des fichiers CSV :
			# Les données originales sans les valeurs testes
			'new_data\\df_customers.csv' , 'new_data\\df_products.csv' et 'new_data\\df_transactions.csv'
			# Jointure des 3 DF, sans valeurs test, en remplaçant le produit 
			'new_data\\df_transaction_join.csv'
			# SANS octobre pour cat 1, AVEC les 4 grands acheteurs 
			'new_data\\data_1.csv'
			# SANS octobre pour cat 1, cat2 et cat0, AVEC les 4 grands acheteurs 
			'new_data\\data_2.csv'
			# Sans octobre pour cat 1, SANS les 4 grands acheteurs 
			'new_data\\data_1a.csv'
			# SANS octobre pour cat 1, cat2 et cat0, SANS les 4 grands acheteurs 
			'new_data\\data_2b.csv'
		- P4_02_scriptanalyse.ipynb contient une analyse partielle des données afin de répondre aux différentes missions
		Quand on exécute ce fichier, il va enregistrer les différents graphiques dans le dossier 'graphes'