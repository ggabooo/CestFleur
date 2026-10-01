"""C'est Fleur · galería floral. Ejecutar: streamlit run app.py."""
from pathlib import Path
import base64
import io
import json
from html import escape
from urllib.parse import quote

import streamlit as st
from PIL import Image

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="C’est Fleur | Galerie Florale", page_icon="🌷", layout="wide")

@st.cache_data
def image_uri(filename):
    """Sirve las imágenes locales, conservando su transparencia; no usa enlaces externos."""
    path = ROOT / "CATALOGO" / filename
    if not path.is_file():
        return ""
    with Image.open(path) as im:
        im.thumbnail((900, 900))
        output = io.BytesIO()
        im.save(output, format="WEBP", quality=90)
    return "data:image/webp;base64," + base64.b64encode(output.getvalue()).decode()

def e(value):
    return escape(str(value), quote=True)

def contact_url(name):
    number = ''.join(c for c in settings.get('whatsapp', '') if c.isdigit())
    if number:
        return f"https://wa.me/{number}?text=" + quote(f"Hola, me gustaría consultar por {name} de C’est Fleur. ¿Me comparten disponibilidad?")
    return settings['instagram_url']

def price(p):
    if p['precio'] is None:
        return 'Cotiza el tuyo' if p['id'] == 'custom' else 'Consultar precio'
    return f"Q{p['precio']:,.2f}" + e(p.get('sufijo', ''))

def card(p, small=False):
    pictures = p.get('imagenes', [])
    visuals = []
    for index, filename in enumerate(pictures):
        uri = image_uri(filename)
        if uri:
            visuals.append(f'<figure><img src="{uri}" alt="{e(p["nombre"])} · presentación {index+1}" loading="lazy" width="500" height="500"/><figcaption>Presentación {index+1}</figcaption></figure>')
    first_uri = image_uri(pictures[0]) if pictures else ''
    art = f'<img class="art" src="{first_uri}" alt="{e(p["nombre"])}" loading="lazy" width="500" height="500">' if first_uri else '<div class="text-art">Composición floral<br><span>por encargo</span></div>'
    detail = f'<details><summary>{"Ver las " + str(len(visuals)) + " presentaciones" if len(visuals)>1 else "Ver imagen en detalle"}</summary><div class="variants">{"".join(visuals)}</div></details>' if visuals else ''
    return f'''<article class="piece {'mini-piece' if small else ''}" id="{e(p['id'])}">
      <div class="art-wall">{art}</div><div class="plaque">
      <span class="category">{e(p['etiqueta'])}</span><h3>{e(p['nombre'])}</h3>
      <p class="description">{e(p['descripcion'])}</p><p class="price">{price(p)}</p>
      <a class="ask" href="{e(contact_url(p['nombre']))}" target="_blank" rel="noopener noreferrer">Consultar esta pieza ↗</a>
      </div>{detail}</article>'''

def section(kicker, title, intro, ident, products, extra_class=''):
    return f'''<section id="{ident}" class="room {extra_class}"><div class="section-heading"><p class="eyebrow">{kicker}</p><h2>{title}</h2><p>{intro}</p></div><div class="gallery">{''.join(card(p, ident=='mini') for p in products)}</div></section>'''

settings = json.loads((ROOT / 'configuracion.json').read_text(encoding='utf-8'))
catalog = json.loads((ROOT / 'catalogo.json').read_text(encoding='utf-8'))
css = (ROOT / 'estilos.css').read_text(encoding='utf-8')
logo = image_uri('Logo.png')
mini_logo = image_uri('Logomini.png')
hero = image_uri('Quatre-saisons2.png')
html = f'''<style>{css}</style><main class="fleur" id="inicio">
<header class="masthead"><a href="#inicio" class="brand">C’est Fleur<span>GALERIE FLORALE</span></a><nav aria-label="Colecciones"><a href="#florale">Galerie Florale</a><a href="#mini">C’est Fleur Mini</a><a href="#temporada">De temporada</a></nav></header>
<section class="hero"><div class="hero-copy"><p class="eyebrow">UNA GALERÍA PARA REGALAR</p><h1>El arte de<br>decirlo con <em>flores.</em></h1><p class="hero-note">Cada bouquet es exclusivo,<br>como quien lo recibe.</p><a class="button" href="#florale">Recorrer la galería <span>↓</span></a><p class="hero-foot">FLORES · PEQUEÑOS DETALLES · MOMENTOS</p></div><div class="hero-art"><img src="{hero}" alt="Bouquet Quatre-saisons, lirios y hortensias en un marco dorado" width="500" height="500"><span>QUATRE-SAISONS &nbsp; / &nbsp; COLECCIÓN FLORAL</span></div></section>
<div class="intro-line"><span>Flores que se convierten en recuerdos.</span><span>Bienvenido a C’est Fleur</span></div>
'''
html += section('SALA I', 'Galerie Florale', 'Bouquets para celebrar, agradecer y querer. Encuentra la composición que habla por ti.', 'florale', [p for p in catalog if p['sala']=='florale'])
html += f'<div class="mini-intro"><img src="{mini_logo}" alt="C’est Fleur Mini" width="280" height="158"><p>Pequeñas piezas. Grandes gestos.</p></div>'
html += section('SALA II', '', '', 'mini', [p for p in catalog if p['sala']=='mini'], 'mini-room')
html += section('SALA III', 'Fleurs de saison', 'La belleza de lo que llega con su temporada. Consulta disponibilidad antes de hacer tu pedido.', 'temporada', [p for p in catalog if p['sala']=='temporada'], 'season-room')
html += f'''<section class="visit" id="pedidos"><div><p class="eyebrow">TU PRÓXIMO GESTO EMPIEZA AQUÍ</p><h2>Hablemos de flores.</h2><p>Cuéntanos qué quieres celebrar y te ayudamos a elegir.</p><a class="button" href="{e(contact_url('un pedido'))}" target="_blank" rel="noopener noreferrer">{('Escríbenos por WhatsApp' if settings.get('whatsapp') else 'Escríbenos en Instagram')} ↗</a></div><div class="conditions"><h3>Antes de encargar</h3><p><strong>01 · Reserva</strong><br>{e(settings['reserva'])}</p><p><strong>02 · Entrega</strong><br>{e(settings['envio'])}</p><p><strong>03 · A tu gusto</strong><br>Consulta colores de los envoltorios y disponibilidad de las flores.</p></div></section>
<footer><img src="{logo}" alt="Logo C’est Fleur" width="160" height="90"><p>C’est Fleur<br><span>Una galería de flores, hecha para regalar.</span></p><a href="{e(settings['instagram_url'])}" target="_blank" rel="noopener noreferrer">@cestfleur ↗</a><a href="#inicio">Volver arriba ↑</a></footer></main>'''
st.html(html)
