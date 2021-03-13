from flask import(
    Blueprint,flash,g,redirect,render_template,request,url_for
)
from werkzeug.exceptions import abort
from nav.db import get_db

from operator import itemgetter
from itertools import groupby

bp = Blueprint('navigation',__name__)

@bp.route('/')
def index():
    db = get_db()
    links = db.execute(
        'SELECT * FROM links'
    ).fetchall()
    maincg_list = db.execute(
        'SELECT distinct maincategory FROM links'
    ).fetchall() 
    links_list = []
    links.sort(key=itemgetter('maincategory'))
    for i,j in groupby(links,key=itemgetter('maincategory')):
        j = list(j)
        j.sort(key=itemgetter('subcategory'))
        sub_list = []
        for x,y in groupby(j,key=itemgetter('subcategory')):
            y = list(y)
            subdict = {'sub_cg':x,'link':y}
            sub_list.append(subdict)
        maindict = {'main_cg':i,'sub_cg_list':sub_list}
        links_list.append(maindict)
    return render_template('index.html',links=links_list,maincg_list=maincg_list)

@bp.route('/', methods=('POST',))
def add():
    if request.method == 'POST':
        maincategory = request.form['maincategory']
        subcategory = request.form['subcategory']
        urlname = request.form['urlname']
        urllocation = request.form['urllocation']
        error = None
        if not maincategory:
            error = 'Main Category is required.'
        elif not subcategory:
            error = 'Sub Category is required.'
        elif not urlname:
            error = 'URL Name is required.'
        elif not urllocation:
            error = 'URL Location is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO links (maincategory, subcategory, urlname, urllocation)'
                ' VALUES (?, ?, ?, ?)',
                (maincategory, subcategory, urlname, urllocation)
            )
            db.commit()
            return redirect(url_for('navigation.index'))
    return render_template('index.html')

@bp.route('/<int:id>', methods=('GET', 'POST'))
def edit(id):
    if request.method == 'POST':
        maincategory = request.form['maincategory']
        subcategory = request.form['subcategory']
        urlname = request.form['urlname']
        urllocation = request.form['urllocation']
        error = None
        if not maincategory:
            error = 'Main Category is required.'
        elif not subcategory:
            error = 'Sub Category is required.'
        elif not urlname:
            error = 'URL Name is required.'
        elif not urllocation:
            error = 'URL Location is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE links SET maincategory = ? , subcategory = ?, urlname = ?, urllocation = ?'
                ' WHERE id = ?',
                (maincategory, subcategory, urlname, urllocation, id)
            )
            db.commit()
            return redirect(url_for('navigation.index'))
    return render_template('index.html')
    
@bp.route('/<int:id>/delete', methods=('GET', 'POST'))
def delete(id):
    db = get_db()
    db.execute('DELETE FROM links WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('navigation.index'))
