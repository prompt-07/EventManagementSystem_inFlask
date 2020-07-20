# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:03:40 2020

@author: Sadashiv
"""
import os
from flask import Flask,render_template,request,send_from_directory
from flask_mysqldb import MySQL


app=Flask(__name__)

 
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''#hidden_beneath_OS-Module
app.config['MYSQL_DB']='event_management'
mysql=MySQL(app)

#------------------------------------------------------------------------------------------------


@app.route('/')
def home():
	return render_template("index.html")


@app.route('/aboutUs')
def aboutUs():
	return render_template("aboutus.html")


@app.route('/specialevents')
def spEvents():
	return render_template("specialevents.html")


@app.route('/register',methods=['POST','GET'])
def register():

	if request.method == 'POST':
		result=request.form

	for key in result:
		event_code=key

	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,(event_code,))
	data=cur.fetchone()
	cur.close()
	m=int(data[3])
	m=m+m
	m=str(m)
	return (m)



#------------------------------------------------------------------------------------------------------

@app.route('/upload_sports/<filename>')
def send_images_sports(filename):
	return send_from_directory("./static/sports",filename)


@app.route('/sports')
def sports():
    cat_img='Sports_cat.png'
    src_name='send_images_sports'

    sports_img_lst=os.listdir('./static/sports')
    event_list=['Carrom','Box Cricket','Futsal','Kabaddi','Neo Cricket','Table Tennis','Tug-Of-War','Volleyball']
    entry_fees=['100','1000','700','600','150','150','400','400']
    to_events=['/sp_carrom','/sp_boxcricket','/sp_futsal','/sp_kabaddi','/sp_neocricket','/sp_tt','/sp_tow','/sp_volleyball']

    
    sql = 'SELECT * FROM category_data WHERE cat_name=%s'
    cur=mysql.connection.cursor()
    cur.execute(sql,('Sports',))
    data=cur.fetchone()
    cur.close()	

    event_info=zip(sports_img_lst,event_list,entry_fees,to_events)


    
    return render_template('layout_for_disp.html',src_name=src_name,cat_img=cat_img,data=data,event_info=event_info)




@app.route('/sp_carrom')
def carrom():
	event_img='./sports/carrom-singles.png'

	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('sp_carrom',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/sp_boxcricket')
def boxcricket():
	event_img='./sports/cricket.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('sp_boxcricket',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)


@app.route('/sp_futsal')
def futsal():
	event_img='./sports/futsal.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('sp_futsal',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)


@app.route('/sp_kabaddi')
def kabaddi():
	event_img='./sports/Kabaddi.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('sp_kabaddi',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)


@app.route('/sp_neocricket')
def neocricket():
	event_img='./sports/neo-cricket.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('sp_neocricket',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)


@app.route('/sp_tt')
def tt():
	event_img='./sports/table-tennis.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('sp_tt',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)


@app.route('/sp_tow')
def tow():
	event_img='./sports/tug-of-war.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('sp_tow',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)


@app.route('/sp_volleyball')
def volleyball():
	event_img='./sports/volleyball.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('sp_volleyball',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)







#------------------------------------------------------------------------------------------------------





@app.route('/upload_pa/<filename>')
def send_images_pa(filename):
	return send_from_directory("./static/pa",filename)



@app.route('/performing_arts')
def pa():
    cat_img='PA_cat.png'
    src_name='send_images_pa'

    img_lst=os.listdir('./static/pa')
    event_list=['Band','Beat Boxing','Duet Dance','Free Style Group','Free Style Solo','Solo Singing','Rapping','Skit']
    entry_fees=['500','200','300','800','200','200','200','1000']
    to_events=['/pa_band','/pa_beatboxing','/pa_duetdance','/pa_freestylegrp','/pa_freestylesolo','/pa_solosinging','/pa_rapping','/pa_skit']


    sql = 'SELECT * FROM category_data WHERE cat_name=%s'
    cur=mysql.connection.cursor()
    cur.execute(sql,('Performing Arts',))
    data=cur.fetchone()
    cur.close()		

    event_info=zip(img_lst,event_list,entry_fees,to_events)


   
    return render_template('layout_for_disp.html',src_name=src_name,cat_img=cat_img,data=data,event_info=event_info)




@app.route('/pa_band')
def band():
	event_img='./pa/Band.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('pa_band',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)




@app.route('/pa_beatboxing')
def beatboxing():
	event_img='./pa/beat-boxing.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('pa_beatboxing',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)


@app.route('/pa_duetdance')
def duetdance():
	event_img='./pa/duet-dance.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('pa_duetdance',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/pa_freestylegrp')
def freestylegrpt():
	event_img='./pa/free-style-group.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('pa_freestylegrp',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/pa_freestylesolo')
def freestylesolo():
	event_img='./pa/freestylesolo.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('pa_freestylesolo',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/pa_solosinging')
def solosinging():
	event_img='./pa/solosinging.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('pa_solosinging',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/pa_rapping')
def rapping():
	event_img='./pa/rapping.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('pa_rapping',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)


@app.route('/pa_skit')
def skit():
	event_img='./pa/skit.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('pa_skit',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)




#---------------------------------------------------------------------------------------------------------------




@app.route('/upload_la/<filename>')
def send_images_la(filename):
	return send_from_directory("./static/la",filename)



@app.route('/literary_arts')
def la():
    cat_img='LA_cat.png'
    src_name='send_images_la'

    sql = 'SELECT * FROM category_data WHERE cat_name=%s'
    cur=mysql.connection.cursor()
    cur.execute(sql,('Literary Arts',))
    data=cur.fetchone()
    cur.close()	

    img_lst=os.listdir('./static/la')
    event_list=['Elocution','Debate','Essay Writing','Poem Writing']
    entry_fees=['200','150','200','200']
    to_events=['/la_elocution','/la_debate','/la_essaywriting','/la_poemwriting']
    event_info=zip(img_lst,event_list,entry_fees,to_events)


    return render_template('layout_for_disp.html',src_name=src_name,cat_img=cat_img,data=data,event_info=event_info)

@app.route('/la_elocution')
def elocution():
	event_img='./la/elocution.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('la_elocution',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/la_essaywriting')
def essaywriting():
	event_img='./la/essaywriting.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('la_essaywriting',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)


@app.route('/la_debate')
def debate():
	event_img='./la/english-debate.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('la_debate',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/la_poemwriting')
def poemwriting():
	event_img='./la/poem-writing.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('la_poemwriting',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)








#----------------------------------------------------------------------------------------------------------------


@app.route('/upload_gaming/<filename>')
def send_images_gaming(filename):
	return send_from_directory("./static/gaming",filename)



@app.route('/gaming')
def gaming():
    cat_img='Gaming_cat.png'
    src_name='send_images_gaming'

    sql = 'SELECT * FROM category_data WHERE cat_name=%s'
    cur=mysql.connection.cursor()
    cur.execute(sql,('Gaming',))
    data=cur.fetchone()
    cur.close()	


    img_lst=os.listdir('./static/gaming')
    event_list=['CS GO','Fruit Ninja','Pocket Tanks','Pubg']
    entry_fees=['400','100','100','200']
    to_events=['/gaming_csgo','/gaming_fruitninja','/gaming_pockettanks','/gaming_pubgmob']
    event_info=zip(img_lst,event_list,entry_fees,to_events)


    return render_template('layout_for_disp.html',src_name=src_name,cat_img=cat_img,data=data,event_info=event_info)




@app.route('/gaming_csgo')
def csgo():
	event_img='./gaming/cs-go.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('gaming_csgo',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/gaming_fruitninja')
def fruitninja():
	event_img='./gaming/fruit-ninja.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('gaming_fruitninja',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/gaming_pubgmob')
def pubgmob():
	event_img='./gaming/PUBG-copy.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('gaming_pubgmob',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)


@app.route('/gaming_pockettanks')
def pockettanks():
	event_img='./gaming/Pocket-Tanks.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('gaming_pockettanks',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)





#-------------------------------------------------------------------------------------------------------------------

@app.route('/upload_technical/<filename>')
def send_images_technical(filename):
	return send_from_directory("./static/technical",filename)



@app.route('/technical')
def technical():
    cat_img='Tech_cat.png'
    src_name='send_images_technical'

    sql = 'SELECT * FROM category_data WHERE cat_name=%s'
    cur=mysql.connection.cursor()
    cur.execute(sql,('Technical Events',))
    data=cur.fetchone()
    cur.close()	


    img_lst=os.listdir('./static/technical')
    event_list=['Coding Competition','Hackathon','Product Design','Technical Paper Presentation']
    entry_fees=['200','200','200','100']
    to_events=['/technical_codingcomp','/technical_hackathon','/technical_productdes','/technical_tpp']
    event_info=zip(img_lst,event_list,entry_fees,to_events)


    return render_template('layout_for_disp.html',src_name=src_name,cat_img=cat_img,data=data,event_info=event_info)



@app.route('/technical_codingcomp')
def codingcomp():
	event_img='./technical/coding.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('technical_codingcomp',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/technical_hackathon')
def hackathon():
	event_img='./technical/hackathon.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('technical_hackathon',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/technical_productdes')
def productdes():
	event_img='./technical/Product-Design.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('technical_productdes',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)



@app.route('/technical_tpp')
def tpp():
	event_img='./technical/technical-paper-representation.png'
	
	sql = 'SELECT * FROM event_data WHERE event_code=%s'
	cur=mysql.connection.cursor()
	cur.execute(sql,('technical_tpp',))
	data=cur.fetchone()
	cur.close()	

	return render_template('layout_for_event.html',event_img=event_img,data=data)


#--------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True)