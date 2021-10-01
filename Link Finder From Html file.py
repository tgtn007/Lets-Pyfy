with open('link.html') as l :
	with open('Only_Links.txt', 'a') as w :
		page=l.read()
		link_exist=True
		while link_exist :
			pos=page.find('<a href=')
			if pos==-1 :
				link_exist=False
			fst_qot=page.find('"',pos)
			snd_qot=page.find('"',fst_qot+1)
			url=page[fst_qot+1:snd_qot]
			w.write(url + '\n')
			page=page[snd_qot :]